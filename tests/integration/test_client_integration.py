"""Integration tests for the UnisphereClient with mock API."""

import responses
from unittest.mock import patch, MagicMock

from dell_unisphere_client.client import UnisphereClient


class TestClientIntegration:
    """Integration tests for the UnisphereClient class with mocked API responses."""

    @responses.activate
    def test_login_logout_flow(self):
        """Test the complete login and logout flow."""
        # Setup client
        client = UnisphereClient(
            base_url="https://example.com",
            username="testuser",
            password="testpass",
            verify_ssl=True,
        )

        # Mock login response
        responses.add(
            responses.GET,
            "https://example.com/api/types/loginSessionInfo/instances",
            json={"content": {"id": "session123"}},
            status=200,
            headers={
                "EMC-CSRF-TOKEN": "test-token",
                "Set-Cookie": "mod_sec_emc=test-cookie",
            },
        )

        # Mock logout response
        responses.add(
            responses.POST,
            "https://example.com/api/types/loginSessionInfo/action/logout",
            json={},
            status=200,
        )

        # Execute login
        login_result = client.login()
        assert login_result is True
        assert client.csrf_token == "test-token"
        assert client.session is not None

        # Execute logout
        logout_result = client.logout()
        assert logout_result is True
        assert client.csrf_token is None
        assert client.session is None

    @responses.activate
    def test_software_version_workflow(self):
        """Test the complete software version workflow."""
        # Setup client with authenticated session
        client = UnisphereClient(
            base_url="https://example.com",
            username="testuser",
            password="testpass",
            verify_ssl=True,
        )
        client.csrf_token = "test-token"
        client.session = MagicMock()

        # Mock installed software version response
        installed_version_response = {
            "entries": [
                {
                    "content": {
                        "id": "1",
                        "version": "5.3.0.0.5.120",
                        "releaseDate": "2025-01-15T00:00:00.000Z",
                        "installationDate": "2025-02-01T10:30:00.000Z",
                    }
                }
            ]
        }
        responses.add(
            responses.GET,
            "https://example.com/api/types/installedSoftwareVersion/instances",
            json=installed_version_response,
            status=200,
        )

        # Mock candidate software versions response
        candidate_versions_response = {
            "entries": [
                {
                    "content": {
                        "id": "1",
                        "version": "5.4.0.0.5.150",
                        "releaseDate": "2025-02-15T00:00:00.000Z",
                    }
                }
            ]
        }
        responses.add(
            responses.GET,
            "https://example.com/api/types/candidateSoftwareVersion/instances",
            json=candidate_versions_response,
            status=200,
        )

        # Mock verify upgrade eligibility response
        verify_response = {"content": {"isEligible": True, "messages": []}}
        responses.add(
            responses.POST,
            "https://example.com/api/types/upgradeSession/action/verifyUpgradeEligibility",
            json=verify_response,
            status=200,
        )

        # Mock create upgrade session response
        create_response = {
            "content": {
                "id": "123",
                "status": "Scheduled",
                "candidateVersion": "5.4.0.0.5.150",
            }
        }
        responses.add(
            responses.POST,
            "https://example.com/api/types/upgradeSession/instances",
            json=create_response,
            status=200,
        )

        # Execute workflow
        installed_version = client.get_installed_software_version()
        assert installed_version == installed_version_response

        candidate_versions = client.get_candidate_software_versions()
        assert candidate_versions == candidate_versions_response

        verify_result = client.verify_upgrade_eligibility("5.4.0.0.5.150")
        assert verify_result == verify_response

        create_result = client.create_upgrade_session("5.4.0.0.5.150")
        assert create_result == create_response

    @responses.activate
    def test_upgrade_session_workflow(self):
        """Test the complete upgrade session workflow."""
        # Setup client with authenticated session
        client = UnisphereClient(
            base_url="https://example.com",
            username="testuser",
            password="testpass",
            verify_ssl=True,
        )
        client.csrf_token = "test-token"
        client.session = MagicMock()

        # Mock upgrade sessions response
        sessions_response = {
            "entries": [
                {
                    "content": {
                        "id": "123",
                        "status": "Paused",
                        "candidateVersion": "5.4.0.0.5.150",
                        "percentComplete": 45,
                    }
                }
            ]
        }
        responses.add(
            responses.GET,
            "https://example.com/api/types/upgradeSession/instances",
            json=sessions_response,
            status=200,
        )

        # Mock resume upgrade session response
        resume_response = {
            "content": {
                "id": "123",
                "status": "InProgress",
                "candidateVersion": "5.4.0.0.5.150",
            }
        }
        responses.add(
            responses.POST,
            "https://example.com/api/instances/upgradeSession/123/action/resume",
            json=resume_response,
            status=200,
        )

        # Execute workflow
        sessions = client.get_software_upgrade_sessions()
        assert sessions == sessions_response

        resume_result = client.resume_upgrade_session("123")
        assert resume_result == resume_response

    @responses.activate
    def test_upload_package_workflow(self):
        """Test the package upload workflow."""
        # Setup client with authenticated session
        client = UnisphereClient(
            base_url="https://example.com",
            username="testuser",
            password="testpass",
            verify_ssl=True,
        )
        client.csrf_token = "test-token"
        client.session = MagicMock()

        # Mock upload response
        upload_response = {"content": {"id": "456", "version": "5.4.0.0.5.150"}}
        responses.add(
            responses.POST,
            "https://example.com/upload/files/types/candidateSoftwareVersion",
            json=upload_response,
            status=200,
        )

        # Mock file open
        mock_file = MagicMock()
        mock_open = MagicMock(return_value=mock_file)

        # Execute workflow
        with patch("builtins.open", mock_open):
            upload_result = client.upload_package("/path/to/package.bin")
            assert upload_result == upload_response
