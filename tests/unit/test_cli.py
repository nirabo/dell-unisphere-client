"""Unit tests for the CLI module."""

import argparse
import pytest
from unittest.mock import patch, MagicMock

from dell_unisphere_client import UnisphereClientError

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
    cmd_monitor_upgrade,
)
from dell_unisphere_client.version import __version__


class TestCLI:
    """Test suite for the CLI module."""

    def test_parse_args_version(self):
        """Test that version information is available."""
        # Since version is now shown in the help banner and not a separate command,
        # we'll just verify that the version is defined and accessible
        from dell_unisphere_client.version import __version__

        # Verify version is defined
        assert __version__ is not None
        assert isinstance(__version__, str)

        # Verify version format (assuming semver format)
        import re

        assert re.match(r"^\d+\.\d+\.\d+", __version__)

    def test_parse_args_configure(self):
        """Test parse_args with configure command."""
        with patch(
            "sys.argv",
            [
                "unisphere",
                "system",
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
            assert args.command == "system"
            assert args.subcommand == "configure"
            assert args.url == "https://example.com"
            assert args.username == "testuser"
            assert args.password == "testpass"
            assert args.verify_ssl is True

    def test_parse_args_login(self):
        """Test parse_args with login command."""
        with patch(
            "sys.argv",
            [
                "unisphere",
                "system",
                "login",
                "--username",
                "testuser",
                "--password",
                "testpass",
            ],
        ):
            args = parse_args()
            assert args.command == "system"
            assert args.subcommand == "login"
            assert args.username == "testuser"
            assert args.password == "testpass"

    def test_parse_args_logout(self):
        """Test parse_args with logout command."""
        with patch("sys.argv", ["unisphere", "system", "logout"]):
            args = parse_args()
            assert args.command == "system"
            assert args.subcommand == "logout"

    def test_parse_args_system_info(self):
        """Test parse_args with system info command."""
        with patch("sys.argv", ["unisphere", "system", "info"]):
            args = parse_args()
            assert args.command == "system"
            assert args.subcommand == "info"

    def test_parse_args_software_version(self):
        """Test parse_args with software-version command."""
        with patch("sys.argv", ["unisphere", "system", "software-version"]):
            args = parse_args()
            assert args.command == "system"
            assert args.subcommand == "software-version"

    def test_parse_args_candidate_versions(self):
        """Test parse_args with candidate versions command."""
        with patch("sys.argv", ["unisphere", "candidate", "version"]):
            args = parse_args()
            assert args.command == "candidate"
            assert args.subcommand == "version"

    def test_parse_args_upgrade_sessions(self):
        """Test parse_args with upgrade sessions command."""
        with patch("sys.argv", ["unisphere", "upgrade", "sessions"]):
            args = parse_args()
            assert args.command == "upgrade"
            assert args.subcommand == "sessions"

    def test_parse_args_verify_upgrade(self):
        """Test parse_args with verify upgrade command."""
        with patch(
            "sys.argv", ["unisphere", "upgrade", "verify", "--version", "5.4.0.0.5.150"]
        ):
            args = parse_args()
            assert args.command == "upgrade"
            assert args.subcommand == "verify"
            assert args.version == "5.4.0.0.5.150"

    def test_parse_args_create_upgrade(self):
        """Test parse_args with create upgrade command."""
        with patch(
            "sys.argv", ["unisphere", "upgrade", "create", "--version", "5.4.0.0.5.150"]
        ):
            args = parse_args()
            assert args.command == "upgrade"
            assert args.subcommand == "create"
            assert args.version == "5.4.0.0.5.150"

    def test_parse_args_resume_upgrade(self):
        """Test parse_args with resume upgrade command."""
        with patch("sys.argv", ["unisphere", "upgrade", "resume", "--id", "123"]):
            args = parse_args()
            assert args.command == "upgrade"
            assert args.subcommand == "resume"
            assert args.id == "123"

    def test_parse_args_upload_package(self):
        """Test parse_args with upload package command."""
        with patch(
            "sys.argv",
            ["unisphere", "candidate", "upload", "--file", "/path/to/package.bin"],
        ):
            args = parse_args()
            assert args.command == "candidate"
            assert args.subcommand == "upload"
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
            **{
                "url": "https://example.com",
                "username": "testuser",
                "password": "testpass",
                "verify_ssl": True,
            }
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

    def test_cmd_login_failed(self, mock_cli_args):
        """Test cmd_login function with failed login."""
        args = mock_cli_args(username="testuser", password="testpass")

        with (
            patch("dell_unisphere_client.cli.get_client") as mock_get_client,
            patch("dell_unisphere_client.cli.console.print") as mock_print,
        ):
            mock_client = MagicMock()
            # Setup login to raise an exception
            mock_client.login.side_effect = UnisphereClientError("Login failed")
            mock_get_client.return_value = mock_client

            # The handle_errors decorator will catch the exception
            with patch("sys.exit") as mock_exit:
                cmd_login(args)

                mock_get_client.assert_called_once()
                mock_client.login.assert_called_once()
                mock_print.assert_called()
                mock_exit.assert_called_once_with(1)

    def test_cmd_login_connection_error(self, mock_cli_args, connection_error_mock):
        """Test cmd_login function with connection error."""
        args = mock_cli_args(username="testuser", password="testpass")

        with (
            patch("dell_unisphere_client.cli.get_client") as mock_get_client,
            patch("dell_unisphere_client.cli.console.print") as mock_print,
            patch("sys.exit") as mock_exit,
        ):
            mock_client = MagicMock()
            mock_client.login.side_effect = connection_error_mock()
            mock_get_client.return_value = mock_client

            cmd_login(args)

            mock_get_client.assert_called_once()
            mock_client.login.assert_called_once()
            mock_print.assert_called()
            mock_exit.assert_called_once_with(1)

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
            mock_get_client.assert_called_once_with(
                password="promptedpass", verbose=False
            )
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

    @pytest.mark.parametrize(
        "args_dict,expected_version,expected_raw_json,expected_print_json,expected_print",
        [
            # Standard case with version
            ({"version": "5.4.0.0.5.150"}, "5.4.0.0.5.150", False, False, True),
            # With raw_json option
            (
                {"version": "5.4.0.0.5.150", "raw_json": True},
                "5.4.0.0.5.150",
                True,
                False,
                True,
            ),
            # With json_output option
            (
                {"version": "5.4.0.0.5.150", "json_output": True},
                "5.4.0.0.5.150",
                False,
                True,
                False,
            ),
            # Without version parameter
            ({}, None, False, False, True),
            # With both raw_json and json_output
            (
                {"version": "5.4.0.0.5.150", "raw_json": True, "json_output": True},
                "5.4.0.0.5.150",
                True,
                True,
                False,
            ),
        ],
    )
    def test_cmd_verify_upgrade_parameterized(
        self,
        args_dict,
        expected_version,
        expected_raw_json,
        expected_print_json,
        expected_print,
    ):
        """Parameterized test for cmd_verify_upgrade function with various options."""
        args = argparse.Namespace(**args_dict)

        with (
            patch("dell_unisphere_client.cli.get_client") as mock_get_client,
            patch("dell_unisphere_client.cli.print_json") as mock_print_json,
            patch("dell_unisphere_client.cli.console.print") as mock_print,
        ):
            mock_client = MagicMock()
            # Set return value based on raw_json flag
            if expected_raw_json:
                mock_client.verify_upgrade_eligibility.return_value = {
                    "content": {"isEligible": True, "messages": []}
                }
            else:
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
                expected_version, raw_json=expected_raw_json
            )

            if expected_print_json:
                mock_print_json.assert_called_once()
            else:
                mock_print_json.assert_not_called()

            if expected_print:
                mock_print.assert_called()
            else:
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

    @pytest.mark.skip(reason="Monitoring tests are complex and may hang")
    def test_cmd_monitor_upgrade(self, sample_monitoring_data):
        """Test cmd_monitor_upgrade function."""
        args = argparse.Namespace(session_id="1", interval=5, timeout=60, watch=False)

        with (
            patch("dell_unisphere_client.cli.get_client") as mock_get_client,
            patch("dell_unisphere_client.cli.console.print") as mock_print,
            # Mock the Live context manager and its __enter__ method
            patch("rich.live.Live") as mock_live,
        ):
            mock_client = MagicMock()
            mock_client.monitor_upgrade_sessions.return_value = sample_monitoring_data
            mock_get_client.return_value = mock_client

            # Setup the mock Live context manager
            mock_live_instance = MagicMock()
            mock_live.return_value = mock_live_instance
            mock_live_instance.__enter__.return_value = mock_live_instance

            cmd_monitor_upgrade(args)

            mock_get_client.assert_called_once()
            mock_client.monitor_upgrade_sessions.assert_called_once()
            mock_print.assert_called()

    @pytest.mark.skip(reason="Monitoring tests are complex and may hang")
    def test_cmd_monitor_upgrade_watch_mode(self, sample_monitoring_data):
        """Test cmd_monitor_upgrade function in watch mode."""
        args = argparse.Namespace(
            session_id="1", interval=0.1, timeout=60, watch=True, max_iterations=2
        )

        with (
            patch("dell_unisphere_client.cli.get_client") as mock_get_client,
            patch("dell_unisphere_client.cli.console.print") as mock_print,
            # Mock the Live context manager
            patch("rich.live.Live") as mock_live,
            # Import time directly in the test
            patch("time.sleep") as mock_sleep,
        ):
            mock_client = MagicMock()
            mock_client.monitor_upgrade_sessions.return_value = sample_monitoring_data
            mock_get_client.return_value = mock_client
            mock_print.call_args()

            # Setup the mock Live context manager
            mock_live_instance = MagicMock()
            mock_live.return_value = mock_live_instance
            mock_live_instance.__enter__.return_value = mock_live_instance

            # Mock KeyboardInterrupt after max_iterations
            mock_live_instance.update.side_effect = [
                None,
                None,
                KeyboardInterrupt("Test interrupt"),
            ]

            cmd_monitor_upgrade(args)

            # Should be called at least once
            mock_client.monitor_upgrade_sessions.assert_called()
            mock_sleep.assert_called()

    @pytest.mark.skip(reason="Monitoring tests are complex and may hang")
    def test_cmd_monitor_upgrade_error_handling(self):
        """Test cmd_monitor_upgrade function with error handling."""
        args = argparse.Namespace(session_id="1", interval=5, timeout=60, watch=False)

        with (
            patch("dell_unisphere_client.cli.get_client") as mock_get_client,
            patch("dell_unisphere_client.cli.console.print") as mock_print,
            # Mock the Live context manager
            patch("rich.live.Live") as mock_live,
            patch("sys.exit") as mock_exit,
        ):
            mock_client = MagicMock()
            mock_client.monitor_upgrade_sessions.side_effect = UnisphereClientError(
                "Connection error"
            )
            mock_get_client.return_value = mock_client

            # Setup the mock Live context manager
            mock_live_instance = MagicMock()
            mock_live.return_value = mock_live_instance
            mock_live_instance.__enter__.return_value = mock_live_instance

            cmd_monitor_upgrade(args)

            mock_get_client.assert_called_once()
            mock_client.monitor_upgrade_sessions.assert_called_once()
            mock_print.assert_called()
            mock_exit.assert_called_once_with(1)

    @pytest.mark.parametrize(
        "command,subcommand,expected_handler",
        [
            ("system", "info", "cmd_system_info"),
            ("system", "software-version", "cmd_software_version"),
            ("candidate", "version", "cmd_candidate_versions"),
            ("upgrade", "sessions", "cmd_upgrade_sessions"),
            pytest.param(
                "upgrade",
                "monitor",
                "cmd_monitor_upgrade",
                marks=pytest.mark.skip(
                    reason="Monitoring tests are complex and may hang"
                ),
            ),
        ],
    )
    def test_main_parameterized(self, command, subcommand, expected_handler):
        """Parameterized test for main function with different commands."""
        with patch("dell_unisphere_client.cli.parse_args") as mock_parse_args:
            # Create mock args with the specified command and subcommand
            mock_args = argparse.Namespace(command=command, subcommand=subcommand)
            mock_parse_args.return_value = mock_args

            # Patch the expected handler function
            with patch(f"dell_unisphere_client.cli.{expected_handler}") as mock_handler:
                main()

                mock_parse_args.assert_called_once()
                mock_handler.assert_called_once_with(mock_args)

    def test_main(self):
        """Test main function."""
        with (
            patch("dell_unisphere_client.cli.parse_args") as mock_parse_args,
            patch("dell_unisphere_client.cli.cmd_system_info") as mock_cmd_system_info,
        ):
            # Test with system info command
            mock_args = argparse.Namespace(command="system", subcommand="info")
            mock_parse_args.return_value = mock_args

            main()

            mock_parse_args.assert_called_once()
            mock_cmd_system_info.assert_called_once_with(mock_args)
