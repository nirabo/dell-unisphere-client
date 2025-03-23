"""Unit tests for the version module."""

import importlib.metadata
from unittest.mock import patch

from dell_unisphere_client.version import get_version, __version__


class TestVersion:
    """Test suite for the version module."""

    def test_get_version_installed(self):
        """Test get_version when package is installed."""
        with patch("importlib.metadata.version", return_value="1.2.3") as mock_version:
            version = get_version()

            mock_version.assert_called_once_with("dell-unisphere-client")
            assert version == "1.2.3"

    def test_get_version_not_installed(self):
        """Test get_version when package is not installed."""
        with patch("importlib.metadata.version") as mock_version:
            # Make importlib.metadata.version raise PackageNotFoundError
            mock_version.side_effect = importlib.metadata.PackageNotFoundError(
                "dell-unisphere-client"
            )

            version = get_version()

            mock_version.assert_called_once_with("dell-unisphere-client")
            assert version == "0.2.0"  # Default version

    def test_version_constant(self):
        """Test that __version__ is defined."""
        assert __version__ is not None
        assert isinstance(__version__, str)
