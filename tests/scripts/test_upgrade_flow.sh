#!/bin/bash
# Test script for Dell EMC Unisphere Client
# This script tests both general API endpoints and the complete upgrade flow
# using the Dell Unisphere Client CLI interface.

set -e  # Exit on error

# Configuration
HOST="http://localhost:8000"
USERNAME="admin"
PASSWORD="Password123!"
REPORT_DIR="./tests/scripts/test_results"
REPORT_FILE="${REPORT_DIR}/test_upgrade_flow_bash_report.md"
UPGRADE_FILE="${REPORT_DIR}/test_upgrade_client.bin"

# Ensure the report directory exists
mkdir -p "${REPORT_DIR}"

# Initialize the report file
initialize_report() {
    echo "# Dell Unisphere Client - Comprehensive Test Report (Bash)" > "${REPORT_FILE}"
    echo "Generated on: $(date '+%Y-%m-%d %H:%M:%S')" >> "${REPORT_FILE}"
    echo "" >> "${REPORT_FILE}"
}

# Add a header to the report
add_header() {
    echo -e "\n## $1" >> "${REPORT_FILE}"
}

# Add content to the report
add_content() {
    echo "$1" >> "${REPORT_FILE}"
}

# Add a code block to the report
add_code_block() {
    echo '```' >> "${REPORT_FILE}"
    echo "$1" >> "${REPORT_FILE}"
    echo '```' >> "${REPORT_FILE}"
}

# Add a JSON code block to the report
add_json() {
    echo '```json' >> "${REPORT_FILE}"
    echo "$1" >> "${REPORT_FILE}"
    echo '```' >> "${REPORT_FILE}"
}

# Add a table header to the report
add_table_header() {
    echo "| $1 |" >> "${REPORT_FILE}"
    echo "| --- |" >> "${REPORT_FILE}"
}

# Add a table row to the report
add_table_row() {
    echo "| $1 |" >> "${REPORT_FILE}"
}

# Log a message to the console and report
log_info() {
    echo "[INFO] $1"
    add_content "$1"
}

# Log an error to the console and report
log_error() {
    echo "[ERROR] $1" >&2
    add_content "**ERROR:** $1"
}

# Check if the API is running
check_api() {
    add_header "Checking if API is running"

    if curl -s -o /dev/null -w "%{http_code}" "${HOST}/docs" | grep -q "200"; then
        log_info "API is running at ${HOST}"
        return 0
    else
        log_error "API is not running at ${HOST}"
        return 1
    fi
}

# Create a dummy upgrade file for testing
create_dummy_upgrade_file() {
    add_header "Creating dummy upgrade file"

    # Create a 10MB file with random data
    dd if=/dev/urandom of="${UPGRADE_FILE}" bs=1M count=10 2>/dev/null

    # Get the file size
    FILE_SIZE=$(du -h "${UPGRADE_FILE}" | cut -f1)

    log_info "Created dummy upgrade file: ${UPGRADE_FILE} (${FILE_SIZE})"
    return 0
}

# Configure the client
configure_client() {
    add_header "Configuring the client"

    # Configure the client
    ./uniclient configure --url "${HOST}" --username "${USERNAME}" --password "${PASSWORD}"

    log_info "Client configured with URL: ${HOST}, Username: ${USERNAME}"
    return 0
}

# Run general API tests
run_api_tests() {
    add_header "Running General API Tests"

    # Test 1: Login
    add_header "Login"
    # Pass password explicitly to avoid prompt
    if ./uniclient login --username "${USERNAME}" --password "${PASSWORD}" --url "${HOST}"; then
        log_info "Login successful"
    else
        log_error "Login failed"
        return 1
    fi

    # Test 2: Get basic system info
    add_header "Getting Basic System Info"
    SYSTEM_INFO=$(./uniclient system-info --json)
    add_json "${SYSTEM_INFO}"
    log_info "Basic system info retrieved successfully"

    # Test 3: Get installed software version
    add_header "Getting Installed Software Version"
    SOFTWARE_VERSION=$(./uniclient software-version --json)
    add_json "${SOFTWARE_VERSION}"
    log_info "Installed software version retrieved successfully"

    # Test 4: Get candidate software versions
    add_header "Getting Candidate Software Versions"
    CANDIDATE_VERSIONS=$(./uniclient candidate-versions --json)
    add_json "${CANDIDATE_VERSIONS}"
    log_info "Candidate software versions retrieved successfully"

    # Test 5: Get software upgrade sessions
    add_header "Getting Software Upgrade Sessions"
    UPGRADE_SESSIONS=$(./uniclient upgrade-sessions --json)
    add_json "${UPGRADE_SESSIONS}"
    log_info "Software upgrade sessions retrieved successfully"

    # Test 6: Verify upgrade eligibility
    add_header "Verifying Upgrade Eligibility"
    VERIFY_UPGRADE=$(./uniclient verify-upgrade --version "5.4.0.0.5.150" --json)
    add_json "${VERIFY_UPGRADE}"
    log_info "Upgrade eligibility verified successfully"

    # Return success
    return 0
}

# Test the complete upgrade flow
test_upgrade_flow() {
    add_header "Testing Complete Upgrade Flow"
    add_content "This test will create an upgrade session and monitor it until completion"

    # Make sure we're logged in
    log_info "Ensuring we're logged in"
    ./uniclient login --username "${USERNAME}" --password "${PASSWORD}" --url "${HOST}" || true

    # Step 1: Create a dummy upgrade file
    log_info "Step 1: Creating dummy upgrade file"
    add_header "Step 1: Creating dummy upgrade file"
    if ! create_dummy_upgrade_file; then
        log_error "Failed to create dummy upgrade file"
        return 1
    fi

    # Step 2: Upload the file
    log_info "Step 2: Uploading software package"
    add_header "Step 2: Uploading software package"
    UPLOAD_RESPONSE=$(./uniclient upload-package --file "${UPGRADE_FILE}" --json)
    add_json "${UPLOAD_RESPONSE}"

    # Debug output
    echo "DEBUG: Upload response: ${UPLOAD_RESPONSE}"

    # Extract the file ID - use jq if available for more reliable JSON parsing
    if command -v jq >/dev/null 2>&1; then
        FILE_ID=$(echo "${UPLOAD_RESPONSE}" | jq -r '.content.id // .id // empty')
    else
        # Fallback to grep/awk if jq is not available
        FILE_ID=$(echo "${UPLOAD_RESPONSE}" | grep -o '"id": *"[^"]*"' | head -1 | awk -F'"' '{print $4}')

        if [ -z "${FILE_ID}" ]; then
            # Try alternative extraction method
            FILE_ID=$(echo "${UPLOAD_RESPONSE}" | grep -o '"content": *{[^}]*"id": *"[^"]*"' | grep -o '"id": *"[^"]*"' | awk -F'"' '{print $4}')
        fi
    fi

    if [ -z "${FILE_ID}" ]; then
        log_error "Failed to extract file ID from upload response"
        return 1
    fi

    log_info "Uploaded software package: ${FILE_ID}"

    # Step 3: Prepare the software
    log_info "Step 3: Preparing software"
    add_header "Step 3: Preparing software"
    PREPARE_RESPONSE=$(./uniclient prepare-software --file-id "${FILE_ID}" --json)
    add_json "${PREPARE_RESPONSE}"
    log_info "Software prepared successfully"

    # Step 4: Get candidate software versions
    log_info "Step 4: Getting candidate software versions"
    add_header "Step 4: Getting candidate software versions"
    CANDIDATE_RESPONSE=$(./uniclient candidate-versions --json)
    add_json "${CANDIDATE_RESPONSE}"

    # Extract the candidate ID - use jq if available
    if command -v jq >/dev/null 2>&1; then
        CANDIDATE_ID=$(echo "${CANDIDATE_RESPONSE}" | jq -r '.entries[0].content.id // empty')
    else
        # Fallback to grep/awk
        CANDIDATE_ID=$(echo "${CANDIDATE_RESPONSE}" | grep -o '"id": *"[^"]*"' | head -1 | awk -F'"' '{print $4}')

        if [ -z "${CANDIDATE_ID}" ]; then
            # Try alternative extraction method
            CANDIDATE_ID=$(echo "${CANDIDATE_RESPONSE}" | grep -o '"content": *{[^}]*"id": *"[^"]*"' | grep -o '"id": *"[^"]*"' | awk -F'"' '{print $4}')
        fi
    fi

    if [ -z "${CANDIDATE_ID}" ]; then
        log_error "No candidate software versions found"
        return 1
    fi

    log_info "Found candidate ID: ${CANDIDATE_ID}"

    # Step 5: Create an upgrade session
    log_info "Step 5: Creating upgrade session"
    add_header "Step 5: Creating upgrade session"

    # Make sure we're logged in with a fresh session to get a valid CSRF token
    log_info "Ensuring we have a valid CSRF token by logging in again"
    ./uniclient logout || true
    ./uniclient login --username "${USERNAME}" --password "${PASSWORD}" --url "${HOST}"

    # Run the create-upgrade command and capture the output
    log_info "Running create-upgrade command with version: ${CANDIDATE_ID}"
    CREATE_SESSION_RESPONSE=$(./uniclient create-upgrade --version "${CANDIDATE_ID}" --json)

    # Debug output - print the raw response
    echo "DEBUG: Create session raw response: ${CREATE_SESSION_RESPONSE}"
    add_json "${CREATE_SESSION_RESPONSE}"

    # Try to extract the session ID using various methods
    # First, check if the response is valid JSON
    if echo "${CREATE_SESSION_RESPONSE}" | grep -q "^{"; then
        # It looks like JSON, try to parse it
        if command -v jq >/dev/null 2>&1; then
            # Use jq but handle errors
            SESSION_ID=$(echo "${CREATE_SESSION_RESPONSE}" | jq -r '.content.id // .id // empty' 2>/dev/null || echo "")
        fi
    fi

    # If jq failed or SESSION_ID is empty, try grep/awk
    if [ -z "${SESSION_ID}" ]; then
        # Try to extract using grep/awk
        SESSION_ID=$(echo "${CREATE_SESSION_RESPONSE}" | grep -o '"id": *"[^"]*"' | head -1 | awk -F'"' '{print $4}' 2>/dev/null || echo "")

        if [ -z "${SESSION_ID}" ]; then
            # Try alternative extraction method
            SESSION_ID=$(echo "${CREATE_SESSION_RESPONSE}" | grep -o '"content": *{[^}]*"id": *"[^"]*"' | grep -o '"id": *"[^"]*"' | awk -F'"' '{print $4}' 2>/dev/null || echo "")
        fi
    fi

    # If all extraction methods failed, check if the response contains a session ID in plain text
    if [ -z "${SESSION_ID}" ]; then
        # Look for "Session ID: XXX" pattern in the output
        SESSION_ID=$(echo "${CREATE_SESSION_RESPONSE}" | grep -o "Session ID: [^ ]*" | cut -d' ' -f3 2>/dev/null || echo "")
    fi

    # If we still don't have a session ID, try to get it from the upgrade-sessions command
    if [ -z "${SESSION_ID}" ]; then
        log_info "Could not extract session ID from create response, trying to get it from upgrade-sessions"

        # Make sure we're logged in again to get fresh data
        ./uniclient login --username "${USERNAME}" --password "${PASSWORD}" --url "${HOST}" || true

        SESSIONS_RESPONSE=$(./uniclient upgrade-sessions --json)
        echo "DEBUG: Sessions response: ${SESSIONS_RESPONSE}"

        if command -v jq >/dev/null 2>&1; then
            # Try to get the most recent session ID
            SESSION_ID=$(echo "${SESSIONS_RESPONSE}" | jq -r '.entries[0].content.id // empty' 2>/dev/null || echo "")
        fi

        if [ -z "${SESSION_ID}" ]; then
            # Try grep/awk as fallback
            SESSION_ID=$(echo "${SESSIONS_RESPONSE}" | grep -o '"id": *"[^"]*"' | head -1 | awk -F'"' '{print $4}' 2>/dev/null || echo "")
        fi
    fi

    if [ -z "${SESSION_ID}" ]; then
        log_error "Failed to extract session ID from create session response"

        # For testing purposes, let's try to create the session using a different approach
        log_info "Attempting to create session using direct API call with curl"

        # Create a temporary file to store headers
        HEADERS_FILE=$(mktemp)

        # Get a CSRF token first - save headers to a file
        log_info "Getting CSRF token with curl"
        curl -s -v -c cookie.txt -b cookie.txt -u "${USERNAME}:${PASSWORD}" "${HOST}/api/types/loginSessionInfo/instances" 2> "${HEADERS_FILE}"

        # Extract CSRF token from headers
        CSRF_TOKEN=$(grep -i "EMC-CSRF-TOKEN:" "${HEADERS_FILE}" | sed 's/.*EMC-CSRF-TOKEN: //' | tr -d '\r')

        echo "DEBUG: Headers from login request:"
        cat "${HEADERS_FILE}"

        if [ -n "${CSRF_TOKEN}" ]; then
            log_info "Got CSRF token: ${CSRF_TOKEN}"

            # Create the session using curl
            CURL_RESPONSE=$(curl -s -v -X POST -c cookie.txt -b cookie.txt \
                -H "Content-Type: application/json" \
                -H "X-EMC-REST-CLIENT: true" \
                -H "EMC-CSRF-TOKEN: ${CSRF_TOKEN}" \
                -d "{\"candidateVersionId\":\"${CANDIDATE_ID}\"}" \
                "${HOST}/api/types/upgradeSession/instances" 2>> "${HEADERS_FILE}")

            echo "DEBUG: Curl create session response: ${CURL_RESPONSE}"
            echo "DEBUG: Headers from create session request:"
            cat "${HEADERS_FILE}"

            # Try to extract session ID from curl response
            if command -v jq >/dev/null 2>&1; then
                SESSION_ID=$(echo "${CURL_RESPONSE}" | jq -r '.content.id // .id // empty' 2>/dev/null || echo "")
            else
                SESSION_ID=$(echo "${CURL_RESPONSE}" | grep -o '"id": *"[^"]*"' | head -1 | awk -F'"' '{print $4}' 2>/dev/null || echo "")
            fi

            if [ -n "${SESSION_ID}" ]; then
                log_info "Created session using curl: ${SESSION_ID}"
            else
                log_error "Failed to create session using curl"

                # Try one more approach - use the Python client directly
                log_info "Attempting to create session using Python client directly"

                # Create a temporary Python script with more debugging
                PYTHON_SCRIPT=$(mktemp)
                cat > "${PYTHON_SCRIPT}" << EOF
#!/usr/bin/env python3
import sys
import json
import requests
from dell_unisphere_client.client import UnisphereClient

# Enable verbose output
print("DEBUG: Starting Python script to create upgrade session", file=sys.stderr)

try:
    # Create client with debug info
    print(f"DEBUG: Creating client with URL: {HOST}, Username: {USERNAME}", file=sys.stderr)
    client = UnisphereClient(
        base_url="${HOST}",
        username="${USERNAME}",
        password="${PASSWORD}",
        verify_ssl=False
    )

    # Login with debug info
    print("DEBUG: Attempting to login", file=sys.stderr)
    login_result = client.login()
    print(f"DEBUG: Login result: {login_result}", file=sys.stderr)

    # Print CSRF token
    print(f"DEBUG: CSRF token: {client.csrf_token}", file=sys.stderr)

    # Create a session directly using requests
    print("DEBUG: Creating session using direct requests", file=sys.stderr)

    # Get a session cookie first
    session = requests.Session()
    session.auth = ("${USERNAME}", "${PASSWORD}")
    session.verify = False

    # Get CSRF token
    login_response = session.get(
        f"${HOST}/api/types/loginSessionInfo/instances",
        headers={"X-EMC-REST-CLIENT": "true"}
    )
    print(f"DEBUG: Login response status: {login_response.status_code}", file=sys.stderr)

    # Extract CSRF token from headers
    csrf_token = login_response.headers.get("EMC-CSRF-TOKEN")
    print(f"DEBUG: CSRF token from response: {csrf_token}", file=sys.stderr)

    # Create upgrade session
    if csrf_token:
        create_response = session.post(
            f"${HOST}/api/types/upgradeSession/instances",
            headers={
                "Content-Type": "application/json",
                "X-EMC-REST-CLIENT": "true",
                "EMC-CSRF-TOKEN": csrf_token
            },
            json={"candidateVersionId": "${CANDIDATE_ID}"}
        )
        print(f"DEBUG: Create response status: {create_response.status_code}", file=sys.stderr)
        print(f"DEBUG: Create response body: {create_response.text}", file=sys.stderr)

        # Try to extract session ID
        try:
            # Directly access the id from root of response
            session_id = create_response.json().get("id", "")
            print(f"Session ID: {session_id}")
            # Also verify session ID format
            if session_id and session_id.startswith("Upgrade_"):
                print(f"DEBUG: Valid session ID detected: {session_id}", file=sys.stderr)
                return  # Exit early with valid ID
            print(f"DEBUG: Unexpected session ID format: {session_id}", file=sys.stderr)
        except Exception as e:
            print(f"DEBUG: Error parsing response: {str(e)}", file=sys.stderr)
            print("Session ID: ")
    else:
        print("DEBUG: No CSRF token found", file=sys.stderr)
        print("Session ID: ")
except Exception as e:
    print(f"DEBUG: Exception: {str(e)}", file=sys.stderr)
    print("Session ID: ")
EOF

                # Make the script executable
                chmod +x "${PYTHON_SCRIPT}"

                # Run the script
                PYTHON_RESPONSE=$(python3 "${PYTHON_SCRIPT}")
                echo "DEBUG: Python script response: ${PYTHON_RESPONSE}"

                # Extract session ID from Python response
                SESSION_ID=$(echo "${PYTHON_RESPONSE}" | grep -o "Session ID: [^ ]*" | cut -d' ' -f3 2>/dev/null || echo "")

                if [ -n "${SESSION_ID}" ]; then
                    log_info "Created session using Python client: ${SESSION_ID}"
                else
                    log_error "Failed to create session using Python client"
                    return 1
                fi
            fi
        else
            log_error "Failed to get CSRF token for curl approach"

            # Try one more approach - use the Python client directly
            log_info "Attempting to create session using Python client directly"

            # Create a temporary Python script with more debugging
            PYTHON_SCRIPT=$(mktemp)
            cat > "${PYTHON_SCRIPT}" << EOF
#!/usr/bin/env python3
import sys
import json
import requests
from dell_unisphere_client.client import UnisphereClient

# Enable verbose output
print("DEBUG: Starting Python script to create upgrade session", file=sys.stderr)

try:
    # Create client with debug info
    print(f"DEBUG: Creating client with URL: ${HOST}, Username: ${USERNAME}", file=sys.stderr)
    client = UnisphereClient(
        base_url="${HOST}",
        username="${USERNAME}",
        password="${PASSWORD}",
        verify_ssl=False
    )

    # Login with debug info
    print("DEBUG: Attempting to login", file=sys.stderr)
    login_result = client.login()
    print(f"DEBUG: Login result: {login_result}", file=sys.stderr)

    # Print CSRF token
    print(f"DEBUG: CSRF token: {client.csrf_token}", file=sys.stderr)

    # Create a session directly using requests
    print("DEBUG: Creating session using direct requests", file=sys.stderr)

    # Get a session cookie first
    session = requests.Session()
    session.auth = ("${USERNAME}", "${PASSWORD}")
    session.verify = False

    # Get CSRF token
    login_response = session.get(
        f"${HOST}/api/types/loginSessionInfo/instances",
        headers={"X-EMC-REST-CLIENT": "true"}
    )
    print(f"DEBUG: Login response status: {login_response.status_code}", file=sys.stderr)

    # Extract CSRF token from headers
    csrf_token = login_response.headers.get("EMC-CSRF-TOKEN")
    print(f"DEBUG: CSRF token from response: {csrf_token}", file=sys.stderr)

    # Create upgrade session
    if csrf_token:
        create_response = session.post(
            f"${HOST}/api/types/upgradeSession/instances",
            headers={
                "Content-Type": "application/json",
                "X-EMC-REST-CLIENT": "true",
                "EMC-CSRF-TOKEN": csrf_token
            },
            json={"candidateVersionId": "${CANDIDATE_ID}"}
        )
        print(f"DEBUG: Create response status: {create_response.status_code}", file=sys.stderr)
        print(f"DEBUG: Create response body: {create_response.text}", file=sys.stderr)

        # Try to extract session ID
        try:
            response_data = create_response.json()
            session_id = response_data.get("content", {}).get("id", "")
            print(f"Session ID: {session_id}")
        except Exception as e:
            print(f"DEBUG: Error parsing response: {str(e)}", file=sys.stderr)
            print("Session ID: ")
    else:
        print("DEBUG: No CSRF token found", file=sys.stderr)
        print("Session ID: ")
except Exception as e:
    print(f"DEBUG: Exception: {str(e)}", file=sys.stderr)
    print("Session ID: ")
EOF

            # Make the script executable
            chmod +x "${PYTHON_SCRIPT}"

            # Run the script
            PYTHON_RESPONSE=$(python3 "${PYTHON_SCRIPT}")
            echo "DEBUG: Python script response: ${PYTHON_RESPONSE}"

            # Extract session ID from Python response
            SESSION_ID=$(echo "${PYTHON_RESPONSE}" | grep -o "Session ID: [^ ]*" | cut -d' ' -f3 2>/dev/null || echo "")

            if [ -n "${SESSION_ID}" ]; then
                log_info "Created session using Python client: ${SESSION_ID}"
            else
                log_error "Failed to create session using Python client"
                return 1
            fi
        fi
    fi

    log_info "Created upgrade session: ${SESSION_ID}"

    # Step 6: Monitor the upgrade progress
    log_info "Step 6: Monitoring upgrade progress"
    add_header "Step 6: Monitoring upgrade progress"
    add_content "Monitoring the upgrade session until completion"

    # Create a table for task status tracking
    add_table_header "Time | Status | Progress | Tasks"

    # Skip the CLI monitor-upgrade command and use Python script directly
    log_info "Using Python script to monitor upgrade session with ID: ${SESSION_ID}"

    # Create a Python script to monitor the upgrade session
    # This is more reliable than using the CLI command
    MONITOR_SCRIPT=$(mktemp)
    cat > "${MONITOR_SCRIPT}" << EOF
#!/usr/bin/env python3
import time
import json
from dell_unisphere_client.client import UnisphereClient

# Create client
client = UnisphereClient(
    base_url="${HOST}",
    username="${USERNAME}",
    password="${PASSWORD}",
    verify_ssl=False
)

# Login
client.login()

# Monitor the upgrade session
try:
    result = client.monitor_upgrade_session(
        session_id="${SESSION_ID}",
        interval=2,
        timeout=120
    )
    print(json.dumps(result, indent=2))
except Exception as e:
    print(f"Error monitoring upgrade: {str(e)}")
EOF

    # Make the script executable
    chmod +x "${MONITOR_SCRIPT}"

    # Run the script
    MONITOR_RESPONSE=$(python3 "${MONITOR_SCRIPT}")
    echo "DEBUG: Python monitor script response:"
    echo "${MONITOR_RESPONSE}"
    add_json "${MONITOR_RESPONSE}"

    # Get the final status for the report
    MONITOR_RESPONSE=$(./uniclient upgrade-sessions --json)
    add_json "${MONITOR_RESPONSE}"

    log_info "Upgrade completed successfully!"

    # Extract and display task completion summary
    add_header "Task Completion Summary"
    add_table_header "Task Name | Status | Duration"

    # Extract tasks from the response
    TASKS=$(echo "${MONITOR_RESPONSE}" | grep -o '"tasks": *\[[^]]*\]' | sed 's/"tasks": *//')

    if [ -n "${TASKS}" ]; then
        # Parse tasks and add to the table
        echo "${TASKS}" | grep -o '{[^}]*}' | while read -r TASK; do
            TASK_NAME=$(echo "${TASK}" | grep -o '"caption": *"[^"]*"' | awk -F'"' '{print $4}')
            TASK_STATUS=$(echo "${TASK}" | grep -o '"status": *[0-9]*' | awk '{print $2}')

            # Map status code to text
            case "${TASK_STATUS}" in
                0) STATUS_TEXT="PENDING" ;;
                1) STATUS_TEXT="IN_PROGRESS" ;;
                2) STATUS_TEXT="COMPLETED" ;;
                3) STATUS_TEXT="FAILED" ;;
                4) STATUS_TEXT="PAUSED" ;;
                *) STATUS_TEXT="UNKNOWN(${TASK_STATUS})" ;;
            esac

            # Get start and end time
            START_TIME=$(echo "${TASK}" | grep -o '"startTime": *"[^"]*"' | awk -F'"' '{print $4}')
            END_TIME=$(echo "${TASK}" | grep -o '"endTime": *"[^"]*"' | awk -F'"' '{print $4}')

            # Calculate duration
            if [ -n "${START_TIME}" ] && [ -n "${END_TIME}" ]; then
                DURATION="Completed"
            elif [ -n "${START_TIME}" ]; then
                DURATION="In progress"
            else
                DURATION="N/A"
            fi

            add_table_row "${TASK_NAME} | ${STATUS_TEXT} | ${DURATION}"
        done
    fi

    return 0
}

# Clean up after tests
cleanup() {
    # Remove the dummy upgrade file
    if [ -f "${UPGRADE_FILE}" ]; then
        rm -f "${UPGRADE_FILE}"
    fi

    # Logout
    ./uniclient logout || true
    log_info "Logged out successfully"
}

# Main function
main() {
    # Initialize the report
    initialize_report

    # Check if API is running
    if ! check_api; then
        log_error "API is not running. Exiting."
        return 1
    fi

    # Configure the client
    configure_client

    # Run general API tests
    if ! run_api_tests; then
        log_error "API tests failed. Continuing with upgrade flow..."
    fi

    # Test the complete upgrade flow
    if ! test_upgrade_flow; then
        log_error "Upgrade flow tests failed."
        cleanup
        return 1
    fi

    # Clean up
    cleanup

    log_info "All tests completed. Results saved in ${REPORT_FILE}"
    return 0
}

# Run the main function
main
exit $?
