"""Unit tests for the CLI module."""

import argparse
from unittest.mock import patch, MagicMock

from dell_unisphere_client.cli import (
    main,
    parse_args,
    cmd_version,
    cmd_configure,
    cmd_login,
    cmd_logout,
    cmd_system_info,
    cmd_software_version,
    cmd_candidate_versions,
    cmd_upgrade_sessions,
    cmd_verify_upgrade,
    cmd_create_upgrade,
    cmd_resume_upgrade,
    cmd_upload_package,
)
from dell_unisphere_client.version import __version__


class TestCLI:
    """Test suite for the CLI module."""

    def test_parse_args_version(self):
        """Test parse_args with version command."""
        with patch("sys.argv", ["uniclient", "version"]):
            args = parse_args()
            assert args.command == "version"

    def test_parse_args_configure(self):
        """Test parse_args with configure command."""
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
            args = parse_args()
            assert args.command == "configure"
            assert args.url == "https://example.com"
            assert args.username == "testuser"
            assert args.password == "testpass"
            assert args.verify_ssl is True

    def test_parse_args_login(self):
        """Test parse_args with login command."""
        with patch(
            "sys.argv",
            ["uniclient", "login", "--username", "testuser", "--password", "testpass"],
        ):
            args = parse_args()
            assert args.command == "login"
            assert args.username == "testuser"
            assert args.password == "testpass"

    def test_parse_args_logout(self):
        """Test parse_args with logout command."""
        with patch("sys.argv", ["uniclient", "logout"]):
            args = parse_args()
            assert args.command == "logout"

    def test_parse_args_system_info(self):
        """Test parse_args with system-info command."""
        with patch("sys.argv", ["uniclient", "system-info"]):
            args = parse_args()
            assert args.command == "system-info"

    def test_parse_args_software_version(self):
        """Test parse_args with software-version command."""
        with patch("sys.argv", ["uniclient", "software-version"]):
            args = parse_args()
            assert args.command == "software-version"

    def test_parse_args_candidate_versions(self):
        """Test parse_args with candidate-versions command."""
        with patch("sys.argv", ["uniclient", "candidate-versions"]):
            args = parse_args()
            assert args.command == "candidate-versions"

    def test_parse_args_upgrade_sessions(self):
        """Test parse_args with upgrade-sessions command."""
        with patch("sys.argv", ["uniclient", "upgrade-sessions"]):
            args = parse_args()
            assert args.command == "upgrade-sessions"

    def test_parse_args_verify_upgrade(self):
        """Test parse_args with verify-upgrade command."""
        with patch(
            "sys.argv", ["uniclient", "verify-upgrade", "--version", "5.4.0.0.5.150"]
        ):
            args = parse_args()
            assert args.command == "verify-upgrade"
            assert args.version == "5.4.0.0.5.150"

    def test_parse_args_create_upgrade(self):
        """Test parse_args with create-upgrade command."""
        with patch(
            "sys.argv", ["uniclient", "create-upgrade", "--version", "5.4.0.0.5.150"]
        ):
            args = parse_args()
            assert args.command == "create-upgrade"
            assert args.version == "5.4.0.0.5.150"

    def test_parse_args_resume_upgrade(self):
        """Test parse_args with resume-upgrade command."""
        with patch("sys.argv", ["uniclient", "resume-upgrade", "--id", "123"]):
            args = parse_args()
            assert args.command == "resume-upgrade"
            assert args.id == "123"

    def test_parse_args_upload_package(self):
        """Test parse_args with upload-package command."""
        with patch(
            "sys.argv",
            ["uniclient", "upload-package", "--file", "/path/to/package.bin"],
        ):
            args = parse_args()
            assert args.command == "upload-package"
            assert args.file == "/path/to/package.bin"

    def test_cmd_version(self, capsys):
        """Test cmd_version function."""
        args = argparse.Namespace()
        cmd_version(args)
        captured = capsys.readouterr()
        assert f"Dell Unisphere Client v{__version__}" in captured.out

    def test_cmd_configure(self, sample_config):
        """Test cmd_configure function."""
        args = argparse.Namespace(
            url="https://example.com",
            username="testuser",
            password="testpass",
            verify_ssl=True,
        )

        with patch("dell_unisphere_client.cli.save_config") as mock_save_config:
            cmd_configure(args)
            mock_save_config.assert_called_once_with(
                {
                    "base_url": "https://example.com",
                    "username": "testuser",
                    "password": "testpass",
                    "verify_ssl": True,
                }
            )

    def test_cmd_login(self, mock_cli_args):
        """Test cmd_login function."""
        args = mock_cli_args(username="testuser", password="testpass")

        with patch("dell_unisphere_client.cli.get_client") as mock_get_client:
            mock_client = MagicMock()
            mock_client.login.return_value = True
            mock_get_client.return_value = mock_client

            cmd_login(args)

            mock_get_client.assert_called_once()
            mock_client.login.assert_called_once()

    def test_cmd_login_with_password_prompt(self, mock_cli_args):
        """Test cmd_login function with password prompt."""
        args = mock_cli_args(
            username="testuser",
            password=None,
            test_password_prompt=True,  # Add flag to enable password prompt in test
        )

        with (
            patch("dell_unisphere_client.cli.get_client") as mock_get_client,
            patch("getpass.getpass", return_value="promptedpass") as mock_getpass,
        ):
            mock_client = MagicMock()
            mock_client.login.return_value = True
            mock_get_client.return_value = mock_client

            cmd_login(args)

            mock_getpass.assert_called_once_with("Password: ")
            mock_get_client.assert_called_once_with(password="promptedpass")
            mock_client.login.assert_called_once()

    def test_cmd_logout(self):
        """Test cmd_logout function."""
        args = argparse.Namespace()

        with patch("dell_unisphere_client.cli.get_client") as mock_get_client:
            mock_client = MagicMock()
            mock_client.logout.return_value = True
            mock_get_client.return_value = mock_client

            cmd_logout(args)

            mock_get_client.assert_called_once()
            mock_client.logout.assert_called_once()

    def test_cmd_system_info(self):
        """Test cmd_system_info function."""
        args = argparse.Namespace()

        with (
            patch("dell_unisphere_client.cli.get_client") as mock_get_client,
            patch("dell_unisphere_client.cli.console.print") as mock_print,
        ):
            mock_client = MagicMock()
            mock_client.get_system_info.return_value = {
                "content": {"name": "Test System"}
            }
            mock_get_client.return_value = mock_client

            cmd_system_info(args)

            mock_get_client.assert_called_once()
            mock_client.get_system_info.assert_called_once()
            mock_print.assert_called()

    def test_cmd_software_version(self):
        """Test cmd_software_version function."""
        args = argparse.Namespace()

        with (
            patch("dell_unisphere_client.cli.get_client") as mock_get_client,
            patch("dell_unisphere_client.cli.console.print") as mock_print,
        ):
            mock_client = MagicMock()
            mock_client.get_installed_software_version.return_value = {
                "entries": [{"content": {"version": "5.3.0.0.5.120"}}]
            }
            mock_get_client.return_value = mock_client

            cmd_software_version(args)

            mock_get_client.assert_called_once()
            mock_client.get_installed_software_version.assert_called_once()
            mock_print.assert_called()

    def test_cmd_candidate_versions(self):
        """Test cmd_candidate_versions function."""
        args = argparse.Namespace()

        with (
            patch("dell_unisphere_client.cli.get_client") as mock_get_client,
            patch("dell_unisphere_client.cli.console.print") as mock_print,
        ):
            mock_client = MagicMock()
            mock_client.get_candidate_software_versions.return_value = {
                "entries": [{"content": {"version": "5.4.0.0.5.150"}}]
            }
            mock_get_client.return_value = mock_client

            cmd_candidate_versions(args)

            mock_get_client.assert_called_once()
            mock_client.get_candidate_software_versions.assert_called_once()
            mock_print.assert_called()

    def test_cmd_upgrade_sessions(self):
        """Test cmd_upgrade_sessions function."""
        args = argparse.Namespace()

        with (
            patch("dell_unisphere_client.cli.get_client") as mock_get_client,
            patch("dell_unisphere_client.cli.console.print") as mock_print,
        ):
            mock_client = MagicMock()
            mock_client.get_software_upgrade_sessions.return_value = {
                "entries": [{"content": {"id": "123", "status": "Paused"}}]
            }
            mock_get_client.return_value = mock_client

            cmd_upgrade_sessions(args)

            mock_get_client.assert_called_once()
            mock_client.get_software_upgrade_sessions.assert_called_once()
            mock_print.assert_called()

    def test_cmd_verify_upgrade(self):
        """Test cmd_verify_upgrade function."""
        # Test 1: Standard output
        args = argparse.Namespace(version="5.4.0.0.5.150")

        with (
            patch("dell_unisphere_client.cli.get_client") as mock_get_client,
            patch("dell_unisphere_client.cli.console.print") as mock_print,
        ):
            mock_client = MagicMock()
            mock_client.verify_upgrade_eligibility.return_value = {
                "eligible": True,
                "messages": [],
                "requiredPatches": [],
                "requiredHotfixes": [],
            }
            mock_get_client.return_value = mock_client

            cmd_verify_upgrade(args)

            mock_get_client.assert_called_once()
            # Note: parameter is passed through CLI but not used by API
            mock_client.verify_upgrade_eligibility.assert_called_once_with(
                "5.4.0.0.5.150", raw_json=False
            )
            mock_print.assert_called()

    def test_cmd_verify_upgrade_raw_json(self):
        """Test cmd_verify_upgrade function with raw_json option."""
        # Test with raw_json option
        args = argparse.Namespace(version="5.4.0.0.5.150", raw_json=True)

        with (
            patch("dell_unisphere_client.cli.get_client") as mock_get_client,
            patch("dell_unisphere_client.cli.console.print") as mock_print,
        ):
            mock_client = MagicMock()
            # Raw API response format
            mock_client.verify_upgrade_eligibility.return_value = {
                "content": {"isEligible": True, "messages": []}
            }
            mock_get_client.return_value = mock_client

            cmd_verify_upgrade(args)

            mock_get_client.assert_called_once()
            # Should call with raw_json=True
            mock_client.verify_upgrade_eligibility.assert_called_once_with(
                "5.4.0.0.5.150", raw_json=True
            )
            mock_print.assert_called()

    def test_cmd_verify_upgrade_json_output(self):
        """Test cmd_verify_upgrade function with json_output option."""
        # Test with json_output option
        args = argparse.Namespace(version="5.4.0.0.5.150", json_output=True)

        with (
            patch("dell_unisphere_client.cli.get_client") as mock_get_client,
            patch("dell_unisphere_client.cli.print_json") as mock_print_json,
            patch("dell_unisphere_client.cli.console.print") as mock_print,
        ):
            mock_client = MagicMock()
            mock_client.verify_upgrade_eligibility.return_value = {
                "eligible": True,
                "messages": [],
                "requiredPatches": [],
                "requiredHotfixes": [],
            }
            mock_get_client.return_value = mock_client

            cmd_verify_upgrade(args)

            mock_get_client.assert_called_once()
            mock_client.verify_upgrade_eligibility.assert_called_once_with(
                "5.4.0.0.5.150", raw_json=False
            )
            mock_print_json.assert_called_once()
            mock_print.assert_not_called()

    def test_cmd_verify_upgrade_raw_json_and_json_output(self):
        """Test cmd_verify_upgrade function with both raw_json and json_output options."""
        # Test with both raw_json and json_output options
        args = argparse.Namespace(
            version="5.4.0.0.5.150", raw_json=True, json_output=True
        )

        with (
            patch("dell_unisphere_client.cli.get_client") as mock_get_client,
            patch("dell_unisphere_client.cli.print_json") as mock_print_json,
            patch("dell_unisphere_client.cli.console.print") as mock_print,
        ):
            mock_client = MagicMock()
            # Raw API response format
            mock_client.verify_upgrade_eligibility.return_value = {
                "content": {"isEligible": True, "messages": []}
            }
            mock_get_client.return_value = mock_client

            cmd_verify_upgrade(args)

            mock_get_client.assert_called_once()
            mock_client.verify_upgrade_eligibility.assert_called_once_with(
                "5.4.0.0.5.150", raw_json=True
            )
            mock_print_json.assert_called_once()
            mock_print.assert_not_called()

    def test_cmd_create_upgrade(self):
        """Test cmd_create_upgrade function."""
        args = argparse.Namespace(version="5.4.0.0.5.150")

        with (
            patch("dell_unisphere_client.cli.get_client") as mock_get_client,
            patch("dell_unisphere_client.cli.console.print") as mock_print,
        ):
            mock_client = MagicMock()
            mock_client.create_upgrade_session.return_value = {
                "content": {"id": "123", "status": "Scheduled"}
            }
            mock_get_client.return_value = mock_client

            cmd_create_upgrade(args)

            mock_get_client.assert_called_once()
            mock_client.create_upgrade_session.assert_called_once_with("5.4.0.0.5.150")
            mock_print.assert_called()

    def test_cmd_resume_upgrade(self):
        """Test cmd_resume_upgrade function."""
        args = argparse.Namespace(id="123")

        with (
            patch("dell_unisphere_client.cli.get_client") as mock_get_client,
            patch("dell_unisphere_client.cli.console.print") as mock_print,
        ):
            mock_client = MagicMock()
            mock_client.resume_upgrade_session.return_value = {
                "content": {"id": "123", "status": "InProgress"}
            }
            mock_get_client.return_value = mock_client

            cmd_resume_upgrade(args)

            mock_get_client.assert_called_once()
            mock_client.resume_upgrade_session.assert_called_once_with("123")
            mock_print.assert_called()

    def test_cmd_upload_package(self):
        """Test cmd_upload_package function."""
        args = argparse.Namespace(file="/path/to/package.bin")

        with (
            patch("dell_unisphere_client.cli.get_client") as mock_get_client,
            patch("dell_unisphere_client.cli.console.print") as mock_print,
            patch("os.path.exists", return_value=True),
        ):
            mock_client = MagicMock()
            mock_client.upload_package.return_value = {"content": {"id": "123"}}
            mock_get_client.return_value = mock_client

            cmd_upload_package(args)

            mock_get_client.assert_called_once()
            mock_client.upload_package.assert_called_once_with("/path/to/package.bin")
            mock_print.assert_called()

    def test_cmd_upload_package_file_not_found(self):
        """Test cmd_upload_package function with file not found."""
        args = argparse.Namespace(file="/path/to/nonexistent.bin")

        with (
            patch("dell_unisphere_client.cli.get_client") as mock_get_client,
            patch("dell_unisphere_client.cli.console.print") as mock_print,
            patch("os.path.exists", return_value=False),
        ):

            cmd_upload_package(args)

            mock_get_client.assert_not_called()
            mock_print.assert_called_once()
            assert "File not found" in mock_print.call_args[0][0]

    def test_main(self):
        """Test main function."""
        with (
            patch("dell_unisphere_client.cli.parse_args") as mock_parse_args,
            patch("dell_unisphere_client.cli.cmd_version") as mock_cmd_version,
        ):
            mock_args = argparse.Namespace(command="version")
            mock_parse_args.return_value = mock_args

            main()

            mock_parse_args.assert_called_once()
            mock_cmd_version.assert_called_once_with(mock_args)
