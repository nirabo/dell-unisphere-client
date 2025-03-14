"""Version management module for Dell Unisphere Client"""

import importlib.metadata
import logging

logger = logging.getLogger(__name__)


def get_version() -> str:
    """
    Get the current version of the package from metadata.

    Returns:
        str: The current version string.
    """
    try:
        return importlib.metadata.version("dell-unisphere-client")
    except importlib.metadata.PackageNotFoundError:
        logger.warning("Package not installed, version information not available")
        return "0.1.0"  # Default version


# Version constant for easy access
__version__ = get_version()
