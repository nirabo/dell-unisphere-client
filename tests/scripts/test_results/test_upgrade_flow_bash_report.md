# Dell Unisphere Client - Comprehensive Test Report (Bash)
Generated on: 2025-03-23 16:53:29


## Checking if API is running
API is running at http://localhost:8000

## Configuring the client
Client configured with URL: http://localhost:8000, Username: admin

## Running General API Tests

## Login
Login successful

## Getting Basic System Info
```json
{
  "@base": "http://localhost:8000/api/types/basicSystemInfo/instances?per_page=2000",
  "updated": "2025-03-23T16:53:29.807Z",
  "links": [
    {
      "rel": "self",
      "href": "&page=1"
    }
  ],
  "entries": [
    {
      "@base": "http://localhost:8000/api/instances/basicSystemInfo",
      "content": {
        "id": "0",
        "model": "Unity 380F",
        "name": "CKM01204905476",
        "softwareVersion": "5.3.0",
        "softwareFullVersion": "Unity 5.3.0.0 (Release, Build 120, 2023-03-18 19:02:01, 5.3.0.0.5.120)",
        "apiVersion": "13.0",
        "earliestApiVersion": "4.0"
      },
      "links": [
        {
          "rel": "self",
          "href": "/0"
        }
      ],
      "updated": "2025-03-23T16:53:29.807Z"
    }
  ]
}
```
Basic system info retrieved successfully

## Getting Installed Software Version
```json
{
  "@base": "http://localhost:8000/api/types/installedSoftwareVersion/instances?per_page=2000",
  "updated": "2025-03-23T16:53:30.127Z",
  "links": [
    {
      "rel": "self",
      "href": "&page=1"
    }
  ],
  "entries": [
    {
      "@base": "http://localhost:8000/api/instances/installedSoftwareVersion",
      "content": {
        "id": "0",
        "version": "5.3.0",
        "revision": 120,
        "releaseDate": "2025-03-23T14:02:13.423081",
        "fullVersion": "Unity 5.3.0.0 (Release, Build 120, 2023-03-18 19:02:01, 5.3.0.0.5.120)",
        "languages": [
          {
            "name": "English",
            "version": "5.3.0"
          },
          {
            "name": "Chinese",
            "version": "5.3.0"
          }
        ],
        "hotFixes": [
          "HF1",
          "HF2"
        ],
        "packageVersions": [
          {
            "name": "Base",
            "version": "5.3.0"
          },
          {
            "name": "Management",
            "version": "5.3.0"
          }
        ],
        "driveFirmware": [
          {
            "name": "Drive Firmware Package 1",
            "version": "1.2.3",
            "releaseDate": "2025-03-23T14:02:13.423093",
            "upgradedeDriveCount": 24,
            "estimatedTime": 30,
            "isNewVersion": false
          }
        ]
      },
      "links": [
        {
          "rel": "self",
          "href": "/0"
        }
      ],
      "updated": "2025-03-23T16:53:30.127Z"
    }
  ]
}
```
Installed software version retrieved successfully

## Getting Candidate Software Versions
```json
{
  "@base": "http://localhost:8000/api/types/candidateSoftwareVersion/instances?per_page=2000",
  "updated": "2025-03-23T16:53:30.383Z",
  "links": [
    {
      "rel": "self",
      "href": "&page=1"
    }
  ],
  "entries": [
    {
      "@base": "http://localhost:8000/api/instances/candidateSoftwareVersion",
      "content": {
        "id": "candidate_8d65c7a0-fb65-4432-9653-8bca2baf3b4d",
        "version": "5.4.0",
        "fullVersion": "Unity 5.4.0.0 (Release, Build 150, 2023-06-18 19:02:01, 5.4.0.0.5.150)",
        "revision": 150,
        "releaseDate": "2025-03-23T14:49:28.331772",
        "type": "SOFTWARE",
        "rebootRequired": true,
        "canPauseBeforeReboot": true
      },
      "links": [
        {
          "rel": "self",
          "href": "/candidate_8d65c7a0-fb65-4432-9653-8bca2baf3b4d"
        }
      ],
      "updated": "2025-03-23T16:53:30.383Z"
    }
  ]
}
```
Candidate software versions retrieved successfully

## Getting Software Upgrade Sessions
```json
{
  "@base": "http://localhost:8000/api/types/upgradeSession/instances?per_page=2000",
  "updated": "2025-03-23T16:53:30.646Z",
  "links": [
    {
      "rel": "self",
      "href": "&page=1"
    }
  ],
  "entries": [
    {
      "@base": "http://localhost:8000/api/instances/upgradeSession",
      "content": {
        "id": "Upgrade_5.4.0.0",
        "type": 0,
        "candidate": "file_7701a4ca-b9ef-486f-9fca-ff143e79544b",
        "caption": "Upgrade to 5.4.0.0",
        "status": 2,
        "startTime": "2025-03-23T14:49:28.426072",
        "messages": [],
        "creationTime": "2025-03-23T14:49:28.426074",
        "elapsedTime": "PT0H0M46S",
        "percentComplete": 100,
        "tasks": [
          {
            "status": 2,
            "type": 0,
            "caption": "Preparing system",
            "creationTime": "2025-03-23T14:49:28.426004",
            "estRemainTime": "00:03:30.000"
          },
          {
            "status": 2,
            "type": 0,
            "caption": "Performing health checks",
            "creationTime": "2025-03-23T14:49:28.426004",
            "estRemainTime": "00:02:10.000"
          },
          {
            "status": 2,
            "type": 0,
            "caption": "Preparing system software",
            "creationTime": "2025-03-23T14:49:28.426004",
            "estRemainTime": "00:16:10.000"
          },
          {
            "status": 2,
            "type": 0,
            "caption": "Waiting for reboot command",
            "creationTime": "2025-03-23T14:49:28.426004",
            "estRemainTime": "00:00:05.000"
          },
          {
            "status": 2,
            "type": 0,
            "caption": "Performing health checks",
            "creationTime": "2025-03-23T14:49:28.426004",
            "estRemainTime": "00:01:05.000"
          },
          {
            "status": 2,
            "type": 2,
            "caption": "Installing new software on peer SP",
            "creationTime": "2025-03-23T14:49:28.426004",
            "estRemainTime": "00:16:50.000"
          },
          {
            "status": 2,
            "type": 3,
            "caption": "Rebooting peer SP",
            "creationTime": "2025-03-23T14:49:28.426004",
            "estRemainTime": "00:14:15.000"
          },
          {
            "status": 2,
            "type": 2,
            "caption": "Restarting services on peer SP",
            "creationTime": "2025-03-23T14:49:28.426004",
            "estRemainTime": "00:05:00.000"
          },
          {
            "status": 2,
            "type": 2,
            "caption": "Installing new software on primary SP",
            "creationTime": "2025-03-23T14:49:28.426004",
            "estRemainTime": "00:13:30.000"
          },
          {
            "status": 2,
            "type": 3,
            "caption": "Rebooting the primary SP",
            "creationTime": "2025-03-23T14:49:28.426004",
            "estRemainTime": "00:13:55.000"
          },
          {
            "status": 2,
            "type": 2,
            "caption": "Restarting services on primary SP",
            "creationTime": "2025-03-23T14:49:28.426004",
            "estRemainTime": "00:05:10.000"
          },
          {
            "status": 2,
            "type": 2,
            "caption": "Final tasks",
            "creationTime": "2025-03-23T14:49:28.426004",
            "estRemainTime": "00:00:45.000"
          }
        ],
        "endTime": "2025-03-23T14:50:14.781913"
      },
      "links": [
        {
          "rel": "self",
          "href": "/0"
        }
      ],
      "updated": "2025-03-23T16:53:30.646Z"
    }
  ]
}
```
Software upgrade sessions retrieved successfully

## Verifying Upgrade Eligibility
```json
{
  "eligible": true,
  "messages": [],
  "requiredPatches": [],
  "requiredHotfixes": []
}
```
Upgrade eligibility verified successfully

## Testing Complete Upgrade Flow
This test will create an upgrade session and monitor it until completion
Ensuring we're logged in
Step 1: Creating dummy upgrade file

## Step 1: Creating dummy upgrade file

## Creating dummy upgrade file
Created dummy upgrade file: ./tests/scripts/test_results/test_upgrade_client.bin (10M)
Step 2: Uploading software package

## Step 2: Uploading software package
```json
{
  "id": "file_4777df0b-d039-4e68-b081-ba8aea0a7d71",
  "filename": "./tests/scripts/test_results/test_upgrade_client.bin",
  "size": 10485760
}
```
Uploaded software package: file_4777df0b-d039-4e68-b081-ba8aea0a7d71
Step 3: Preparing software

## Step 3: Preparing software
```json
{
  "id": "candidate_9675ec9e-c3eb-4924-b366-e14559970c2f",
  "status": "SUCCESS"
}
```
Software prepared successfully
Step 4: Getting candidate software versions

## Step 4: Getting candidate software versions
```json
{
  "@base": "http://localhost:8000/api/types/candidateSoftwareVersion/instances?per_page=2000",
  "updated": "2025-03-23T16:53:32.156Z",
  "links": [
    {
      "rel": "self",
      "href": "&page=1"
    }
  ],
  "entries": [
    {
      "@base": "http://localhost:8000/api/instances/candidateSoftwareVersion",
      "content": {
        "id": "file_4777df0b-d039-4e68-b081-ba8aea0a7d71",
        "version": "5.4.0.0",
        "fullVersion": "Unity ./tests/scripts/test_results/test_upgrade_client.bin",
        "revision": 0,
        "releaseDate": "2025-03-23T16:53:31.543434",
        "type": "SOFTWARE",
        "rebootRequired": true,
        "canPauseBeforeReboot": true
      },
      "links": [
        {
          "rel": "self",
          "href": "/file_4777df0b-d039-4e68-b081-ba8aea0a7d71"
        }
      ],
      "updated": "2025-03-23T16:53:32.156Z"
    },
    {
      "@base": "http://localhost:8000/api/instances/candidateSoftwareVersion",
      "content": {
        "id": "candidate_9675ec9e-c3eb-4924-b366-e14559970c2f",
        "version": "5.4.0",
        "fullVersion": "Unity 5.4.0.0 (Release, Build 150, 2023-06-18 19:02:01, 5.4.0.0.5.150)",
        "revision": 150,
        "releaseDate": "2025-03-23T16:53:31.849949",
        "type": "SOFTWARE",
        "rebootRequired": true,
        "canPauseBeforeReboot": true
      },
      "links": [
        {
          "rel": "self",
          "href": "/candidate_9675ec9e-c3eb-4924-b366-e14559970c2f"
        }
      ],
      "updated": "2025-03-23T16:53:32.156Z"
    }
  ]
}
```
Found candidate ID: file_4777df0b-d039-4e68-b081-ba8aea0a7d71
Step 5: Creating upgrade session

## Step 5: Creating upgrade session
Ensuring we have a valid CSRF token by logging in again
Running create-upgrade command with version: file_4777df0b-d039-4e68-b081-ba8aea0a7d71
```json
{
  "id": "Upgrade_5.4.0.0",
  "content": {
    "id": "Upgrade_5.4.0.0",
    "type": 0,
    "candidate": "file_4777df0b-d039-4e68-b081-ba8aea0a7d71",
    "caption": "Upgrade to 5.4.0.0",
    "status": 1,
    "startTime": "2025-03-23T16:53:32.886859",
    "messages": [],
    "creationTime": "2025-03-23T16:53:32.886862",
    "elapsedTime": "PT0M",
    "percentComplete": 0,
    "tasks": [
      {
        "status": 1,
        "type": 0,
        "caption": "Preparing system",
        "creationTime": "2025-03-23T16:53:32.886754",
        "estRemainTime": "00:03:30.000"
      },
      {
        "status": 0,
        "type": 0,
        "caption": "Performing health checks",
        "creationTime": "2025-03-23T16:53:32.886754",
        "estRemainTime": "00:02:10.000"
      },
      {
        "status": 0,
        "type": 0,
        "caption": "Preparing system software",
        "creationTime": "2025-03-23T16:53:32.886754",
        "estRemainTime": "00:16:10.000"
      },
      {
        "status": 0,
        "type": 0,
        "caption": "Waiting for reboot command",
        "creationTime": "2025-03-23T16:53:32.886754",
        "estRemainTime": "00:00:05.000"
      },
      {
        "status": 0,
        "type": 0,
        "caption": "Performing health checks",
        "creationTime": "2025-03-23T16:53:32.886754",
        "estRemainTime": "00:01:05.000"
      },
      {
        "status": 0,
        "type": 2,
        "caption": "Installing new software on peer SP",
        "creationTime": "2025-03-23T16:53:32.886754",
        "estRemainTime": "00:16:50.000"
      },
      {
        "status": 0,
        "type": 3,
        "caption": "Rebooting peer SP",
        "creationTime": "2025-03-23T16:53:32.886754",
        "estRemainTime": "00:14:15.000"
      },
      {
        "status": 0,
        "type": 2,
        "caption": "Restarting services on peer SP",
        "creationTime": "2025-03-23T16:53:32.886754",
        "estRemainTime": "00:05:00.000"
      },
      {
        "status": 0,
        "type": 2,
        "caption": "Installing new software on primary SP",
        "creationTime": "2025-03-23T16:53:32.886754",
        "estRemainTime": "00:13:30.000"
      },
      {
        "status": 0,
        "type": 3,
        "caption": "Rebooting the primary SP",
        "creationTime": "2025-03-23T16:53:32.886754",
        "estRemainTime": "00:13:55.000"
      },
      {
        "status": 0,
        "type": 2,
        "caption": "Restarting services on primary SP",
        "creationTime": "2025-03-23T16:53:32.886754",
        "estRemainTime": "00:05:10.000"
      },
      {
        "status": 0,
        "type": 2,
        "caption": "Final tasks",
        "creationTime": "2025-03-23T16:53:32.886754",
        "estRemainTime": "00:00:45.000"
      }
    ]
  }
}
```
Created upgrade session: Upgrade_5.4.0.0
Step 6: Monitoring upgrade progress

## Step 6: Monitoring upgrade progress
Monitoring the upgrade session until completion
| Time | Status | Progress | Tasks |
| --- |
Using Python script to monitor upgrade session with ID: Upgrade_5.4.0.0
```json
[16:53:33] Starting upgrade monitoring...
[16:53:33] Status: IN_PROGRESS
[16:53:33] Progress: 0%
[16:53:33] Task: Preparing system - IN_PROGRESS
[16:53:33] Task: Performing health checks - PENDING
[16:53:33] Task: Preparing system software - PENDING
[16:53:33] Task: Waiting for reboot command - PENDING
[16:53:33] Task: Performing health checks - PENDING
[16:53:33] Task: Installing new software on peer SP - PENDING
[16:53:33] Task: Rebooting peer SP - PENDING
[16:53:33] Task: Restarting services on peer SP - PENDING
[16:53:33] Task: Installing new software on primary SP - PENDING
[16:53:33] Task: Rebooting the primary SP - PENDING
[16:53:33] Task: Restarting services on primary SP - PENDING
[16:53:33] Task: Final tasks - PENDING
[16:53:35] Status: IN_PROGRESS
[16:53:35] Progress: 12%
[16:53:35] Task: Preparing system - COMPLETED
[16:53:35] Task: Performing health checks - IN_PROGRESS
[16:53:35] Task: Preparing system software - PENDING
[16:53:35] Task: Waiting for reboot command - PENDING
[16:53:35] Task: Performing health checks - PENDING
[16:53:35] Task: Installing new software on peer SP - PENDING
[16:53:35] Task: Rebooting peer SP - PENDING
[16:53:35] Task: Restarting services on peer SP - PENDING
[16:53:35] Task: Installing new software on primary SP - PENDING
[16:53:35] Task: Rebooting the primary SP - PENDING
[16:53:35] Task: Restarting services on primary SP - PENDING
[16:53:35] Task: Final tasks - PENDING
[16:53:37] Status: IN_PROGRESS
[16:53:37] Progress: 17%
[16:53:37] Task: Preparing system - COMPLETED
[16:53:37] Task: Performing health checks - COMPLETED
[16:53:37] Task: Preparing system software - IN_PROGRESS
[16:53:37] Task: Waiting for reboot command - PENDING
[16:53:37] Task: Performing health checks - PENDING
[16:53:37] Task: Installing new software on peer SP - PENDING
[16:53:37] Task: Rebooting peer SP - PENDING
[16:53:37] Task: Restarting services on peer SP - PENDING
[16:53:37] Task: Installing new software on primary SP - PENDING
[16:53:37] Task: Rebooting the primary SP - PENDING
[16:53:37] Task: Restarting services on primary SP - PENDING
[16:53:37] Task: Final tasks - PENDING
[16:53:39] Status: IN_PROGRESS
[16:53:39] Progress: 20%
[16:53:39] Task: Preparing system - COMPLETED
[16:53:39] Task: Performing health checks - COMPLETED
[16:53:39] Task: Preparing system software - IN_PROGRESS
[16:53:39] Task: Waiting for reboot command - PENDING
[16:53:39] Task: Performing health checks - PENDING
[16:53:39] Task: Installing new software on peer SP - PENDING
[16:53:39] Task: Rebooting peer SP - PENDING
[16:53:39] Task: Restarting services on peer SP - PENDING
[16:53:39] Task: Installing new software on primary SP - PENDING
[16:53:39] Task: Rebooting the primary SP - PENDING
[16:53:39] Task: Restarting services on primary SP - PENDING
[16:53:39] Task: Final tasks - PENDING
[16:53:41] Status: IN_PROGRESS
[16:53:41] Progress: 21%
[16:53:41] Task: Preparing system - COMPLETED
[16:53:41] Task: Performing health checks - COMPLETED
[16:53:41] Task: Preparing system software - IN_PROGRESS
[16:53:41] Task: Waiting for reboot command - PENDING
[16:53:41] Task: Performing health checks - PENDING
[16:53:41] Task: Installing new software on peer SP - PENDING
[16:53:41] Task: Rebooting peer SP - PENDING
[16:53:41] Task: Restarting services on peer SP - PENDING
[16:53:41] Task: Installing new software on primary SP - PENDING
[16:53:41] Task: Rebooting the primary SP - PENDING
[16:53:41] Task: Restarting services on primary SP - PENDING
[16:53:41] Task: Final tasks - PENDING
[16:53:43] Status: IN_PROGRESS
[16:53:43] Progress: 24%
[16:53:43] Task: Preparing system - COMPLETED
[16:53:43] Task: Performing health checks - COMPLETED
[16:53:43] Task: Preparing system software - IN_PROGRESS
[16:53:43] Task: Waiting for reboot command - PENDING
[16:53:43] Task: Performing health checks - PENDING
[16:53:43] Task: Installing new software on peer SP - PENDING
[16:53:43] Task: Rebooting peer SP - PENDING
[16:53:43] Task: Restarting services on peer SP - PENDING
[16:53:43] Task: Installing new software on primary SP - PENDING
[16:53:43] Task: Rebooting the primary SP - PENDING
[16:53:43] Task: Restarting services on primary SP - PENDING
[16:53:43] Task: Final tasks - PENDING
[16:53:45] Status: IN_PROGRESS
[16:53:45] Progress: 41%
[16:53:45] Task: Preparing system - COMPLETED
[16:53:45] Task: Performing health checks - COMPLETED
[16:53:45] Task: Preparing system software - COMPLETED
[16:53:45] Task: Waiting for reboot command - COMPLETED
[16:53:45] Task: Performing health checks - COMPLETED
[16:53:45] Task: Installing new software on peer SP - IN_PROGRESS
[16:53:45] Task: Rebooting peer SP - PENDING
[16:53:45] Task: Restarting services on peer SP - PENDING
[16:53:45] Task: Installing new software on primary SP - PENDING
[16:53:45] Task: Rebooting the primary SP - PENDING
[16:53:45] Task: Restarting services on primary SP - PENDING
[16:53:45] Task: Final tasks - PENDING
[16:53:47] Status: IN_PROGRESS
[16:53:47] Progress: 44%
[16:53:47] Task: Preparing system - COMPLETED
[16:53:47] Task: Performing health checks - COMPLETED
[16:53:47] Task: Preparing system software - COMPLETED
[16:53:47] Task: Waiting for reboot command - COMPLETED
[16:53:47] Task: Performing health checks - COMPLETED
[16:53:47] Task: Installing new software on peer SP - IN_PROGRESS
[16:53:47] Task: Rebooting peer SP - PENDING
[16:53:47] Task: Restarting services on peer SP - PENDING
[16:53:47] Task: Installing new software on primary SP - PENDING
[16:53:47] Task: Rebooting the primary SP - PENDING
[16:53:47] Task: Restarting services on primary SP - PENDING
[16:53:47] Task: Final tasks - PENDING
[16:53:49] Status: IN_PROGRESS
[16:53:49] Progress: 45%
[16:53:49] Task: Preparing system - COMPLETED
[16:53:49] Task: Performing health checks - COMPLETED
[16:53:49] Task: Preparing system software - COMPLETED
[16:53:49] Task: Waiting for reboot command - COMPLETED
[16:53:49] Task: Performing health checks - COMPLETED
[16:53:49] Task: Installing new software on peer SP - IN_PROGRESS
[16:53:49] Task: Rebooting peer SP - PENDING
[16:53:49] Task: Restarting services on peer SP - PENDING
[16:53:49] Task: Installing new software on primary SP - PENDING
[16:53:49] Task: Rebooting the primary SP - PENDING
[16:53:49] Task: Restarting services on primary SP - PENDING
[16:53:49] Task: Final tasks - PENDING
[16:53:51] Status: IN_PROGRESS
[16:53:51] Progress: 48%
[16:53:51] Task: Preparing system - COMPLETED
[16:53:51] Task: Performing health checks - COMPLETED
[16:53:51] Task: Preparing system software - COMPLETED
[16:53:51] Task: Waiting for reboot command - COMPLETED
[16:53:51] Task: Performing health checks - COMPLETED
[16:53:51] Task: Installing new software on peer SP - IN_PROGRESS
[16:53:51] Task: Rebooting peer SP - PENDING
[16:53:51] Task: Restarting services on peer SP - PENDING
[16:53:51] Task: Installing new software on primary SP - PENDING
[16:53:51] Task: Rebooting the primary SP - PENDING
[16:53:51] Task: Restarting services on primary SP - PENDING
[16:53:51] Task: Final tasks - PENDING
[16:53:53] Status: IN_PROGRESS
[16:53:53] Progress: 50%
[16:53:53] Task: Preparing system - COMPLETED
[16:53:53] Task: Performing health checks - COMPLETED
[16:53:53] Task: Preparing system software - COMPLETED
[16:53:53] Task: Waiting for reboot command - COMPLETED
[16:53:53] Task: Performing health checks - COMPLETED
[16:53:53] Task: Installing new software on peer SP - COMPLETED
[16:53:53] Task: Rebooting peer SP - IN_PROGRESS
[16:53:53] Task: Restarting services on peer SP - PENDING
[16:53:53] Task: Installing new software on primary SP - PENDING
[16:53:53] Task: Rebooting the primary SP - PENDING
[16:53:53] Task: Restarting services on primary SP - PENDING
[16:53:53] Task: Final tasks - PENDING
[16:53:55] Status: IN_PROGRESS
[16:53:55] Progress: 52%
[16:53:55] Task: Preparing system - COMPLETED
[16:53:55] Task: Performing health checks - COMPLETED
[16:53:55] Task: Preparing system software - COMPLETED
[16:53:55] Task: Waiting for reboot command - COMPLETED
[16:53:55] Task: Performing health checks - COMPLETED
[16:53:55] Task: Installing new software on peer SP - COMPLETED
[16:53:55] Task: Rebooting peer SP - IN_PROGRESS
[16:53:55] Task: Restarting services on peer SP - PENDING
[16:53:55] Task: Installing new software on primary SP - PENDING
[16:53:55] Task: Rebooting the primary SP - PENDING
[16:53:55] Task: Restarting services on primary SP - PENDING
[16:53:55] Task: Final tasks - PENDING
[16:53:57] Status: IN_PROGRESS
[16:53:57] Progress: 54%
[16:53:57] Task: Preparing system - COMPLETED
[16:53:57] Task: Performing health checks - COMPLETED
[16:53:57] Task: Preparing system software - COMPLETED
[16:53:57] Task: Waiting for reboot command - COMPLETED
[16:53:57] Task: Performing health checks - COMPLETED
[16:53:57] Task: Installing new software on peer SP - COMPLETED
[16:53:57] Task: Rebooting peer SP - IN_PROGRESS
[16:53:57] Task: Restarting services on peer SP - PENDING
[16:53:57] Task: Installing new software on primary SP - PENDING
[16:53:57] Task: Rebooting the primary SP - PENDING
[16:53:57] Task: Restarting services on primary SP - PENDING
[16:53:57] Task: Final tasks - PENDING
[16:53:59] Status: IN_PROGRESS
[16:53:59] Progress: 57%
[16:53:59] Task: Preparing system - COMPLETED
[16:53:59] Task: Performing health checks - COMPLETED
[16:53:59] Task: Preparing system software - COMPLETED
[16:53:59] Task: Waiting for reboot command - COMPLETED
[16:53:59] Task: Performing health checks - COMPLETED
[16:53:59] Task: Installing new software on peer SP - COMPLETED
[16:53:59] Task: Rebooting peer SP - IN_PROGRESS
[16:53:59] Task: Restarting services on peer SP - PENDING
[16:53:59] Task: Installing new software on primary SP - PENDING
[16:53:59] Task: Rebooting the primary SP - PENDING
[16:53:59] Task: Restarting services on primary SP - PENDING
[16:53:59] Task: Final tasks - PENDING
[16:54:01] Status: IN_PROGRESS
[16:54:01] Progress: 62%
[16:54:01] Task: Preparing system - COMPLETED
[16:54:01] Task: Performing health checks - COMPLETED
[16:54:01] Task: Preparing system software - COMPLETED
[16:54:01] Task: Waiting for reboot command - COMPLETED
[16:54:01] Task: Performing health checks - COMPLETED
[16:54:01] Task: Installing new software on peer SP - COMPLETED
[16:54:01] Task: Rebooting peer SP - COMPLETED
[16:54:01] Task: Restarting services on peer SP - IN_PROGRESS
[16:54:01] Task: Installing new software on primary SP - PENDING
[16:54:01] Task: Rebooting the primary SP - PENDING
[16:54:01] Task: Restarting services on primary SP - PENDING
[16:54:01] Task: Final tasks - PENDING
[16:54:03] Status: IN_PROGRESS
[16:54:03] Progress: 67%
[16:54:03] Task: Preparing system - COMPLETED
[16:54:03] Task: Performing health checks - COMPLETED
[16:54:03] Task: Preparing system software - COMPLETED
[16:54:03] Task: Waiting for reboot command - COMPLETED
[16:54:03] Task: Performing health checks - COMPLETED
[16:54:03] Task: Installing new software on peer SP - COMPLETED
[16:54:03] Task: Rebooting peer SP - COMPLETED
[16:54:03] Task: Restarting services on peer SP - COMPLETED
[16:54:03] Task: Installing new software on primary SP - IN_PROGRESS
[16:54:03] Task: Rebooting the primary SP - PENDING
[16:54:03] Task: Restarting services on primary SP - PENDING
[16:54:03] Task: Final tasks - PENDING
[16:54:05] Status: IN_PROGRESS
[16:54:05] Progress: 70%
[16:54:05] Task: Preparing system - COMPLETED
[16:54:05] Task: Performing health checks - COMPLETED
[16:54:05] Task: Preparing system software - COMPLETED
[16:54:05] Task: Waiting for reboot command - COMPLETED
[16:54:05] Task: Performing health checks - COMPLETED
[16:54:05] Task: Installing new software on peer SP - COMPLETED
[16:54:05] Task: Rebooting peer SP - COMPLETED
[16:54:05] Task: Restarting services on peer SP - COMPLETED
[16:54:05] Task: Installing new software on primary SP - IN_PROGRESS
[16:54:05] Task: Rebooting the primary SP - PENDING
[16:54:05] Task: Restarting services on primary SP - PENDING
[16:54:05] Task: Final tasks - PENDING
[16:54:07] Status: IN_PROGRESS
[16:54:07] Progress: 72%
[16:54:07] Task: Preparing system - COMPLETED
[16:54:07] Task: Performing health checks - COMPLETED
[16:54:07] Task: Preparing system software - COMPLETED
[16:54:07] Task: Waiting for reboot command - COMPLETED
[16:54:07] Task: Performing health checks - COMPLETED
[16:54:07] Task: Installing new software on peer SP - COMPLETED
[16:54:07] Task: Rebooting peer SP - COMPLETED
[16:54:07] Task: Restarting services on peer SP - COMPLETED
[16:54:07] Task: Installing new software on primary SP - IN_PROGRESS
[16:54:07] Task: Rebooting the primary SP - PENDING
[16:54:07] Task: Restarting services on primary SP - PENDING
[16:54:07] Task: Final tasks - PENDING
[16:54:09] Status: IN_PROGRESS
[16:54:09] Progress: 75%
[16:54:09] Task: Preparing system - COMPLETED
[16:54:09] Task: Performing health checks - COMPLETED
[16:54:09] Task: Preparing system software - COMPLETED
[16:54:09] Task: Waiting for reboot command - COMPLETED
[16:54:09] Task: Performing health checks - COMPLETED
[16:54:09] Task: Installing new software on peer SP - COMPLETED
[16:54:09] Task: Rebooting peer SP - COMPLETED
[16:54:09] Task: Restarting services on peer SP - COMPLETED
[16:54:09] Task: Installing new software on primary SP - COMPLETED
[16:54:09] Task: Rebooting the primary SP - IN_PROGRESS
[16:54:09] Task: Restarting services on primary SP - PENDING
[16:54:09] Task: Final tasks - PENDING
[16:54:11] Status: IN_PROGRESS
[16:54:11] Progress: 76%
[16:54:11] Task: Preparing system - COMPLETED
[16:54:11] Task: Performing health checks - COMPLETED
[16:54:11] Task: Preparing system software - COMPLETED
[16:54:11] Task: Waiting for reboot command - COMPLETED
[16:54:11] Task: Performing health checks - COMPLETED
[16:54:11] Task: Installing new software on peer SP - COMPLETED
[16:54:11] Task: Rebooting peer SP - COMPLETED
[16:54:11] Task: Restarting services on peer SP - COMPLETED
[16:54:11] Task: Installing new software on primary SP - COMPLETED
[16:54:11] Task: Rebooting the primary SP - IN_PROGRESS
[16:54:11] Task: Restarting services on primary SP - PENDING
[16:54:11] Task: Final tasks - PENDING
[16:54:13] Status: IN_PROGRESS
[16:54:13] Progress: 79%
[16:54:13] Task: Preparing system - COMPLETED
[16:54:13] Task: Performing health checks - COMPLETED
[16:54:13] Task: Preparing system software - COMPLETED
[16:54:13] Task: Waiting for reboot command - COMPLETED
[16:54:13] Task: Performing health checks - COMPLETED
[16:54:13] Task: Installing new software on peer SP - COMPLETED
[16:54:13] Task: Rebooting peer SP - COMPLETED
[16:54:13] Task: Restarting services on peer SP - COMPLETED
[16:54:13] Task: Installing new software on primary SP - COMPLETED
[16:54:13] Task: Rebooting the primary SP - IN_PROGRESS
[16:54:13] Task: Restarting services on primary SP - PENDING
[16:54:13] Task: Final tasks - PENDING
[16:54:15] Status: IN_PROGRESS
[16:54:15] Progress: 81%
[16:54:15] Task: Preparing system - COMPLETED
[16:54:15] Task: Performing health checks - COMPLETED
[16:54:15] Task: Preparing system software - COMPLETED
[16:54:15] Task: Waiting for reboot command - COMPLETED
[16:54:15] Task: Performing health checks - COMPLETED
[16:54:15] Task: Installing new software on peer SP - COMPLETED
[16:54:15] Task: Rebooting peer SP - COMPLETED
[16:54:15] Task: Restarting services on peer SP - COMPLETED
[16:54:15] Task: Installing new software on primary SP - COMPLETED
[16:54:15] Task: Rebooting the primary SP - IN_PROGRESS
[16:54:15] Task: Restarting services on primary SP - PENDING
[16:54:15] Task: Final tasks - PENDING
[16:54:17] Status: IN_PROGRESS
[16:54:17] Progress: 86%
[16:54:17] Task: Preparing system - COMPLETED
[16:54:17] Task: Performing health checks - COMPLETED
[16:54:17] Task: Preparing system software - COMPLETED
[16:54:17] Task: Waiting for reboot command - COMPLETED
[16:54:17] Task: Performing health checks - COMPLETED
[16:54:17] Task: Installing new software on peer SP - COMPLETED
[16:54:17] Task: Rebooting peer SP - COMPLETED
[16:54:17] Task: Restarting services on peer SP - COMPLETED
[16:54:17] Task: Installing new software on primary SP - COMPLETED
[16:54:17] Task: Rebooting the primary SP - COMPLETED
[16:54:17] Task: Restarting services on primary SP - IN_PROGRESS
[16:54:17] Task: Final tasks - PENDING
[16:54:19] Status: COMPLETED
[16:54:19] Progress: 100%
[16:54:19] Task: Preparing system - COMPLETED
[16:54:19] Task: Performing health checks - COMPLETED
[16:54:19] Task: Preparing system software - COMPLETED
[16:54:19] Task: Waiting for reboot command - COMPLETED
[16:54:19] Task: Performing health checks - COMPLETED
[16:54:19] Task: Installing new software on peer SP - COMPLETED
[16:54:19] Task: Rebooting peer SP - COMPLETED
[16:54:19] Task: Restarting services on peer SP - COMPLETED
[16:54:19] Task: Installing new software on primary SP - COMPLETED
[16:54:19] Task: Rebooting the primary SP - COMPLETED
[16:54:19] Task: Restarting services on primary SP - COMPLETED
[16:54:19] Task: Final tasks - COMPLETED
[16:54:19] Upgrade completed successfully!
{
  "@base": "http://localhost:8000/api/instances/upgradeSession",
  "content": {
    "id": "Upgrade_5.4.0.0",
    "type": 0,
    "candidate": "file_4777df0b-d039-4e68-b081-ba8aea0a7d71",
    "caption": "Upgrade to 5.4.0.0",
    "status": 2,
    "startTime": "2025-03-23T16:53:32.886859",
    "messages": [],
    "creationTime": "2025-03-23T16:53:32.886862",
    "elapsedTime": "PT0H0M46S",
    "percentComplete": 100,
    "tasks": [
      {
        "status": 2,
        "type": 0,
        "caption": "Preparing system",
        "creationTime": "2025-03-23T16:53:32.886754",
        "estRemainTime": "00:03:30.000"
      },
      {
        "status": 2,
        "type": 0,
        "caption": "Performing health checks",
        "creationTime": "2025-03-23T16:53:32.886754",
        "estRemainTime": "00:02:10.000"
      },
      {
        "status": 2,
        "type": 0,
        "caption": "Preparing system software",
        "creationTime": "2025-03-23T16:53:32.886754",
        "estRemainTime": "00:16:10.000"
      },
      {
        "status": 2,
        "type": 0,
        "caption": "Waiting for reboot command",
        "creationTime": "2025-03-23T16:53:32.886754",
        "estRemainTime": "00:00:05.000"
      },
      {
        "status": 2,
        "type": 0,
        "caption": "Performing health checks",
        "creationTime": "2025-03-23T16:53:32.886754",
        "estRemainTime": "00:01:05.000"
      },
      {
        "status": 2,
        "type": 2,
        "caption": "Installing new software on peer SP",
        "creationTime": "2025-03-23T16:53:32.886754",
        "estRemainTime": "00:16:50.000"
      },
      {
        "status": 2,
        "type": 3,
        "caption": "Rebooting peer SP",
        "creationTime": "2025-03-23T16:53:32.886754",
        "estRemainTime": "00:14:15.000"
      },
      {
        "status": 2,
        "type": 2,
        "caption": "Restarting services on peer SP",
        "creationTime": "2025-03-23T16:53:32.886754",
        "estRemainTime": "00:05:00.000"
      },
      {
        "status": 2,
        "type": 2,
        "caption": "Installing new software on primary SP",
        "creationTime": "2025-03-23T16:53:32.886754",
        "estRemainTime": "00:13:30.000"
      },
      {
        "status": 2,
        "type": 3,
        "caption": "Rebooting the primary SP",
        "creationTime": "2025-03-23T16:53:32.886754",
        "estRemainTime": "00:13:55.000"
      },
      {
        "status": 2,
        "type": 2,
        "caption": "Restarting services on primary SP",
        "creationTime": "2025-03-23T16:53:32.886754",
        "estRemainTime": "00:05:10.000"
      },
      {
        "status": 2,
        "type": 2,
        "caption": "Final tasks",
        "creationTime": "2025-03-23T16:53:32.886754",
        "estRemainTime": "00:00:45.000"
      }
    ],
    "endTime": "2025-03-23T16:54:19.246294"
  },
  "links": [
    {
      "rel": "self",
      "href": "/Upgrade_5.4.0.0"
    }
  ],
  "updated": "2025-03-23T16:54:19.401Z"
}
```
```json
{
  "@base": "http://localhost:8000/api/types/upgradeSession/instances?per_page=2000",
  "updated": "2025-03-23T16:54:19.621Z",
  "links": [
    {
      "rel": "self",
      "href": "&page=1"
    }
  ],
  "entries": [
    {
      "@base": "http://localhost:8000/api/instances/upgradeSession",
      "content": {
        "id": "Upgrade_5.4.0.0",
        "type": 0,
        "candidate": "file_4777df0b-d039-4e68-b081-ba8aea0a7d71",
        "caption": "Upgrade to 5.4.0.0",
        "status": 2,
        "startTime": "2025-03-23T16:53:32.886859",
        "messages": [],
        "creationTime": "2025-03-23T16:53:32.886862",
        "elapsedTime": "PT0H0M46S",
        "percentComplete": 100,
        "tasks": [
          {
            "status": 2,
            "type": 0,
            "caption": "Preparing system",
            "creationTime": "2025-03-23T16:53:32.886754",
            "estRemainTime": "00:03:30.000"
          },
          {
            "status": 2,
            "type": 0,
            "caption": "Performing health checks",
            "creationTime": "2025-03-23T16:53:32.886754",
            "estRemainTime": "00:02:10.000"
          },
          {
            "status": 2,
            "type": 0,
            "caption": "Preparing system software",
            "creationTime": "2025-03-23T16:53:32.886754",
            "estRemainTime": "00:16:10.000"
          },
          {
            "status": 2,
            "type": 0,
            "caption": "Waiting for reboot command",
            "creationTime": "2025-03-23T16:53:32.886754",
            "estRemainTime": "00:00:05.000"
          },
          {
            "status": 2,
            "type": 0,
            "caption": "Performing health checks",
            "creationTime": "2025-03-23T16:53:32.886754",
            "estRemainTime": "00:01:05.000"
          },
          {
            "status": 2,
            "type": 2,
            "caption": "Installing new software on peer SP",
            "creationTime": "2025-03-23T16:53:32.886754",
            "estRemainTime": "00:16:50.000"
          },
          {
            "status": 2,
            "type": 3,
            "caption": "Rebooting peer SP",
            "creationTime": "2025-03-23T16:53:32.886754",
            "estRemainTime": "00:14:15.000"
          },
          {
            "status": 2,
            "type": 2,
            "caption": "Restarting services on peer SP",
            "creationTime": "2025-03-23T16:53:32.886754",
            "estRemainTime": "00:05:00.000"
          },
          {
            "status": 2,
            "type": 2,
            "caption": "Installing new software on primary SP",
            "creationTime": "2025-03-23T16:53:32.886754",
            "estRemainTime": "00:13:30.000"
          },
          {
            "status": 2,
            "type": 3,
            "caption": "Rebooting the primary SP",
            "creationTime": "2025-03-23T16:53:32.886754",
            "estRemainTime": "00:13:55.000"
          },
          {
            "status": 2,
            "type": 2,
            "caption": "Restarting services on primary SP",
            "creationTime": "2025-03-23T16:53:32.886754",
            "estRemainTime": "00:05:10.000"
          },
          {
            "status": 2,
            "type": 2,
            "caption": "Final tasks",
            "creationTime": "2025-03-23T16:53:32.886754",
            "estRemainTime": "00:00:45.000"
          }
        ],
        "endTime": "2025-03-23T16:54:19.246294"
      },
      "links": [
        {
          "rel": "self",
          "href": "/0"
        }
      ],
      "updated": "2025-03-23T16:54:19.621Z"
    }
  ]
}
```
Upgrade completed successfully!

## Task Completion Summary
| Task Name | Status | Duration |
| --- |
Logged out successfully
All tests completed. Results saved in ./tests/scripts/test_results/test_upgrade_flow_bash_report.md
