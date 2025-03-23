"""Dell Unisphere Client.

This package provides a client for interacting with the Dell Unisphere REST API.
"""

from dell_unisphere_client.client import UnisphereClient
from dell_unisphere_client.exceptions import (
    UnisphereClientError,
    AuthenticationError,
    CSRFTokenError,
    APIError,
)
from dell_unisphere_client.version import __version__

__all__ = [
    "UnisphereClient",
    "UnisphereClientError",
    "AuthenticationError",
    "CSRFTokenError",
    "APIError",
    "__version__",
]
