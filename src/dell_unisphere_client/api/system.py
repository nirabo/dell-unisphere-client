"""System API endpoints for Dell Unisphere."""

from typing import Any, Dict

from dell_unisphere_client.api.base import BaseApiClient


class SystemApi(BaseApiClient):
    """API client for system-related endpoints."""

    def get_basic_system_info(self) -> Dict[str, Any]:
        """Get basic system information.

        This endpoint does not require authentication.

        Returns:
            System information with extracted fields.
        """
        response = self.request("GET", "/api/types/basicSystemInfo/instances")
        if isinstance(response, list) and len(response) > 0:
            # Extract first system info entry
            system_info = response[0]
            return {
                "name": system_info.get("name", "Unknown"),
                "model": system_info.get("model", "Unknown"),
                "serialNumber": system_info.get("serialNumber", "Unknown"),
            }
        return {}

    def get_system_info(self) -> Dict[str, Any]:
        """Get system information.

        Returns:
            System information with content field.
        """
        response = self.get_basic_system_info()
        return {
            "content": {
                "name": response.get("name", "Unknown"),
                "model": response.get("model", "Unknown"),
                "serialNumber": response.get("serialNumber", "Unknown"),
            }
        }

    def get_system(self) -> Dict[str, Any]:
        """Get system information.

        Returns:
            System information.
        """
        return self.request("GET", "/api/types/system/instances")
