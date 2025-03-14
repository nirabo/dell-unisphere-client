"""Dell Unisphere API Client.

This module provides a client for interacting with the Dell Unisphere REST API.
"""

import logging

from typing import Any, Dict, Optional
from urllib.parse import urljoin

import requests

logger = logging.getLogger(__name__)


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


class UnisphereClient:
    """Client for interacting with Dell Unisphere REST API."""

    def __init__(
        self,
        base_url: str,
        username: str,
        password: str,
        verify_ssl: bool = True,
        timeout: int = 30,
    ):
        """Initialize the client.

        Args:
            base_url: Base URL of the Unisphere API.
            username: Username for authentication.
            password: Password for authentication.
            verify_ssl: Whether to verify SSL certificates.
            timeout: Request timeout in seconds.
        """
        self.base_url = base_url if base_url.endswith("/") else f"{base_url}/"
        self.username = username
        self.password = password
        self.verify_ssl = verify_ssl
        self.timeout = timeout
        self.session = requests.Session()
        self.session.verify = verify_ssl
        self.session.auth = (username, password)
        self.csrf_token = None
        self._logged_in = False

    def _url(self, path: str) -> str:
        """Construct a full URL from a path.

        Args:
            path: API path.

        Returns:
            Full URL.
        """
        return urljoin(self.base_url, path.lstrip("/"))

    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        """Handle API response.

        Args:
            response: Response object.

        Returns:
            Response data.

        Raises:
            AuthenticationError: When authentication fails.
            APIError: When the API returns an error.
        """
        if response.status_code == 401:
            raise AuthenticationError(
                "Authentication failed", status_code=401, response=response
            )

        if response.status_code >= 400:
            try:
                error_data = response.json()
                error_message = error_data.get("error", {}).get(
                    "messages", ["Unknown error"]
                )[0]
            except (ValueError, KeyError):
                error_message = response.text or "Unknown error"

            raise APIError(
                f"API error: {error_message}",
                status_code=response.status_code,
                response=response,
            )

        # Store CSRF token if present in response headers
        if "EMC-CSRF-TOKEN" in response.headers:
            self.csrf_token = response.headers["EMC-CSRF-TOKEN"]
            logger.debug("Received CSRF token: %s", self.csrf_token)

        # Return response data
        try:
            return response.json()
        except ValueError:
            return {"status": "success", "status_code": response.status_code}

    def _request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """Make an API request.

        Args:
            method: HTTP method.
            path: API path.
            params: Query parameters.
            data: Form data.
            json_data: JSON data.
            headers: Additional headers.

        Returns:
            Response data.

        Raises:
            CSRFTokenError: When CSRF token is missing for POST/DELETE requests.
            APIError: When the API returns an error.
        """
        url = self._url(path)
        request_headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-EMC-REST-CLIENT": "true",
        }

        if headers:
            request_headers.update(headers)

        # Add CSRF token for POST/DELETE requests
        if method.upper() in ["POST", "DELETE"]:
            if not self.csrf_token and not path.endswith(
                ("loginSessionInfo/instances", "auth", "candidateSoftwareVersion")
            ):
                raise CSRFTokenError("CSRF token is required for POST/DELETE requests")
            request_headers["EMC-CSRF-TOKEN"] = self.csrf_token

        logger.debug(
            "Making %s request to %s with headers: %s",
            method,
            url,
            request_headers,
        )

        response = self.session.request(
            method=method,
            url=url,
            params=params,
            data=data,
            json=json_data,
            headers=request_headers,
            timeout=self.timeout,
        )

        return self._handle_response(response)

    def login(self) -> Dict[str, Any]:
        """Login to the Unisphere API.

        Returns:
            Login response data.

        Raises:
            AuthenticationError: When authentication fails.
        """
        try:
            # First, make a GET request to obtain a CSRF token
            response = self._request("GET", "/api/types/loginSessionInfo/instances")
            self._logged_in = True
            return response
        except Exception as e:
            raise AuthenticationError(f"Login failed: {str(e)}")

    def logout(self) -> Dict[str, Any]:
        """Logout from the Unisphere API.

        Returns:
            Logout response data.
        """
        if not self._logged_in:
            return {"status": "success", "message": "Not logged in"}

        try:
            response = self._request(
                "POST", "/api/types/loginSessionInfo/action/logout"
            )
            self._logged_in = False
            self.csrf_token = None
            return response
        except Exception as e:
            logger.error("Logout failed: %s", str(e))
            return {"status": "error", "message": f"Logout failed: {str(e)}"}

    def get_basic_system_info(self) -> Dict[str, Any]:
        """Get basic system information.

        This endpoint does not require authentication.

        Returns:
            System information.
        """
        return self._request("GET", "/api/types/basicSystemInfo/instances")

    def get_system(self) -> Dict[str, Any]:
        """Get system information.

        Returns:
            System information.
        """
        return self._request("GET", "/api/types/system/instances")

    def get_installed_software_version(self) -> Dict[str, Any]:
        """Get installed software version information.

        Returns:
            Installed software version information.
        """
        return self._request("GET", "/api/types/installedSoftwareVersion/instances")

    def get_candidate_software_versions(self) -> Dict[str, Any]:
        """Get candidate software versions.

        Returns:
            Candidate software versions.
        """
        return self._request("GET", "/api/types/candidateSoftwareVersion/instances")

    def get_software_upgrade_sessions(self) -> Dict[str, Any]:
        """Get software upgrade sessions.

        Returns:
            Software upgrade sessions.
        """
        return self._request("GET", "/api/types/softwareUpgradeSession/instances")

    def get_software_upgrade_session(self, session_id: str) -> Dict[str, Any]:
        """Get a specific software upgrade session.

        Args:
            session_id: Session ID.

        Returns:
            Software upgrade session.
        """
        return self._request(
            "GET", f"/api/instances/softwareUpgradeSession/{session_id}"
        )

    def verify_upgrade_eligibility(self, candidate_version_id: str) -> Dict[str, Any]:
        """Verify upgrade eligibility.

        Args:
            candidate_version_id: Candidate version ID.

        Returns:
            Verification result.
        """
        return self._request(
            "POST",
            "/api/types/softwareUpgradeSession/action/verifyUpgradeEligibility",
            json_data={"candidateVersionId": candidate_version_id},
        )

    def create_upgrade_session(
        self, candidate_version_id: str, description: Optional[str] = None
    ) -> Dict[str, Any]:
        """Create a software upgrade session.

        Args:
            candidate_version_id: Candidate version ID.
            description: Session description.

        Returns:
            Created session.
        """
        data = {"candidateVersionId": candidate_version_id}
        if description:
            data["description"] = description

        return self._request(
            "POST",
            "/api/types/softwareUpgradeSession/instances",
            json_data=data,
        )

    def resume_upgrade_session(self, session_id: str) -> Dict[str, Any]:
        """Resume a software upgrade session.

        Args:
            session_id: Session ID.

        Returns:
            Resume result.
        """
        return self._request(
            "POST",
            f"/api/instances/softwareUpgradeSession/{session_id}/action/resume",
        )

    def upload_software_package(self, file_path: str) -> Dict[str, Any]:
        """Upload a software package.

        Args:
            file_path: Path to the software package file.

        Returns:
            Upload result.
        """
        url = self._url("/upload/files/types/candidateSoftwareVersion")
        headers = {
            "X-EMC-REST-CLIENT": "true",
        }

        with open(file_path, "rb") as f:
            files = {"file": (file_path, f, "application/octet-stream")}
            response = self.session.post(
                url,
                headers=headers,
                files=files,
                timeout=self.timeout,
                verify=self.verify_ssl,
            )

        return self._handle_response(response)

    def __enter__(self):
        """Context manager entry.

        Returns:
            Client instance.
        """
        self.login()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit.

        Args:
            exc_type: Exception type.
            exc_val: Exception value.
            exc_tb: Exception traceback.
        """
        self.logout()
