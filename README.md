# Dell Unisphere Client

A Python client library and command-line interface for interacting with Dell EMC Unisphere REST API for Unity storage systems.

## Features

- Complete API client for Dell Unisphere REST API
- Command-line interface for all API operations
- Stateless authentication with per-request authentication
- CSRF token handling
- Software upgrade management with enhanced monitoring capabilities
- Estimated time tracking for upgrade tasks
- File upload support
- Comprehensive error handling with improved logging

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

The CLI has been reorganized into a more intuitive nested command structure with three main command groups:

**System Operations**
```
unisphere system <command>
```
- `login`: Login to the Unisphere API
- `logout`: Logout from the Unisphere API
- `configure`: Configure the client
- `info`: Get basic system information
- `software-version`: Get installed software version information

**Candidate Software Operations**
```
unisphere candidate <command>
```
- `version`: Get candidate software versions
- `upload`: Upload a software package
- `prepare`: Prepare an uploaded software package

**Upgrade Operations**
```
unisphere upgrade <command>
```
- `sessions`: Get software upgrade sessions
- `verify`: Verify upgrade eligibility
- `create`: Create a software upgrade session
- `resume`: Resume a software upgrade session
- `cancel`: Cancel a software upgrade session
- `monitor`: Monitor the upgrade session (stateless operation)

The version information is now displayed in the help banner when running `unisphere` without arguments or with `--help`.

All commands support the following flags:
- `--json` - Output the raw JSON response
- `--verbose` - Enable detailed request and response visualization for API calls

### Library Usage

You can use the Dell Unisphere Client as a library in your Python code. The client is now fully stateless, authenticating with each API call:

```python
from dell_unisphere_client.client import UnisphereClient

# Create a client
client = UnisphereClient(
    base_url="https://your-unisphere-server",
    username="admin",
    password="Password123!",
    verify_ssl=False,
    verbose=True,  # Enable detailed request and response output
)

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

# Monitor upgrade sessions with estimated time information
upgrade_sessions = client.monitor_upgrade_sessions()
print(f"Total estimated time remaining: {upgrade_sessions['total_estimated_time']}")
for task in upgrade_sessions['tasks']:
    print(f"Task: {task['caption']} - Estimated time: {task['estimated_time']}")

# Upload a software package
client.upload_software_package("/path/to/software-package.bin")
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

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes.
