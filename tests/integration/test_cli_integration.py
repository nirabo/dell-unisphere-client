"""Integration tests for the CLI module with mock client."""

import pytest
import os
import tempfile
from unittest.mock import patch, MagicMock

import dell_unisphere_client.cli as cli


class TestCLIIntegration:
    """Integration tests for the CLI module with mocked client."""

    @pytest.fixture
    def temp_config_file(self):
        """Create a temporary config file for testing."""
        # Create a temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a temporary config file path
            config_path = os.path.join(temp_dir, "config.json")

            # Patch the config path
            with patch("dell_unisphere_client.cli.DEFAULT_CONFIG_FILE", config_path):
                yield config_path

    def test_save_load_config(self, temp_config_file):
        """Test saving and loading configuration."""
        # Test data
        config = {
            "base_url": "https://example.com",
            "username": "testuser",
            "password": "testpass",
            "verify_ssl": True,
        }

        # Save config
        cli.save_config(config)

        # Verify file exists
        assert os.path.exists(temp_config_file)

        # Load config
        loaded_config = cli.load_config()

        # Verify loaded config matches saved config
        assert loaded_config == config

    def test_get_client(self, temp_config_file):
        """Test get_client function."""
        # Test data
        config = {
            "base_url": "https://example.com",
            "username": "testuser",
            "password": "testpass",
            "verify_ssl": True,
        }

        # Save config
        cli.save_config(config)

        # Get client
        with patch("dell_unisphere_client.cli.UnisphereClient") as MockClient:
            # Actually call get_client
            cli.get_client()

            # Verify client was created with correct parameters
            MockClient.assert_called_once_with(
                base_url="https://example.com",
                username="testuser",
                password="testpass",
                verify_ssl=True,
            )

    def test_get_client_with_override(self, temp_config_file):
        """Test get_client function with parameter override."""
        # Test data
        config = {
            "base_url": "https://example.com",
            "username": "testuser",
            "password": "testpass",
            "verify_ssl": True,
        }

        # Save config
        cli.save_config(config)

        # Get client with override
        with patch("dell_unisphere_client.cli.UnisphereClient") as MockClient:
            # Actually call get_client with password override
            cli.get_client(password="newpass")

            # Verify client was created with correct parameters
            MockClient.assert_called_once_with(
                base_url="https://example.com",
                username="testuser",
                password="newpass",
                verify_ssl=True,
            )

    def test_cli_workflow(self, temp_config_file, capsys):
        """Test complete CLI workflow."""
        # Mock the UnisphereClient
        mock_client = MagicMock()

        # Configure mock client responses
        mock_client.login.return_value = True
        mock_client.get_installed_software_version.return_value = {
            "entries": [
                {
                    "content": {
                        "id": "1",
                        "version": "5.3.0.0.5.120",
                        "releaseDate": "2025-01-15T00:00:00.000Z",
                    }
                }
            ]
        }
        mock_client.get_candidate_software_versions.return_value = {
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
        mock_client.verify_upgrade_eligibility.return_value = {
            "content": {"isEligible": True, "messages": []}
        }
        mock_client.create_upgrade_session.return_value = {
            "content": {"id": "123", "status": "Scheduled"}
        }
        mock_client.logout.return_value = True

        # Patch the UnisphereClient constructor
        with patch(
            "dell_unisphere_client.cli.UnisphereClient", return_value=mock_client
        ):
            # Step 1: Configure
            with patch(
                "sys.argv",
                [
                    "uniclient",
                    "configure",
                    "--url",
                    "https://example.com",
                    "--username",
                    "testuser",
                    "--password",
                    "testpass",
                    "--verify-ssl",
                    "true",
                ],
            ):
                cli.main()

            # Verify config was saved
            config = cli.load_config()
            assert config["base_url"] == "https://example.com"
            assert config["username"] == "testuser"
            assert config["password"] == "testpass"
            assert config["verify_ssl"] is True

            # Step 2: Login
            with patch("sys.argv", ["uniclient", "login"]):
                cli.main()

            # Verify login was called
            mock_client.login.assert_called_once()

            # Step 3: Get software version
            with patch("sys.argv", ["uniclient", "software-version"]):
                cli.main()

            # Verify get_installed_software_version was called
            mock_client.get_installed_software_version.assert_called_once()

            # Step 4: Get candidate versions
            with patch("sys.argv", ["uniclient", "candidate-versions"]):
                cli.main()

            # Verify get_candidate_software_versions was called
            mock_client.get_candidate_software_versions.assert_called_once()

            # Step 5: Verify upgrade
            with patch(
                "sys.argv",
                ["uniclient", "verify-upgrade", "--version", "5.4.0.0.5.150"],
            ):
                cli.main()

            # Verify verify_upgrade_eligibility was called
            mock_client.verify_upgrade_eligibility.assert_called_once_with(
                "5.4.0.0.5.150"
            )

            # Step 6: Create upgrade
            with patch(
                "sys.argv",
                ["uniclient", "create-upgrade", "--version", "5.4.0.0.5.150"],
            ):
                cli.main()

            # Verify create_upgrade_session was called
            mock_client.create_upgrade_session.assert_called_once_with("5.4.0.0.5.150")

            # Step 7: Logout
            with patch("sys.argv", ["uniclient", "logout"]):
                cli.main()

            # Verify logout was called
            mock_client.logout.assert_called_once()

    def test_error_handling(self, temp_config_file, capsys):
        """Test CLI error handling."""
        # Mock the UnisphereClient
        mock_client = MagicMock()

        # Configure mock client to raise exceptions
        mock_client.login.side_effect = Exception("Authentication failed")

        # Patch the UnisphereClient constructor
        with patch(
            "dell_unisphere_client.cli.UnisphereClient", return_value=mock_client
        ):
            # Configure first
            with patch(
                "sys.argv",
                [
                    "uniclient",
                    "configure",
                    "--url",
                    "https://example.com",
                    "--username",
                    "testuser",
                    "--password",
                    "testpass",
                    "--verify-ssl",
                    "true",
                ],
            ):
                cli.main()

            # Try to login and expect error handling with sys.exit(1)
            with (
                patch("sys.argv", ["uniclient", "login"]),
                pytest.raises(SystemExit) as excinfo,
            ):
                cli.main()

            # Verify exit code is 1
            assert excinfo.value.code == 1

            # Verify error message was printed
            captured = capsys.readouterr()
            assert "Error" in captured.out
            assert "Authentication failed" in captured.out
