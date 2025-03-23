"""Exceptions for the Dell Unisphere Client."""

from typing import Any, Optional


class UnisphereClientError(Exception):
    """Base exception for all client errors."""

    def __init__(
        self,
        message: str,
        status_code: Optional[int] = None,
        response: Optional[Any] = None,
    ):
        self.status_code = status_code
        self.response = response
        super().__init__(message)


class AuthenticationError(UnisphereClientError):
    """Raised when authentication fails."""

    pass


class CSRFTokenError(UnisphereClientError):
    """Raised when CSRF token is missing or invalid."""

    pass


class APIError(UnisphereClientError):
    """Raised when the API returns an error."""

    pass
