# Dell Unisphere Client

A Python client library and command-line interface for interacting with Dell EMC Unisphere REST API for Unity storage systems.

## Features

- Complete API client for Dell Unisphere REST API
- Command-line interface for all API operations
- Authentication and session management
- CSRF token handling
- Software upgrade management
- File upload support

## Installation

### Using astral uv

```bash
uv install -e .
```

## Usage

### Command-Line Interface

The Dell Unisphere Client provides a command-line interface for interacting with the Dell Unisphere API. The CLI is available as the `unisphere` command after installation.

#### Configuration

Before using the CLI, you need to configure it with your Dell Unisphere API credentials:

```bash
unisphere configure --url https://your-unisphere-server --username admin
```

You will be prompted for your password.

#### Commands

- `unisphere version`: Show version information
- `unisphere configure`: Configure the client
- `unisphere login`: Login to the Unisphere API
- `unisphere logout`: Logout from the Unisphere API
- `unisphere system-info`: Get basic system information
- `unisphere software-version`: Get installed software version information
- `unisphere candidate-versions`: Get candidate software versions
- `unisphere upgrade-sessions`: Get software upgrade sessions
- `unisphere verify-upgrade <candidate-id>`: Verify upgrade eligibility
- `unisphere create-upgrade <candidate-id>`: Create a software upgrade session
- `unisphere resume-upgrade <session-id>`: Resume a software upgrade session
- `unisphere upload-package <file-path>`: Upload a software package

All commands support the `--json` flag to output the raw JSON response.

### Library Usage

You can also use the Dell Unisphere Client as a library in your Python code:

```python
from dell_unisphere_client.client import UnisphereClient

# Create a client
client = UnisphereClient(
    base_url="https://your-unisphere-server",
    username="admin",
    password="Password123!",
    verify_ssl=False,
)

# Login to the API
client.login()

# Get basic system information
system_info = client.get_basic_system_info()
print(system_info)

# Get installed software version
software_version = client.get_installed_software_version()
print(software_version)

# Get candidate software versions
candidate_versions = client.get_candidate_software_versions()
print(candidate_versions)

# Verify upgrade eligibility
eligibility = client.verify_upgrade_eligibility("candidate-version-id")
print(eligibility)

# Create an upgrade session
session = client.create_upgrade_session("candidate-version-id", "Upgrade to new version")
print(session)

# Resume an upgrade session
client.resume_upgrade_session("session-id")

# Upload a software package
client.upload_software_package("/path/to/software-package.bin")

# Logout from the API
client.logout()
```

You can also use the client as a context manager:

```python
from dell_unisphere_client.client import UnisphereClient

with UnisphereClient(
    base_url="https://your-unisphere-server",
    username="admin",
    password="Password123!",
    verify_ssl=False,
) as client:
    # Get basic system information
    system_info = client.get_basic_system_info()
    print(system_info)
```

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/dell-unisphere-client.git
cd dell-unisphere-client

# Install dependencies
uv install -e .
```

### Running Tests

```bash
make test
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
