"""Test data fixtures for Dell Unisphere Client tests."""

import pytest


@pytest.fixture
def sample_config():
    """Sample configuration for testing."""
    return {
        "base_url": "https://example.com",
        "username": "testuser",
        "password": "testpass",
        "verify_ssl": True,
    }


@pytest.fixture
def mock_cli_args():
    """Factory fixture for creating mock CLI arguments."""

    def _create_args(**kwargs):
        """Create a mock args object with the given attributes."""
        return type("Args", (object,), kwargs)

    return _create_args


@pytest.fixture
def sample_software_version():
    """Sample software version response for testing."""
    return {
        "entries": [
            {
                "content": {
                    "id": "1",
                    "version": "5.3.0.0.5.120",
                    "releaseDate": "2025-01-15T00:00:00.000Z",
                    "installationDate": "2025-02-01T10:30:00.000Z",
                    "status": "Installed",
                }
            }
        ]
    }


@pytest.fixture
def sample_candidate_versions():
    """Sample candidate software versions response for testing."""
    return {
        "entries": [
            {
                "content": {
                    "id": "1",
                    "version": "5.4.0.0.5.150",
                    "releaseDate": "2025-02-15T00:00:00.000Z",
                    "status": "Available",
                }
            },
            {
                "content": {
                    "id": "2",
                    "version": "5.4.0.0.5.160",
                    "releaseDate": "2025-03-01T00:00:00.000Z",
                    "status": "Available",
                }
            },
        ]
    }


@pytest.fixture
def sample_upgrade_sessions():
    """Sample upgrade sessions response for testing."""
    return {
        "entries": [
            {
                "content": {
                    "id": "123",
                    "status": "Paused",
                    "candidateVersion": "5.4.0.0.5.150",
                    "percentComplete": 45,
                    "startTime": "2025-03-15T10:00:00.000Z",
                    "estimatedTimeRemaining": "01:30:00",
                }
            },
            {
                "content": {
                    "id": "124",
                    "status": "Completed",
                    "candidateVersion": "5.3.0.0.5.120",
                    "percentComplete": 100,
                    "startTime": "2025-01-15T08:00:00.000Z",
                    "completionTime": "2025-01-15T10:30:00.000Z",
                }
            },
        ]
    }


@pytest.fixture
def sample_system_info():
    """Sample system information response for testing."""
    return {
        "content": {
            "id": "SYS-001",
            "name": "Test Storage System",
            "model": "Unity 500",
            "serialNumber": "UNITY-123456789",
            "operatingEnvironment": "Production",
            "health": {"value": "OK", "descriptionIds": ["SYSTEM_HEALTH_OK"]},
        }
    }
