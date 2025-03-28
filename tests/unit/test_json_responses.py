"""Unit tests for JSON responses of all Dell Unisphere Client endpoints."""

from unittest.mock import patch, MagicMock

from dell_unisphere_client import UnisphereClient
from dell_unisphere_client.api import SystemApi, SoftwareApi, UpgradeApi


class TestJsonResponses:
    """Test suite for checking JSON responses of all endpoints."""

    def test_get_basic_system_info_json(self, mock_requests, mock_response):
        """Test get_basic_system_info method returns expected JSON structure."""
        # Setup
        client = UnisphereClient(
            base_url="https://example.com", username="testuser", password="testpass"
        )
        client.csrf_token = "test-token"
        client.session = MagicMock()

        # Initialize API clients
        client.system_api = SystemApi(
            base_url="https://example.com",
            session=client.session,
            csrf_token=client.csrf_token,
            verify_ssl=True,
            timeout=60,
            verbose=False,
        )

        # Create expected JSON response
        expected_response = {
            "content": {
                "id": "system_1",
                "name": "Unity100-1",
                "model": "Unity 100",
                "serialNumber": "UNITY-123456789",
                "health": {
                    "value": 5,
                    "descriptionIds": ["ALRT_COMPONENT_OK"],
                    "descriptions": ["The component is operating normally."],
                },
            }
        }
        response = mock_response(json_data=expected_response, status_code=200)

        # Configure mock requests to return our response
        mock_requests.get.return_value = response

        # Patch the _ensure_logged_in method to avoid actual login
        with patch.object(client, "_ensure_logged_in"):
            # Mock the system_api.get_basic_system_info to return our expected_response
            with patch.object(
                client.system_api,
                "get_basic_system_info",
                return_value=expected_response,
            ):
                # Call the method
                result = client.get_basic_system_info()

        # Assertions
        assert result == expected_response
        assert "content" in result
        assert "id" in result["content"]
        assert "name" in result["content"]
        assert "model" in result["content"]
        assert "serialNumber" in result["content"]
        assert "health" in result["content"]

    def test_get_installed_software_version_json(
        self, mock_requests, mock_response, sample_software_version
    ):
        """Test get_installed_software_version method returns expected JSON structure."""
        # Setup
        client = UnisphereClient(
            base_url="https://example.com", username="testuser", password="testpass"
        )
        client.csrf_token = "test-token"
        client.session = MagicMock()

        # Initialize API clients
        client.software_api = SoftwareApi(
            base_url="https://example.com",
            session=client.session,
            csrf_token=client.csrf_token,
            verify_ssl=True,
            timeout=60,
            verbose=False,
        )

        # Create mock response
        response = mock_response(json_data=sample_software_version, status_code=200)

        # Configure mock requests to return our response
        mock_requests.get.return_value = response

        # Patch the _ensure_logged_in method to avoid actual login
        with patch.object(client, "_ensure_logged_in"):
            # Call the method
            result = client.get_installed_software_version()

        # Assertions
        assert result == sample_software_version
        assert "@base" in result
        assert "updated" in result
        assert "links" in result
        assert "content" in result
        assert "version" in result["content"]
        assert "releaseDate" in result["content"]
        assert "installationDate" in result["content"]
        assert "packages" in result["content"]

    def test_get_candidate_software_versions_json(
        self, mock_requests, mock_response, sample_candidate_versions
    ):
        """Test get_candidate_software_versions method returns expected JSON structure."""
        # Setup
        client = UnisphereClient(
            base_url="https://example.com", username="testuser", password="testpass"
        )
        client.csrf_token = "test-token"
        client.session = MagicMock()

        # Initialize API clients
        client.software_api = SoftwareApi(
            base_url="https://example.com",
            session=client.session,
            csrf_token=client.csrf_token,
            verify_ssl=True,
            timeout=60,
            verbose=False,
        )

        # Create mock response
        response = mock_response(json_data=sample_candidate_versions, status_code=200)

        # Configure mock requests to return our response
        mock_requests.get.return_value = response

        # Patch the _ensure_logged_in method to avoid actual login
        with patch.object(client, "_ensure_logged_in"):
            # Call the method
            result = client.get_candidate_software_versions()

        # Assertions
        assert result == sample_candidate_versions
        assert "@base" in result
        assert "updated" in result
        assert "links" in result
        assert "entries" in result
        assert len(result["entries"]) > 0
        assert "content" in result["entries"][0]
        assert "id" in result["entries"][0]["content"]
        assert "version" in result["entries"][0]["content"]
        assert "releaseDate" in result["entries"][0]["content"]
        assert "isValid" in result["entries"][0]["content"]

    def test_get_software_upgrade_sessions_json(
        self, mock_requests, mock_response, sample_upgrade_sessions
    ):
        """Test get_software_upgrade_sessions method returns expected JSON structure."""
        # Setup
        client = UnisphereClient(
            base_url="https://example.com", username="testuser", password="testpass"
        )
        client.csrf_token = "test-token"
        client.session = MagicMock()

        # Initialize API clients
        client.upgrade_api = UpgradeApi(
            base_url="https://example.com",
            session=client.session,
            csrf_token=client.csrf_token,
            verify_ssl=True,
            timeout=60,
            verbose=False,
        )

        # Create mock response
        response = mock_response(json_data=sample_upgrade_sessions, status_code=200)

        # Configure mock requests to return our response
        mock_requests.get.return_value = response

        # Patch the _ensure_logged_in method to avoid actual login
        with patch.object(client, "_ensure_logged_in"):
            # Call the method
            result = client.get_software_upgrade_sessions()

        # Assertions
        assert result == sample_upgrade_sessions
        assert "@base" in result
        assert "updated" in result
        assert "links" in result
        assert "entries" in result
        assert len(result["entries"]) > 0
        assert "content" in result["entries"][0]
        assert "id" in result["entries"][0]["content"]
        assert "candidateVersion" in result["entries"][0]["content"]
        assert "status" in result["entries"][0]["content"]
        assert "percentComplete" in result["entries"][0]["content"]

    def test_verify_upgrade_eligibility_json(self, mock_requests, mock_response):
        """Test verify_upgrade_eligibility method returns expected JSON structure with raw_json=True."""
        # Setup
        client = UnisphereClient(
            base_url="https://example.com", username="testuser", password="testpass"
        )
        client.csrf_token = "test-token"
        client.session = MagicMock()

        # Initialize API clients
        client.upgrade_api = UpgradeApi(
            base_url="https://example.com",
            session=client.session,
            csrf_token=client.csrf_token,
            verify_ssl=True,
            timeout=60,
            verbose=False,
        )

        # Create mock response
        response_data = {
            "updated": "2025-03-25T14:28:18.980Z",
            "content": {"statusMessage": "", "overallStatus": False},
        }
        response = mock_response(json_data=response_data, status_code=200)

        # Configure mock requests to return our response
        mock_requests.post.return_value = response

        # Patch the _ensure_logged_in method to avoid actual login
        with patch.object(client, "_ensure_logged_in"):
            # Mock the upgrade_api.verify_upgrade_eligibility to return our response_data
            with patch.object(
                client.upgrade_api,
                "verify_upgrade_eligibility",
                return_value=response_data,
            ):
                # Call the method with raw_json=True
                result = client.verify_upgrade_eligibility(
                    "5.4.0.0.5.150", raw_json=True
                )

        # Assertions
        assert result == response_data
        assert "updated" in result
        assert "content" in result
        assert "statusMessage" in result["content"]
        assert "overallStatus" in result["content"]

    def test_create_upgrade_session_json(self, mock_requests, mock_response):
        """Test create_upgrade_session method returns expected JSON structure."""
        # Setup
        client = UnisphereClient(
            base_url="https://example.com", username="testuser", password="testpass"
        )
        client.csrf_token = "test-token"
        client.session = MagicMock()

        # Initialize API clients
        client.upgrade_api = UpgradeApi(
            base_url="https://example.com",
            session=client.session,
            csrf_token=client.csrf_token,
            verify_ssl=True,
            timeout=60,
            verbose=False,
        )

        # Create mock response
        response_data = {
            "content": {
                "id": "123",
                "status": "Scheduled",
                "candidateVersion": "5.4.0.0.5.150",
                "percentComplete": 0,
                "creationTime": "2025-03-25T14:30:00.000Z",
            }
        }
        response = mock_response(json_data=response_data, status_code=200)

        # Configure mock requests to return our response
        mock_requests.post.return_value = response

        # Patch the _ensure_logged_in method to avoid actual login
        with patch.object(client, "_ensure_logged_in"):
            # Mock the upgrade_api.create_upgrade_session to return our response_data
            with patch.object(
                client.upgrade_api, "create_upgrade_session", return_value=response_data
            ):
                # Call the method
                result = client.create_upgrade_session("5.4.0.0.5.150")

        # Assertions
        assert result == response_data
        assert "content" in result
        assert "id" in result["content"]
        assert "status" in result["content"]
        assert "candidateVersion" in result["content"]
        assert "percentComplete" in result["content"]

    def test_resume_upgrade_session_json(self, mock_requests, mock_response):
        """Test resume_upgrade_session method returns expected JSON structure."""
        # Setup
        client = UnisphereClient(
            base_url="https://example.com", username="testuser", password="testpass"
        )
        client.csrf_token = "test-token"
        client.session = MagicMock()

        # Initialize API clients
        client.upgrade_api = UpgradeApi(
            base_url="https://example.com",
            session=client.session,
            csrf_token=client.csrf_token,
            verify_ssl=True,
            timeout=60,
            verbose=False,
        )

        # Create mock response
        response_data = {
            "content": {
                "id": "123",
                "status": "InProgress",
                "candidateVersion": "5.4.0.0.5.150",
                "percentComplete": 5,
                "lastModificationTime": "2025-03-25T14:35:00.000Z",
            }
        }
        response = mock_response(json_data=response_data, status_code=200)

        # Configure mock requests to return our response
        mock_requests.post.return_value = response

        # Patch the _ensure_logged_in method to avoid actual login
        with patch.object(client, "_ensure_logged_in"):
            # Mock the upgrade_api.resume_upgrade_session to return our response_data
            with patch.object(
                client.upgrade_api, "resume_upgrade_session", return_value=response_data
            ):
                # Call the method
                result = client.resume_upgrade_session("123")

        # Assertions
        assert result == response_data
        assert "content" in result
        assert "id" in result["content"]
        assert "status" in result["content"]
        assert "candidateVersion" in result["content"]
        assert "percentComplete" in result["content"]

    def test_monitor_upgrade_sessions_json(self, mock_requests, mock_response):
        """Test monitor_upgrade_sessions method returns expected JSON structure with raw_json=True."""
        # Setup
        client = UnisphereClient(
            base_url="https://example.com", username="testuser", password="testpass"
        )
        client.csrf_token = "test-token"
        client.session = MagicMock()

        # Initialize API clients
        client.upgrade_api = UpgradeApi(
            base_url="https://example.com",
            session=client.session,
            csrf_token=client.csrf_token,
            verify_ssl=True,
            timeout=60,
            verbose=False,
        )

        # Create mock response with the fields specified in the curl example
        response_data = {
            "entries": [
                {
                    "content": {
                        "id": "123",
                        "status": "InProgress",
                        "caption": "Upgrade to 5.4.0.0.5.150",
                        "percentComplete": 45,
                        "type": "Software Upgrade",
                        "elapsedTime": "01:15:30",
                        "tasks": [
                            {
                                "name": "Prepare",
                                "status": "Completed",
                                "estimatedTime": "00:10:00",
                            },
                            {
                                "name": "Install",
                                "status": "InProgress",
                                "estimatedTime": "00:45:00",
                            },
                            {
                                "name": "Finalize",
                                "status": "Pending",
                                "estimatedTime": "00:30:00",
                            },
                        ],
                    }
                }
            ]
        }
        response = mock_response(json_data=response_data, status_code=200)

        # Configure mock requests to return our response
        mock_requests.get.return_value = response

        # Patch the _ensure_logged_in method to avoid actual login
        with patch.object(client, "_ensure_logged_in"):
            # Mock the upgrade_api.get_software_upgrade_sessions to return our response_data
            with patch.object(
                client.upgrade_api,
                "get_software_upgrade_sessions",
                return_value=response_data,
            ):
                # Call the method with raw_json=True
                result = client.monitor_upgrade_sessions(raw_json=True)

        # Assertions
        assert result == response_data
        assert "entries" in result
        assert len(result["entries"]) > 0
        assert "content" in result["entries"][0]
        assert "id" in result["entries"][0]["content"]
        assert "status" in result["entries"][0]["content"]
        assert "caption" in result["entries"][0]["content"]
        assert "percentComplete" in result["entries"][0]["content"]
        assert "type" in result["entries"][0]["content"]
        assert "elapsedTime" in result["entries"][0]["content"]
        assert "tasks" in result["entries"][0]["content"]

        # Check tasks structure
        tasks = result["entries"][0]["content"]["tasks"]
        assert len(tasks) > 0
        assert "name" in tasks[0]
        assert "status" in tasks[0]

    def test_upload_package_json(self, mock_requests, mock_response):
        """Test upload_package method returns expected JSON structure."""
        # Setup
        client = UnisphereClient(
            base_url="https://example.com", username="testuser", password="testpass"
        )
        client.csrf_token = "test-token"
        client.session = MagicMock()

        # Initialize API clients
        client.software_api = SoftwareApi(
            base_url="https://example.com",
            session=client.session,
            csrf_token=client.csrf_token,
            verify_ssl=True,
            timeout=60,
            verbose=False,
        )

        # Create mock response
        response_data = {
            "content": {
                "id": "file_123",
                "name": "unity-5.4.0.0.5.150.bin",
                "size": 1024000000,
                "uploadTime": "2025-03-25T15:00:00.000Z",
            }
        }
        response = mock_response(json_data=response_data, status_code=200)

        # Configure mock requests to return our response
        mock_requests.post.return_value = response

        # Mock open file
        mock_file = MagicMock()
        mock_open = MagicMock(return_value=mock_file)

        # Patch the _ensure_logged_in method to avoid actual login
        with patch.object(client, "_ensure_logged_in"):
            # Mock the software_api.upload_package to return our response_data
            with patch.object(
                client.software_api, "upload_package", return_value=response_data
            ):
                # Call the method
                with patch("builtins.open", mock_open):
                    result = client.upload_package("/path/to/package.bin")

        # Assertions
        assert result == response_data
        assert "content" in result
        assert "id" in result["content"]
        assert "name" in result["content"]
        assert "size" in result["content"]
        assert "uploadTime" in result["content"]
