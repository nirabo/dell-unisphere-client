#!/usr/bin/env python3
"""
Dell Unisphere Client Response Inspector

This script uses the Dell Unisphere client as a library to make API requests
and inspect the full server responses, including error details.
"""

import argparse
import json
import logging
import sys
from typing import Dict, Any, Optional

from dell_unisphere_client.client import UnisphereClient
from dell_unisphere_client.api.base import BaseApiClient


class ResponseInspector(BaseApiClient):
    """Extension of BaseApiClient that captures raw responses."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_response = None
        self.last_request_info = None

    def request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """Override request method to capture raw response."""
        # Store request info
        self.last_request_info = {
            "method": method,
            "path": path,
            "params": params,
            "data": data,
            "json_data": json_data,
            "headers": headers,
        }

        # Create a local variable with a different name to avoid namespace conflict with json module
        json_payload = json_data

        # Make the request and capture the raw response
        url = self.url(path)
        request_headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-EMC-REST-CLIENT": "true",
        }

        if headers:
            request_headers.update(headers)

        # Add CSRF token for POST/DELETE requests
        if method.upper() in ["POST", "DELETE"]:
            if self.csrf_token:
                request_headers["EMC-CSRF-TOKEN"] = self.csrf_token

        # Make the request
        response = self.session.request(
            method=method,
            url=url,
            params=params,
            data=data,
            json=json_payload,
            headers=request_headers,
            verify=self.verify_ssl,
            timeout=self.timeout,
        )

        # Store the raw response
        self.last_response = response

        # Return the processed response
        try:
            return response.json()
        except ValueError:
            return {"status": "success", "status_code": response.status_code}


class ResponseInspectorClient(UnisphereClient):
    """Extension of UnisphereClient that uses ResponseInspector for API calls."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.inspector = None

    def login(self):
        """Override login to use ResponseInspector."""
        # Call the parent login method
        result = super().login()

        # Replace the API clients with our inspector
        self.inspector = ResponseInspector(
            base_url=self.base_url,
            session=self.session_manager.session,
            csrf_token=self.session_manager.csrf_token,
            verify_ssl=self.verify_ssl,
            timeout=self.timeout,
            verbose=self.verbose,
        )

        # Replace the API clients with our inspector
        self.system = self.inspector
        self.software = self.inspector
        self.upgrade = self.inspector

        return result

    def get_last_response(self):
        """Get the last raw response."""
        if self.inspector and self.inspector.last_response:
            return self.inspector.last_response
        return None

    def get_last_request_info(self):
        """Get the last request info."""
        if self.inspector and self.inspector.last_request_info:
            return self.inspector.last_request_info
        return None


def setup_logging(verbose: bool):
    """Set up logging configuration."""
    log_level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )


def print_response_details(response, request_info=None):
    """Print detailed information about a response."""
    if not response:
        print("No response available")
        return

    print("\n" + "=" * 80)
    print("RESPONSE INSPECTOR")
    print("=" * 80)

    if request_info:
        print("\nREQUEST DETAILS:")
        print(f"  Method: {request_info['method']}")
        print(f"  Path: {request_info['path']}")
        if request_info["params"]:
            print(f"  Params: {json.dumps(request_info['params'], indent=2)}")
        if request_info["json_data"]:
            print(f"  JSON Data: {json.dumps(request_info['json_data'], indent=2)}")
        if request_info["headers"]:
            print(f"  Headers: {json.dumps(request_info['headers'], indent=2)}")

    print("\nRESPONSE DETAILS:")
    print(f"  Status Code: {response.status_code}")
    print(f"  Reason: {response.reason}")

    print("\nRESPONSE HEADERS:")
    for key, value in response.headers.items():
        print(f"  {key}: {value}")

    print("\nRESPONSE BODY:")
    try:
        json_response = response.json()
        print(json.dumps(json_response, indent=2))
    except ValueError:
        print(f"  {response.text}")

    print("\n" + "=" * 80)


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Dell Unisphere Client Response Inspector"
    )
    parser.add_argument("--url", required=True, help="Base URL of the Unisphere API")
    parser.add_argument("--username", required=True, help="Username for authentication")
    parser.add_argument("--password", required=True, help="Password for authentication")
    parser.add_argument(
        "--version", required=True, help="Candidate version for upgrade"
    )
    parser.add_argument(
        "--verify-ssl", action="store_true", help="Verify SSL certificates"
    )
    parser.add_argument(
        "--timeout", type=int, default=600, help="Request timeout in seconds"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose logging"
    )

    args = parser.parse_args()

    # Set up logging
    setup_logging(args.verbose)

    # Initialize the client
    client = ResponseInspectorClient(
        base_url=args.url,
        username=args.username,
        password=args.password,
        verify_ssl=args.verify_ssl,
        timeout=args.timeout,
        verbose=args.verbose,
    )

    # Login
    try:
        client.login()
        print("Login successful")
    except Exception as e:
        print(f"Login failed: {e}")
        sys.exit(1)

    # Try to create an upgrade session
    try:
        print(f"Creating upgrade session with version: {args.version}")
        result = client.create_upgrade_session(args.version)
        print("Result:", result)
    except Exception as e:
        print(f"Error creating upgrade session: {e}")

    # Print the detailed response
    response = client.get_last_response()
    request_info = client.get_last_request_info()
    print_response_details(response, request_info)

    # Also try to get all upgrade sessions
    try:
        print("\nGetting all upgrade sessions:")
        sessions = client.get_upgrade_sessions()
        print("Sessions:", sessions)
    except Exception as e:
        print(f"Error getting upgrade sessions: {e}")

    # Print the detailed response
    response = client.get_last_response()
    request_info = client.get_last_request_info()
    print_response_details(response, request_info)


if __name__ == "__main__":
    main()
