"""End-to-end tests for the Dell Unisphere Client.

These tests require a running Dell Unisphere API server to run against.
They can be skipped if no server is available by setting the environment variable:
SKIP_E2E_TESTS=1
"""

import os
import pytest
import json

from dell_unisphere_client.client import UnisphereClient


# Skip all tests in this module if SKIP_E2E_TESTS is set
pytestmark = pytest.mark.skipif(
    os.environ.get("SKIP_E2E_TESTS", "0") == "1",
    reason="Skipping E2E tests as requested by environment variable",
)


class TestE2EClient:
    """End-to-end test suite for the UnisphereClient class.

    These tests require a running Dell Unisphere API server.
    """

    @pytest.fixture
    def server_config(self):
        """Load server configuration for E2E tests."""
        # Try to load from environment variables first
        base_url = os.environ.get("UNISPHERE_URL")
        username = os.environ.get("UNISPHERE_USERNAME")
        password = os.environ.get("UNISPHERE_PASSWORD")
        verify_ssl = os.environ.get("UNISPHERE_VERIFY_SSL", "True").lower() in (
            "true",
            "1",
            "yes",
        )

        # If not available from environment, try to load from config file
        if not all([base_url, username, password]):
            config_path = os.environ.get(
                "UNISPHERE_CONFIG",
                os.path.expanduser("~/.dell-unisphere-client/e2e_config.json"),
            )
            try:
                with open(config_path, "r") as f:
                    config = json.load(f)
                    base_url = base_url or config.get("base_url")
                    username = username or config.get("username")
                    password = password or config.get("password")
                    if "verify_ssl" in config:
                        verify_ssl = config["verify_ssl"]
            except (FileNotFoundError, json.JSONDecodeError):
                pass

        # Skip tests if configuration is incomplete
        if not all([base_url, username, password]):
            pytest.skip(
                "Unisphere server configuration incomplete. Set environment variables or config file."
            )

        return {
            "base_url": base_url,
            "username": username,
            "password": password,
            "verify_ssl": verify_ssl,
        }

    @pytest.fixture
    def client(self, server_config):
        """Create and configure a client for testing."""
        client = UnisphereClient(
            base_url=server_config["base_url"],
            username=server_config["username"],
            password=server_config["password"],
            verify_ssl=server_config["verify_ssl"],
        )

        # Login to the server
        client.login()

        # Yield the client for the test
        yield client

        # Logout after the test
        try:
            client.logout()
        except Exception:
            pass  # Ignore logout failures in cleanup

    def test_login_logout(self, server_config):
        """Test the login and logout functionality."""
        client = UnisphereClient(
            base_url=server_config["base_url"],
            username=server_config["username"],
            password=server_config["password"],
            verify_ssl=server_config["verify_ssl"],
        )

        # Verify login
        login_result = client.login()
        assert login_result is True
        assert client.csrf_token is not None
        assert client.session is not None

        # Verify logout
        logout_result = client.logout()
        assert logout_result is True
        assert client.csrf_token is None
        assert client.session is None

    def test_get_installed_software_version(self, client):
        """Test retrieving the installed software version."""
        result = client.get_installed_software_version()

        # Verify response structure
        assert "entries" in result
        assert len(result["entries"]) > 0

        # Verify content of first entry
        first_entry = result["entries"][0]["content"]
        assert "version" in first_entry
        assert "releaseDate" in first_entry

    def test_get_candidate_software_versions(self, client):
        """Test retrieving candidate software versions."""
        result = client.get_candidate_software_versions()

        # Verify response structure
        assert "entries" in result

        # If there are entries, verify their structure
        if result["entries"]:
            first_entry = result["entries"][0]["content"]
            assert "version" in first_entry
            assert "releaseDate" in first_entry

    def test_get_software_upgrade_sessions(self, client):
        """Test retrieving software upgrade sessions."""
        result = client.get_software_upgrade_sessions()

        # Check if the endpoint is not implemented in this server
        if "detail" in result and result["detail"] == "Not Found":
            pytest.skip(
                "Software upgrade sessions endpoint not implemented in this server"
            )

        # Verify response structure
        assert "entries" in result

        # If there are entries, verify their structure
        if result["entries"]:
            first_entry = result["entries"][0]["content"]
            assert "id" in first_entry
            assert "status" in first_entry

    def test_verify_upgrade_eligibility(self, client):
        """Test verifying upgrade eligibility.

        Note: This test requires a valid candidate version.
        """
        # Get candidate versions
        candidates = client.get_candidate_software_versions()

        # Skip test if no candidates available
        if not candidates["entries"]:
            pytest.skip(
                "No candidate versions available for testing upgrade eligibility"
            )

        # Use the first candidate version
        candidate_version = candidates["entries"][0]["content"]["version"]

        # Verify upgrade eligibility
        result = client.verify_upgrade_eligibility(candidate_version)

        # Verify response structure
        assert "content" in result
        assert "isEligible" in result["content"]
        assert "messages" in result["content"]

    @pytest.mark.skip(
        reason="Creating an upgrade session can have side effects on the system"
    )
    def test_create_upgrade_session(self, client):
        """Test creating an upgrade session.

        Note: This test is skipped by default as it can have side effects.
        """
        # Get candidate versions
        candidates = client.get_candidate_software_versions()

        # Skip test if no candidates available
        if not candidates["entries"]:
            pytest.skip("No candidate versions available for testing upgrade creation")

        # Use the first candidate version
        candidate_version = candidates["entries"][0]["content"]["version"]

        # Create upgrade session
        result = client.create_upgrade_session(candidate_version)

        # Verify response structure
        assert "content" in result
        assert "id" in result["content"]
        assert "status" in result["content"]

    @pytest.mark.skip(
        reason="Resuming an upgrade session can have side effects on the system"
    )
    def test_resume_upgrade_session(self, client):
        """Test resuming an upgrade session.

        Note: This test is skipped by default as it can have side effects.
        """
        # Get upgrade sessions
        sessions = client.get_software_upgrade_sessions()

        # Skip test if no paused sessions available
        paused_sessions = [
            entry["content"]
            for entry in sessions["entries"]
            if entry["content"]["status"] == "Paused"
        ]

        if not paused_sessions:
            pytest.skip("No paused upgrade sessions available for testing resume")

        # Use the first paused session
        session_id = paused_sessions[0]["id"]

        # Resume upgrade session
        result = client.resume_upgrade_session(session_id)

        # Verify response structure
        assert "content" in result
        assert "id" in result["content"]
        assert "status" in result["content"]

    @pytest.mark.skip(reason="Uploading packages can have side effects on the system")
    def test_upload_package(self, client, tmp_path):
        """Test uploading a package.

        Note: This test is skipped by default as it requires a valid package file
        and can have side effects.
        """
        # Create a dummy package file
        package_path = tmp_path / "dummy_package.bin"
        with open(package_path, "wb") as f:
            f.write(b"DUMMY PACKAGE DATA")

        # Skip this test with a message
        pytest.skip("Package upload test requires a valid package file")

        # Upload package (commented out as it would fail with a dummy file)
        # result = client.upload_package(str(package_path))
        #
        # # Verify response structure
        # assert "content" in result
        # assert "id" in result["content"]
