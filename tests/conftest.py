"""Global pytest configuration for Dell Unisphere Client tests."""

import pytest
from unittest.mock import MagicMock


@pytest.fixture
def mock_response():
    """Create a mock response object with customizable attributes."""

    class MockResponse:
        def __init__(
            self, json_data=None, status_code=200, headers=None, text="", cookies=None
        ):
            self.json_data = json_data or {}
            self.status_code = status_code
            self.headers = headers or {}
            self.text = text
            self.cookies = cookies or {}

        def json(self):
            return self.json_data

        def raise_for_status(self):
            if self.status_code >= 400:
                raise Exception(f"HTTP Error: {self.status_code}")

    return MockResponse


@pytest.fixture
def mock_requests(monkeypatch):
    """Create a mock for the requests library."""
    mock = MagicMock()
    monkeypatch.setattr("dell_unisphere_client.client.requests", mock)
    return mock


@pytest.fixture
def mock_client():
    """Create a mock client for testing."""
    from dell_unisphere_client.client import UnisphereClient

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
def mock_cli_args():
    """Create mock CLI arguments."""

    class MockArgs:
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

    return MockArgs
