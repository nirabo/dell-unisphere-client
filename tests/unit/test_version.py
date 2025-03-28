"""Unit tests for the version module."""

import importlib.metadata
from unittest.mock import patch

from dell_unisphere_client.version import get_version, __version__, _VERSION


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
            assert version == _VERSION

    def test_version_constant(self):
        """Test that __version__ is defined."""
        assert __version__ is not None
        assert isinstance(__version__, str)

    def test_version_consistency(self):
        """Test that version in pyproject.toml matches version in version.py."""
        import os
        import re

        # Get the project root directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, "../.."))

        # Read version from pyproject.toml using regex
        pyproject_path = os.path.join(project_root, "pyproject.toml")
        with open(pyproject_path, "r") as f:
            pyproject_content = f.read()
            version_match = re.search(r'version\s*=\s*"([^"]+)"', pyproject_content)
            if not version_match:
                raise ValueError("Could not find version in pyproject.toml")
            pyproject_version = version_match.group(1)

        # Compare with the hard-coded version in version.py
        # This is more reliable than calling get_version() which might use the installed version
        hardcoded_version = _VERSION

        # Assert versions match
        assert pyproject_version == hardcoded_version, (
            f"Version mismatch: pyproject.toml has {pyproject_version}, "
            f"but version.py _VERSION is {hardcoded_version}"
        )

        # Also check that get_version() returns the correct version when package is not installed
        with patch("importlib.metadata.version") as mock_version:
            mock_version.side_effect = importlib.metadata.PackageNotFoundError(
                "dell-unisphere-client"
            )
            default_version = get_version()

        assert default_version == hardcoded_version, (
            f"Version mismatch: version.py _VERSION is {hardcoded_version}, "
            f"but get_version() returns {default_version}"
        )
