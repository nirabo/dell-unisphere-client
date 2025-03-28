"""Version management module for Dell Unisphere Client"""

import importlib.metadata
import logging
import re
from pathlib import Path

logger = logging.getLogger(__name__)


def _read_version_from_pyproject() -> str:
    """
    Read version directly from pyproject.toml.

    Returns:
        str: The version string from pyproject.toml or a default if not found.
    """
    try:
        # Find the project root directory by looking for pyproject.toml
        current_file = Path(__file__)
        # Navigate up from src/dell_unisphere_client/version.py to the project root
        project_root = current_file.resolve().parents[2]  # Go up 3 levels
        pyproject_path = project_root / "pyproject.toml"
        logger.debug("Looking for pyproject.toml at %s", pyproject_path)

        if not pyproject_path.exists():
            logger.warning("pyproject.toml not found at %s", pyproject_path)
            return "0.6.0"  # Default fallback

        # Read version from pyproject.toml using regex
        with open(pyproject_path, "r") as f:
            pyproject_content = f.read()
            version_match = re.search(r'version\s*=\s*"([^"]+)"', pyproject_content)
            if not version_match:
                logger.warning("Could not find version in pyproject.toml")
                return "0.6.0"  # Default fallback
            return version_match.group(1)
    except Exception as e:
        logger.warning("Error reading version from pyproject.toml: %s", e)
        return "0.6.0"  # Default fallback


# Read version from pyproject.toml at import time
_VERSION = _read_version_from_pyproject()


def get_version() -> str:
    """
    Get the current version of the package.

    Always tries to read from pyproject.toml first to ensure consistency.
    Falls back to package metadata only if pyproject.toml cannot be read.

    Returns:
        str: The current version string.
    """
    # Always prioritize reading from pyproject.toml for consistency
    pyproject_version = _read_version_from_pyproject()
    if pyproject_version != "0.6.0":  # Not the default fallback
        return pyproject_version

    # Fallback to package metadata only if pyproject.toml couldn't be read
    try:
        return importlib.metadata.version("dell-unisphere-client")
    except importlib.metadata.PackageNotFoundError:
        logger.warning("Package not installed, using default version")
        return "0.6.0"  # Last resort fallback


# Version constant for easy access
__version__ = get_version()
