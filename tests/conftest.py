"""Global pytest configuration for Dell Unisphere Client tests."""

import pytest
from unittest.mock import MagicMock


@pytest.fixture
def mock_response():
    """Create a mock response object with customizable attributes."""

    class MockResponse:
        def __init__(
            self,
            json_data=None,
            status_code=200,
            headers=None,
            text="",
            cookies=None,
            raise_exception=None,
            timeout=False,
        ):
            """
            Create a mock response object with customizable attributes.

            Args:
                json_data (dict, optional): JSON data to return. Defaults to empty dict.
                status_code (int, optional): HTTP status code. Defaults to 200.
                headers (dict, optional): Response headers. Defaults to empty dict.
                text (str, optional): Response text. Defaults to empty string.
                cookies (dict, optional): Response cookies. Defaults to empty dict.
                raise_exception (Exception, optional): Exception to raise when accessing response.
                timeout (bool, optional): Simulate a request timeout. Defaults to False.
            """
            self.json_data = json_data or {}
            self.status_code = status_code
            self.headers = headers or {}
            self.text = text
            self.cookies = cookies or {}
            self._is_mock = True  # Flag to identify mock responses
            self._raise_exception = raise_exception
            self._timeout = timeout

        def json(self):
            """
            Return the JSON data from the response.

            Raises:
                Exception: If raise_exception was specified during initialization.

            Returns:
                dict: The JSON data.
            """
            if self._raise_exception:
                raise self._raise_exception
            if self._timeout:
                raise TimeoutError("Request timed out")
            return self.json_data

        def raise_for_status(self):
            """
            Raise an exception if the status code indicates an error.

            Raises:
                Exception: If status_code >= 400 or if raise_exception was specified.
            """
            if self._raise_exception:
                raise self._raise_exception
            if self._timeout:
                raise TimeoutError("Request timed out")
            if self.status_code >= 400:
                raise Exception(f"HTTP Error: {self.status_code}")

    return MockResponse


@pytest.fixture
def mock_requests(monkeypatch):
    """Create a mock for the requests library."""
    mock = MagicMock()
    # Patch the requests module
    monkeypatch.setattr("requests.Session", MagicMock)
    monkeypatch.setattr("requests.get", mock.get)
    monkeypatch.setattr("requests.post", mock.post)
    monkeypatch.setattr("requests.put", mock.put)
    monkeypatch.setattr("requests.delete", mock.delete)
    monkeypatch.setattr("dell_unisphere_client.client.requests", mock)
    return mock


@pytest.fixture
def mock_client():
    """Create a mock client for testing."""
    from dell_unisphere_client import UnisphereClient

    client = MagicMock(spec=UnisphereClient)
    client.base_url = "https://example.com"
    client.username = "testuser"
    client.password = "testpass"
    client.verify_ssl = True
    client.session = MagicMock()

    return client


@pytest.fixture
def sample_config():
    """Return a sample configuration dictionary."""
    return {
        "base_url": "https://example.com",
        "username": "testuser",
        "password": "testpass",
        "verify_ssl": True,
    }


@pytest.fixture
def sample_software_version():
    """Return a sample software version response."""
    return {
        "@base": "https://example.com/api/instances/installedSoftwareVersion",
        "updated": "2025-03-14T08:00:00.000Z",
        "links": [{"rel": "self", "href": "/1"}],
        "content": {
            "id": "1",
            "version": "5.3.0.0.5.120",
            "releaseDate": "2025-01-15T00:00:00.000Z",
            "installationDate": "2025-02-01T10:30:00.000Z",
            "isEMCInternal": False,
            "isValid": True,
            "packages": [
                {
                    "name": "Base Package",
                    "version": "5.3.0.0.5.120",
                    "isInstalled": True,
                }
            ],
        },
    }


@pytest.fixture
def sample_candidate_versions():
    """Return a sample candidate versions response."""
    return {
        "@base": "https://example.com/api/types/candidateSoftwareVersion/instances?per_page=2000",
        "updated": "2025-03-14T08:00:00.000Z",
        "links": [{"rel": "self", "href": "&page=1"}],
        "entries": [
            {
                "@base": "https://example.com/api/instances/candidateSoftwareVersion",
                "updated": "2025-03-14T08:00:00.000Z",
                "links": [{"rel": "self", "href": "/1"}],
                "content": {
                    "id": "1",
                    "version": "5.4.0.0.5.150",
                    "releaseDate": "2025-02-15T00:00:00.000Z",
                    "isValid": True,
                    "isEMCInternal": False,
                },
            }
        ],
    }


@pytest.fixture
def sample_upgrade_sessions():
    """Return a sample upgrade sessions response."""
    return {
        "@base": "https://example.com/api/types/upgradeSession/instances?per_page=2000",
        "updated": "2025-03-14T08:00:00.000Z",
        "links": [{"rel": "self", "href": "&page=1"}],
        "entries": [
            {
                "@base": "https://example.com/api/instances/upgradeSession",
                "updated": "2025-03-14T08:00:00.000Z",
                "links": [{"rel": "self", "href": "/1"}],
                "content": {
                    "id": "1",
                    "candidateVersion": "5.4.0.0.5.150",
                    "status": "Paused",
                    "percentComplete": 45,
                    "creationTime": "2025-03-10T14:30:00.000Z",
                    "lastModificationTime": "2025-03-10T15:45:00.000Z",
                },
            }
        ],
    }


@pytest.fixture
def csrf_token():
    """Return a sample CSRF token."""
    return (
        "d2nFivGgU8EiztUJ6IlsFwStrS+s59RxdKTX1mqvuFnOUz2fi",
        "wy1slHlItOu9ET003xOjsJFX+E9UE6jFxck4Ffo/Km9AJj13dsyt/7PkZQ=",
    )


@pytest.fixture
def sample_monitoring_data():
    """Return sample monitoring data for upgrade sessions."""
    return {
        "content": {
            "id": "1",
            "status": "InProgress",
            "caption": "Software upgrade to version 5.4.0.0.5.150",
            "percentComplete": 65,
            "type": "Software Upgrade",
            "elapsedTime": "01:30:45",
            "tasks": [
                {
                    "id": "task1",
                    "name": "Preparing system",
                    "status": "Completed",
                    "percentComplete": 100,
                    "estimatedTimeRemaining": "00:00:00",
                },
                {
                    "id": "task2",
                    "name": "Downloading packages",
                    "status": "Completed",
                    "percentComplete": 100,
                    "estimatedTimeRemaining": "00:00:00",
                },
                {
                    "id": "task3",
                    "name": "Installing packages",
                    "status": "InProgress",
                    "percentComplete": 60,
                    "estimatedTimeRemaining": "00:45:30",
                },
                {
                    "id": "task4",
                    "name": "Finalizing installation",
                    "status": "Pending",
                    "percentComplete": 0,
                    "estimatedTimeRemaining": "01:15:00",
                },
            ],
        }
    }


@pytest.fixture
def sample_error_responses():
    """Return a collection of sample error responses."""
    return {
        "authentication_error": {
            "error": {
                "code": 401,
                "message": "Authentication failed. Invalid credentials.",
            }
        },
        "not_found": {"error": {"code": 404, "message": "Resource not found."}},
        "server_error": {
            "error": {"code": 500, "message": "Internal server error occurred."}
        },
        "upgrade_ineligible": {
            "content": {
                "isEligible": False,
                "messages": [
                    "System has insufficient disk space.",
                    "Required patches are missing.",
                ],
                "requiredPatches": ["patch-123", "patch-456"],
                "requiredHotfixes": ["hotfix-789"],
            }
        },
    }


@pytest.fixture
def connection_error_mock():
    """Create a mock that simulates connection errors."""
    import requests

    class ConnectionErrorMock:
        def __init__(self, error_type="connection"):
            self.error_type = error_type

        def __call__(self, *args, **kwargs):
            if self.error_type == "connection":
                raise requests.exceptions.ConnectionError(
                    "Failed to establish connection"
                )
            elif self.error_type == "timeout":
                raise requests.exceptions.Timeout("Request timed out")
            elif self.error_type == "ssl":
                raise requests.exceptions.SSLError(
                    "SSL certificate verification failed"
                )
            else:
                raise requests.exceptions.RequestException("General request exception")

    return ConnectionErrorMock


@pytest.fixture
def mock_cli_args():
    """Create mock CLI arguments."""

    class MockArgs:
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

    return MockArgs
