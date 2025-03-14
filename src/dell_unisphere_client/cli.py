"""Dell Unisphere CLI.

This module provides a command-line interface for interacting with the Dell Unisphere REST API.
"""

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from rich.console import Console
from rich.logging import RichHandler
from rich.table import Table

from . import __version__
from .client import (
    AuthenticationError,
    UnisphereClient,
    UnisphereClientError,
)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)
logger = logging.getLogger("dell_unisphere_client")

# Create console for rich output
console = Console()

# Default configuration
DEFAULT_CONFIG_DIR = Path.home() / ".config" / "dell-unisphere-client"
DEFAULT_CONFIG_FILE = DEFAULT_CONFIG_DIR / "config.json"
DEFAULT_CONFIG = {
    "base_url": "https://localhost:8000",
    "username": "admin",
    "password": "Password123!",
    "verify_ssl": False,
}


def load_config() -> Dict[str, Any]:
    """Load configuration from file.

    Returns:
        Configuration dictionary.
    """
    if not DEFAULT_CONFIG_FILE.exists():
        return DEFAULT_CONFIG

    try:
        with open(DEFAULT_CONFIG_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        logger.warning(f"Failed to load config: {e}")
        return DEFAULT_CONFIG


def save_config(config: Dict[str, Any]) -> None:
    """Save configuration to file.

    Args:
        config: Configuration dictionary.
    """
    DEFAULT_CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    try:
        with open(DEFAULT_CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=2)
    except Exception as e:
        logger.error(f"Failed to save config: {e}")


def get_client(
    base_url: Optional[str] = None,
    username: Optional[str] = None,
    password: Optional[str] = None,
    verify_ssl: Optional[bool] = None,
) -> UnisphereClient:
    """Get a configured client instance.

    Args:
        base_url: Base URL of the Unisphere API.
        username: Username for authentication.
        password: Password for authentication.
        verify_ssl: Whether to verify SSL certificates.

    Returns:
        Configured client instance.
    """
    config = load_config()

    # Override config with provided values
    if base_url:
        config["base_url"] = base_url
    if username:
        config["username"] = username
    if password:
        config["password"] = password
    if verify_ssl is not None:
        config["verify_ssl"] = verify_ssl

    return UnisphereClient(
        base_url=config["base_url"],
        username=config["username"],
        password=config["password"],
        verify_ssl=config["verify_ssl"],
    )


def print_json(data: Any) -> None:
    """Print data as formatted JSON.

    Args:
        data: Data to print.
    """
    console.print_json(json.dumps(data))


def print_table(data: List[Dict[str, Any]], title: str) -> None:
    """Print data as a table.

    Args:
        data: Data to print.
        title: Table title.
    """
    if not data:
        console.print(f"No {title.lower()} found.")
        return

    table = Table(title=title)

    # Add columns based on first item's keys
    sample = data[0]
    for key in sample.keys():
        table.add_column(key.capitalize())

    # Add rows
    for item in data:
        row = [str(item.get(key, "")) for key in sample.keys()]
        table.add_row(*row)

    console.print(table)


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser for the CLI.

    Returns:
        Configured argument parser.
    """
    parser = argparse.ArgumentParser(
        description="Dell Unisphere CLI - A command-line interface for Dell Unisphere REST API"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output"
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Version command
    subparsers.add_parser("version", help="Show version information")

    # Configure command
    configure_parser = subparsers.add_parser("configure", help="Configure the client")
    configure_parser.add_argument(
        "-u", "--url", required=True, help="Base URL of the Unisphere API"
    )
    configure_parser.add_argument(
        "-U", "--username", required=True, help="Username for authentication"
    )
    configure_parser.add_argument(
        "-P", "--password", required=True, help="Password for authentication"
    )
    configure_parser.add_argument(
        "--verify-ssl",
        action="store_true",
        default=True,
        help="Verify SSL certificates",
    )
    configure_parser.add_argument(
        "--no-verify-ssl",
        action="store_false",
        dest="verify_ssl",
        help="Do not verify SSL certificates",
    )

    # Login command
    login_parser = subparsers.add_parser("login", help="Login to the Unisphere API")
    login_parser.add_argument("-u", "--url", help="Base URL of the Unisphere API")
    login_parser.add_argument("-U", "--username", help="Username for authentication")
    login_parser.add_argument("-P", "--password", help="Password for authentication")
    login_parser.add_argument(
        "--verify-ssl",
        action="store_true",
        dest="verify_ssl",
        help="Verify SSL certificates",
    )
    login_parser.add_argument(
        "--no-verify-ssl",
        action="store_false",
        dest="verify_ssl",
        help="Do not verify SSL certificates",
    )

    # Logout command
    subparsers.add_parser("logout", help="Logout from the Unisphere API")

    # System info command
    system_info_parser = subparsers.add_parser(
        "system-info", help="Get basic system information"
    )
    system_info_parser.add_argument(
        "-j",
        "--json",
        action="store_true",
        dest="json_output",
        help="Output in JSON format",
    )

    # Software version command
    software_version_parser = subparsers.add_parser(
        "software-version", help="Get installed software version information"
    )
    software_version_parser.add_argument(
        "-j",
        "--json",
        action="store_true",
        dest="json_output",
        help="Output in JSON format",
    )

    # Candidate versions command
    candidate_versions_parser = subparsers.add_parser(
        "candidate-versions", help="Get candidate software versions"
    )
    candidate_versions_parser.add_argument(
        "-j",
        "--json",
        action="store_true",
        dest="json_output",
        help="Output in JSON format",
    )

    # Upgrade sessions command
    upgrade_sessions_parser = subparsers.add_parser(
        "upgrade-sessions", help="Get software upgrade sessions"
    )
    upgrade_sessions_parser.add_argument(
        "-j",
        "--json",
        action="store_true",
        dest="json_output",
        help="Output in JSON format",
    )

    # Verify upgrade command
    verify_upgrade_parser = subparsers.add_parser(
        "verify-upgrade", help="Verify upgrade eligibility"
    )
    verify_upgrade_parser.add_argument("candidate_id", help="Candidate version ID")
    verify_upgrade_parser.add_argument(
        "-j",
        "--json",
        action="store_true",
        dest="json_output",
        help="Output in JSON format",
    )

    # Create upgrade command
    create_upgrade_parser = subparsers.add_parser(
        "create-upgrade", help="Create a software upgrade session"
    )
    create_upgrade_parser.add_argument("candidate_id", help="Candidate version ID")
    create_upgrade_parser.add_argument(
        "-d", "--description", help="Session description"
    )
    create_upgrade_parser.add_argument(
        "-j",
        "--json",
        action="store_true",
        dest="json_output",
        help="Output in JSON format",
    )

    # Resume upgrade command
    resume_upgrade_parser = subparsers.add_parser(
        "resume-upgrade", help="Resume a software upgrade session"
    )
    resume_upgrade_parser.add_argument("session_id", help="Session ID")
    resume_upgrade_parser.add_argument(
        "-j",
        "--json",
        action="store_true",
        dest="json_output",
        help="Output in JSON format",
    )

    # Upload package command
    upload_package_parser = subparsers.add_parser(
        "upload-package", help="Upload a software package"
    )
    upload_package_parser.add_argument(
        "file_path", help="Path to the software package file"
    )
    upload_package_parser.add_argument(
        "-j",
        "--json",
        action="store_true",
        dest="json_output",
        help="Output in JSON format",
    )

    return parser


def cmd_version(args: argparse.Namespace) -> None:
    """Show version information.

    Args:
        args: Command line arguments.
    """
    console.print(f"Dell Unisphere Client v{__version__}")


def cmd_configure(args: argparse.Namespace) -> None:
    """Configure the client.

    Args:
        args: Command line arguments.
    """
    config = {
        "base_url": args.url,
        "username": args.username,
        "password": args.password,
        "verify_ssl": args.verify_ssl,
    }
    save_config(config)
    console.print("Configuration saved.")


def cmd_login(args: argparse.Namespace) -> None:
    """Login to the Unisphere API.

    Args:
        args: Command line arguments.
    """
    # If password not provided, prompt for it
    password = args.password
    if password is None:
        import getpass

        password = getpass.getpass("Password: ")

    try:
        client = get_client(args.url, args.username, password, args.verify_ssl)
        client.login()
        console.print("Login successful.")
    except AuthenticationError as e:
        console.print(f"[red]Authentication failed: {str(e)}[/red]")
        sys.exit(1)
    except UnisphereClientError as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)


def cmd_logout(args: argparse.Namespace) -> None:
    """Logout from the Unisphere API.

    Args:
        args: Command line arguments.
    """
    try:
        client = get_client()
        client.logout()
        console.print("Logout successful.")
    except UnisphereClientError as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)


def cmd_system_info(args: argparse.Namespace) -> None:
    """Get basic system information.

    Args:
        args: Command line arguments.
    """
    try:
        client = get_client()
        result = client.get_basic_system_info()

        if args.json_output:
            print_json(result)
        else:
            # Extract the entries from the response
            entries = result.get("entries", [])
            if entries:
                # Get the first entry's content
                content = entries[0].get("content", {})

                # Create a table
                table = Table(title="System Information")
                table.add_column("Attribute")
                table.add_column("Value")

                for key, value in content.items():
                    table.add_row(key, str(value))

                console.print(table)
            else:
                console.print("No system information available.")
    except UnisphereClientError as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)


def cmd_software_version(args: argparse.Namespace) -> None:
    """Get installed software version information.

    Args:
        args: Command line arguments.
    """
    try:
        client = get_client()
        result = client.get_installed_software_version()

        if args.json_output:
            print_json(result)
        else:
            # Extract the entries from the response
            entries = result.get("entries", [])
            if entries:
                # Get the first entry's content
                content = entries[0].get("content", {})

                # Create a table
                table = Table(title="Installed Software Version")
                table.add_column("Attribute")
                table.add_column("Value")

                for key, value in content.items():
                    if isinstance(value, dict):
                        table.add_row(key, json.dumps(value, indent=2))
                    else:
                        table.add_row(key, str(value))

                console.print(table)
            else:
                console.print("No software version information available.")
    except UnisphereClientError as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)


def cmd_candidate_versions(args: argparse.Namespace) -> None:
    """Get candidate software versions.

    Args:
        args: Command line arguments.
    """
    try:
        client = get_client()
        result = client.get_candidate_software_versions()

        if args.json_output:
            print_json(result)
        else:
            # Extract the entries from the response
            entries = result.get("entries", [])
            if entries:
                # Create a list of candidate versions
                candidates = []
                for entry in entries:
                    content = entry.get("content", {})
                    candidates.append(
                        {
                            "id": content.get("id", ""),
                            "version": content.get("version", ""),
                            "status": content.get("status", ""),
                            "type": content.get("type", ""),
                        }
                    )

                print_table(candidates, "Candidate Software Versions")
            else:
                console.print("No candidate software versions available.")
    except UnisphereClientError as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)


def cmd_upgrade_sessions(args: argparse.Namespace) -> None:
    """Get software upgrade sessions.

    Args:
        args: Command line arguments.
    """
    try:
        client = get_client()
        result = client.get_software_upgrade_sessions()

        if args.json_output:
            print_json(result)
        else:
            # Extract the entries from the response
            entries = result.get("entries", [])
            if entries:
                # Create a list of upgrade sessions
                sessions = []
                for entry in entries:
                    content = entry.get("content", {})
                    sessions.append(
                        {
                            "id": content.get("id", ""),
                            "status": content.get("status", ""),
                            "percentComplete": content.get("percentComplete", ""),
                            "description": content.get("description", ""),
                        }
                    )

                print_table(sessions, "Software Upgrade Sessions")
            else:
                console.print("No software upgrade sessions available.")
    except UnisphereClientError as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)


def cmd_verify_upgrade(args: argparse.Namespace) -> None:
    """Verify upgrade eligibility.

    Args:
        args: Command line arguments.
    """
    try:
        client = get_client()
        result = client.verify_upgrade_eligibility(args.candidate_id)

        if args.json_output:
            print_json(result)
        else:
            console.print("Upgrade eligibility verified successfully.")
    except UnisphereClientError as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)


def cmd_create_upgrade(args: argparse.Namespace) -> None:
    """Create a software upgrade session.

    Args:
        args: Command line arguments.
    """
    try:
        client = get_client()
        result = client.create_upgrade_session(args.candidate_id, args.description)

        if args.json_output:
            print_json(result)
        else:
            console.print("Upgrade session created successfully.")
    except UnisphereClientError as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)


def cmd_resume_upgrade(args: argparse.Namespace) -> None:
    """Resume a software upgrade session.

    Args:
        args: Command line arguments.
    """
    try:
        client = get_client()
        result = client.resume_upgrade_session(args.session_id)

        if args.json_output:
            print_json(result)
        else:
            console.print("Upgrade session resumed successfully.")
    except UnisphereClientError as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)


def cmd_upload_package(args: argparse.Namespace) -> None:
    """Upload a software package.

    Args:
        args: Command line arguments.
    """
    try:
        client = get_client()
        result = client.upload_software_package(args.file_path)

        if args.json_output:
            print_json(result)
        else:
            console.print("Software package uploaded successfully.")
    except UnisphereClientError as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)
    except FileNotFoundError:
        console.print(f"[red]Error: File not found: {args.file_path}[/red]")
        sys.exit(1)


def main() -> None:
    """Main entry point for the CLI."""
    parser = create_parser()
    args = parser.parse_args()

    # Set logging level if verbose flag is set
    if args.verbose:
        logger.setLevel(logging.DEBUG)

    # Execute the appropriate command
    if args.command == "version":
        cmd_version(args)
    elif args.command == "configure":
        cmd_configure(args)
    elif args.command == "login":
        cmd_login(args)
    elif args.command == "logout":
        cmd_logout(args)
    elif args.command == "system-info":
        cmd_system_info(args)
    elif args.command == "software-version":
        cmd_software_version(args)
    elif args.command == "candidate-versions":
        cmd_candidate_versions(args)
    elif args.command == "upgrade-sessions":
        cmd_upgrade_sessions(args)
    elif args.command == "verify-upgrade":
        cmd_verify_upgrade(args)
    elif args.command == "create-upgrade":
        cmd_create_upgrade(args)
    elif args.command == "resume-upgrade":
        cmd_resume_upgrade(args)
    elif args.command == "upload-package":
        cmd_upload_package(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
