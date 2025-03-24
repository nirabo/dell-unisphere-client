"""System API endpoints for Dell Unisphere."""

from typing import Any, Dict

from dell_unisphere_client.api.base import BaseApiClient


class SystemApi(BaseApiClient):
    """API client for system-related endpoints."""

    def get_basic_system_info(self) -> Dict[str, Any]:
        """Get basic system information.

        This endpoint does not require authentication.

        Returns:
            System information.
        """
        return self.request("GET", "/api/types/basicSystemInfo/instances")

    def get_system_info(self) -> Dict[str, Any]:
        """Get system information.

        Returns:
            System information.
        """
        return self.get_basic_system_info()

    def get_system(self) -> Dict[str, Any]:
        """Get system information.

        Returns:
            System information.
        """
        return self.request("GET", "/api/types/system/instances")
