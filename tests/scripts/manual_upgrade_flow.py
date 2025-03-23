#!/usr/bin/env python3
"""
Test script for Dell EMC Unisphere Client
This script tests both general API endpoints and the complete upgrade flow
using the Dell Unisphere Client instead of curl.
"""

import os
import sys
import json
import logging
import pytest

from datetime import datetime

from dell_unisphere_client import UnisphereClient

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("test_upgrade_flow")

# Configuration
HOST = "http://localhost:8000"
USERNAME = "admin"
PASSWORD = "Password123!"
REPORT_DIR = "./tests/scripts/test_results"
REPORT_FILE = f"{REPORT_DIR}/test_upgrade_flow_client_report.md"
UPGRADE_FILE = f"{REPORT_DIR}/test_upgrade_client.bin"


class TestReport:
    """Class to handle test reporting."""

    def __init__(self, report_file):
        self.report_file = report_file
        self.ensure_report_dir()
        self.initialize_report()

    def ensure_report_dir(self):
        """Ensure the report directory exists."""
        os.makedirs(os.path.dirname(self.report_file), exist_ok=True)

    def initialize_report(self):
        """Initialize the report file."""
        with open(self.report_file, "w") as f:
            f.write("# Dell Unisphere Client - Comprehensive Test Report\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

    def add_header(self, header):
        """Add a header to the report."""
        with open(self.report_file, "a") as f:
            f.write(f"\n## {header}\n")

    def add_content(self, content):
        """Add content to the report."""
        with open(self.report_file, "a") as f:
            f.write(f"{content}\n")

    def add_code_block(self, content, language=""):
        """Add a code block to the report."""
        with open(self.report_file, "a") as f:
            f.write(f"```{language}\n")
            f.write(f"{content}\n")
            f.write("```\n")

    def add_json(self, data):
        """Add formatted JSON to the report."""
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                self.add_code_block(data)
                return

        formatted_json = json.dumps(data, indent=2)
        self.add_code_block(formatted_json, "json")

    def add_table_header(self, headers):
        """Add a table header to the report."""
        with open(self.report_file, "a") as f:
            f.write("| " + " | ".join(headers) + " |\n")
            f.write("| " + " | ".join(["---"] * len(headers)) + " |\n")

    def add_table_row(self, values):
        """Add a table row to the report."""
        with open(self.report_file, "a") as f:
            f.write("| " + " | ".join(str(v) for v in values) + " |\n")


def check_api(report):
    """Check if the API is running."""
    report.add_header("Checking if API is running")

    try:
        # Simply try to connect to the API using a basic HTTP request
        import requests

        response = requests.get(f"{HOST}/docs", verify=False)

        if response.status_code == 200:
            logger.info(f"API is running at {HOST}")
            report.add_content(f"API is running at {HOST}")
            return True
        else:
            logger.error(
                f"API is not running at {HOST}, status code: {response.status_code}"
            )
            report.add_content(
                f"API is not running at {HOST}, status code: {response.status_code}"
            )
            return False
    except Exception as e:
        logger.error(f"Error checking API: {str(e)}")
        report.add_content(f"Error checking API: {str(e)}")
        return False


def create_dummy_upgrade_file(report):
    """Create a dummy upgrade file for testing."""
    report.add_header("Creating dummy upgrade file")

    try:
        # Create a 10MB file with random data
        with open(UPGRADE_FILE, "wb") as f:
            f.write(os.urandom(10 * 1024 * 1024))  # 10MB

        file_size = os.path.getsize(UPGRADE_FILE) / (1024 * 1024)
        logger.info(f"Created dummy upgrade file: {UPGRADE_FILE} ({file_size:.1f}MB)")
        report.add_content(
            f"Created dummy upgrade file: {UPGRADE_FILE} ({file_size:.1f}MB)"
        )
        return True
    except Exception as e:
        logger.error(f"Error creating dummy file: {str(e)}")
        report.add_content(f"Error creating dummy file: {str(e)}")
        return False


def run_api_tests(client, report):
    """Run general API tests."""
    report.add_header("Running General API Tests")

    # Test 1: Login
    logger.info("Testing: Login")
    report.add_header("Login")
    try:
        client.login()
        report.add_content("Login successful")
        logger.info("Login successful")
    except Exception as e:
        logger.error(f"Error logging in: {str(e)}")
        report.add_content(f"Error: {str(e)}")
        return False

    # Test 2: Get basic system info
    logger.info("Testing: Get basic system info")
    report.add_header("Getting Basic System Info")
    try:
        response = client.get_basic_system_info()
        report.add_json(response)
        logger.info("Basic system info retrieved successfully")
    except Exception as e:
        logger.error(f"Error getting basic system info: {str(e)}")
        report.add_content(f"Error: {str(e)}")

    # Test 3: Get installed software version
    logger.info("Testing: Get installed software version")
    report.add_header("Getting Installed Software Version")
    try:
        response = client.get_installed_software_version()
        report.add_json(response)
        logger.info("Installed software version retrieved successfully")
    except Exception as e:
        logger.error(f"Error getting installed software version: {str(e)}")
        report.add_content(f"Error: {str(e)}")

    # Test 4: Get candidate software versions
    logger.info("Testing: Get candidate software versions")
    report.add_header("Getting Candidate Software Versions")
    try:
        response = client.get_candidate_software_versions()
        report.add_json(response)
        logger.info("Candidate software versions retrieved successfully")
    except Exception as e:
        logger.error(f"Error getting candidate software versions: {str(e)}")
        report.add_content(f"Error: {str(e)}")

    # Test 5: Get software upgrade sessions
    logger.info("Testing: Get software upgrade sessions")
    report.add_header("Getting Software Upgrade Sessions")
    try:
        response = client.get_software_upgrade_sessions()
        report.add_json(response)
        logger.info("Software upgrade sessions retrieved successfully")
    except Exception as e:
        logger.error(f"Error getting software upgrade sessions: {str(e)}")
        report.add_content(f"Error: {str(e)}")

    # Test 6: Verify upgrade eligibility
    logger.info("Testing: Verify upgrade eligibility")
    report.add_header("Verifying Upgrade Eligibility")
    try:
        # Use a dummy version ID for testing
        response = client.verify_upgrade_eligibility("5.4.0.0.5.150")
        report.add_json(response)
        logger.info("Upgrade eligibility verified successfully")
    except Exception as e:
        logger.error(f"Error verifying upgrade eligibility: {str(e)}")
        report.add_content(f"Error: {str(e)}")


@pytest.fixture
def client():
    """Fixture to create and configure a UnisphereClient instance."""
    return UnisphereClient(
        base_url="http://localhost:8000",
        username="admin",
        password="Password123!",
        verify_ssl=False,
    )


@pytest.fixture
def report():
    """Fixture to create a TestReport instance."""
    return TestReport(REPORT_FILE)


def test_upgrade_flow(client, report):
    """Test the complete upgrade flow."""
    report.add_header("Testing Complete Upgrade Flow")
    report.add_content(
        "This test will create an upgrade session and monitor it until completion"
    )

    # Step 1: Create a dummy upgrade file
    logger.info("Step 1: Creating dummy upgrade file")
    report.add_header("Step 1: Creating dummy upgrade file")
    if not create_dummy_upgrade_file(report):
        return False

    # Step 2: Upload the file
    logger.info("Step 2: Uploading software package")
    report.add_header("Step 2: Uploading software package")
    try:
        upload_response = client.upload_package(UPGRADE_FILE)
        report.add_json(upload_response)

        # Extract the file ID
        file_id = None
        if "id" in upload_response:
            file_id = upload_response["id"]
        elif "content" in upload_response and "id" in upload_response["content"]:
            file_id = upload_response["content"]["id"]

        if not file_id:
            logger.error("Failed to extract file ID from upload response")
            report.add_content("Failed to extract file ID from upload response")
            return False

        logger.info(f"Uploaded software package: {file_id}")
        report.add_content(f"Uploaded software package: {file_id}")
    except Exception as e:
        logger.error(f"Error uploading software package: {str(e)}")
        report.add_content(f"Error uploading software package: {str(e)}")
        return False

    # Step 3: Prepare the software
    logger.info("Step 3: Preparing software")
    report.add_header("Step 3: Preparing software")
    try:
        prepare_response = client.prepare_software(file_id)
        report.add_json(prepare_response)
        logger.info("Software prepared successfully")
        report.add_content("Software prepared successfully")
    except Exception as e:
        logger.error(f"Error preparing software: {str(e)}")
        report.add_content(f"Error preparing software: {str(e)}")
        return False

    # Step 4: Get candidate software versions
    logger.info("Step 4: Getting candidate software versions")
    report.add_header("Step 4: Getting candidate software versions")
    try:
        candidate_response = client.get_candidate_software_versions()
        report.add_json(candidate_response)

        # Extract the candidate ID
        candidate_id = None
        if "entries" in candidate_response:
            for entry in candidate_response["entries"]:
                if "content" in entry and "id" in entry["content"]:
                    candidate_id = entry["content"]["id"]
                    break

        if not candidate_id:
            logger.error("No candidate software versions found")
            report.add_content("No candidate software versions found")
            return False

        logger.info(f"Found candidate ID: {candidate_id}")
        report.add_content(f"Found candidate ID: {candidate_id}")
    except Exception as e:
        logger.error(f"Error getting candidate software versions: {str(e)}")
        report.add_content(f"Error getting candidate software versions: {str(e)}")
        return False

    # Step 5: Create an upgrade session
    logger.info("Step 5: Creating upgrade session")
    report.add_header("Step 5: Creating upgrade session")
    try:
        create_session_response = client.create_upgrade_session(candidate_id)
        report.add_json(create_session_response)

        # Debug log the response
        logger.info(
            f"Create session response: {json.dumps(create_session_response, indent=2)}"
        )

        # Extract the session ID
        session_id = None
        if isinstance(create_session_response, dict):
            if "id" in create_session_response:
                session_id = create_session_response["id"]
            elif "content" in create_session_response and isinstance(
                create_session_response["content"], dict
            ):
                if "id" in create_session_response["content"]:
                    session_id = create_session_response["content"]["id"]

        if not session_id:
            # Try to extract from the raw response
            logger.info("Trying alternative session ID extraction methods")
            try:
                # Try to find any field that might contain the session ID
                if isinstance(create_session_response, dict):
                    for key, value in create_session_response.items():
                        logger.info(f"Checking key: {key}, value: {value}")
                        if isinstance(value, dict) and "id" in value:
                            session_id = value["id"]
                            logger.info(f"Found session ID in {key}.id: {session_id}")
                            break
            except Exception as e:
                logger.error(f"Error in alternative extraction: {str(e)}")

        if not session_id:
            logger.error("Failed to extract session ID from create session response")
            report.add_content(
                "Failed to extract session ID from create session response"
            )
            return False

        logger.info(f"Created upgrade session: {session_id}")
        report.add_content(f"Created upgrade session: {session_id}")
    except Exception as e:
        logger.error(f"Error creating upgrade session: {str(e)}")
        report.add_content(f"Error creating upgrade session: {str(e)}")
        return False

    # Step 6: Monitor the upgrade progress
    logger.info("Step 6: Monitoring upgrade progress")
    report.add_header("Step 6: Monitoring upgrade progress")
    report.add_content("Monitoring the upgrade session until completion")

    # Create a table for task status tracking
    report.add_table_header(["Time", "Status", "Progress", "Tasks"])

    try:
        # Use our monitor_upgrade_session method
        final_status = client.monitor_upgrade_session(
            session_id=session_id,
            interval=2,  # Check every 2 seconds
            timeout=120,  # Maximum 2 minutes
        )

        logger.info("Upgrade completed successfully!")
        report.add_content("Upgrade completed successfully!")
        report.add_json(final_status)

        # Extract and display task completion summary
        report.add_header("Task Completion Summary")
        report.add_table_header(["Task Name", "Status", "Duration"])

        if "content" in final_status and "tasks" in final_status["content"]:
            tasks = final_status["content"]["tasks"]
            for task in tasks:
                task_name = task.get("caption", "Unknown")
                task_status = task.get("status", 0)

                # Map status code to text
                status_map = {
                    0: "PENDING",
                    1: "IN_PROGRESS",
                    2: "COMPLETED",
                    3: "FAILED",
                    4: "PAUSED",
                }
                status_text = status_map.get(task_status, f"UNKNOWN({task_status})")

                # Calculate duration if available
                start_time = task.get("startTime", "")
                end_time = task.get("endTime", "")

                duration = "N/A"
                if start_time and end_time:
                    duration = "Completed"
                elif start_time:
                    duration = "In progress"

                report.add_table_row([task_name, status_text, duration])

        return True
    except Exception as e:
        logger.error(f"Error monitoring upgrade: {str(e)}")
        report.add_content(f"Error monitoring upgrade: {str(e)}")
        return False


def cleanup():
    """Clean up after tests."""
    # Remove the dummy upgrade file
    if os.path.exists(UPGRADE_FILE):
        os.remove(UPGRADE_FILE)


def main():
    """Main function."""
    # Create report
    report = TestReport(REPORT_FILE)

    # Check if API is running
    if not check_api(report):
        logger.error("API is not running. Exiting.")
        return 1

    # Create client
    client = UnisphereClient(
        base_url=HOST,
        username=USERNAME,
        password=PASSWORD,
        verify_ssl=False,
    )

    try:
        # Run general API tests
        run_api_tests(client, report)

        # Test the complete upgrade flow
        test_upgrade_flow(client, report)
    except Exception as e:
        logger.error(f"Error during tests: {str(e)}")
        report.add_content(f"Error during tests: {str(e)}")
    finally:
        # Clean up
        cleanup()

        # Logout
        try:
            client.logout()
            logger.info("Logged out successfully")
        except Exception as e:
            logger.error(f"Error logging out: {str(e)}")

    logger.info(f"All tests completed. Results saved in {REPORT_FILE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
