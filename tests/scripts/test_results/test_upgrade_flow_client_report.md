# Dell Unisphere Client - Comprehensive Test Report
Generated on: 2025-03-25 09:59:00


## Checking if API is running
API is running at http://localhost:8000

## Running General API Tests

## Login
Login successful

## Getting Basic System Info
```json
{
  "@base": "http://localhost:8000/api/types/basicSystemInfo/instances?per_page=2000",
  "updated": "2025-03-25T09:59:00.870Z",
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
      "updated": "2025-03-25T09:59:00.870Z"
    }
  ]
}
```

## Getting Installed Software Version
```json
{
  "@base": "http://localhost:8000/api/types/installedSoftwareVersion/instances?per_page=2000",
  "updated": "2025-03-25T09:59:00.922Z",
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
        "releaseDate": "2025-03-25T08:22:12.406698",
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
            "releaseDate": "2025-03-25T08:22:12.406707",
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
      "updated": "2025-03-25T09:59:00.922Z"
    }
  ]
}
```

## Getting Candidate Software Versions
```json
{
  "@base": "http://localhost:8000/api/types/candidateSoftwareVersion/instances?per_page=2000",
  "updated": "2025-03-25T09:59:00.979Z",
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
        "id": "file_b0c37bb3-50da-41ee-b01d-a50c19fc5bdb",
        "version": "5.4.0.0",
        "fullVersion": "Unity ./tests/scripts/test_results/test_upgrade_client.bin",
        "revision": 0,
        "releaseDate": "2025-03-25T09:09:38.160971",
        "type": "SOFTWARE",
        "rebootRequired": true,
        "canPauseBeforeReboot": true
      },
      "links": [
        {
          "rel": "self",
          "href": "/file_b0c37bb3-50da-41ee-b01d-a50c19fc5bdb"
        }
      ],
      "updated": "2025-03-25T09:59:00.979Z"
    }
  ]
}
```

## Getting Software Upgrade Sessions
```json
{
  "@base": "http://localhost:8000/api/types/upgradeSession/instances?per_page=2000",
  "updated": "2025-03-25T09:59:01.035Z",
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
        "candidate": "file_66613a41-6b0a-4a5c-b639-034837ade3e7",
        "caption": "Upgrade to 5.4.0.0",
        "status": 2,
        "startTime": "2025-03-25T09:05:34.887754",
        "messages": [],
        "creationTime": "2025-03-25T09:05:34.887758",
        "elapsedTime": "PT0H0M46S",
        "percentComplete": 100,
        "tasks": [
          {
            "status": 2,
            "type": 0,
            "caption": "Preparing system",
            "creationTime": "2025-03-25T09:05:34.887649",
            "estRemainTime": "00:03:30.000"
          },
          {
            "status": 2,
            "type": 0,
            "caption": "Performing health checks",
            "creationTime": "2025-03-25T09:05:34.887649",
            "estRemainTime": "00:02:10.000"
          },
          {
            "status": 2,
            "type": 0,
            "caption": "Preparing system software",
            "creationTime": "2025-03-25T09:05:34.887649",
            "estRemainTime": "00:16:10.000"
          },
          {
            "status": 2,
            "type": 0,
            "caption": "Waiting for reboot command",
            "creationTime": "2025-03-25T09:05:34.887649",
            "estRemainTime": "00:00:05.000"
          },
          {
            "status": 2,
            "type": 0,
            "caption": "Performing health checks",
            "creationTime": "2025-03-25T09:05:34.887649",
            "estRemainTime": "00:01:05.000"
          },
          {
            "status": 2,
            "type": 2,
            "caption": "Installing new software on peer SP",
            "creationTime": "2025-03-25T09:05:34.887649",
            "estRemainTime": "00:16:50.000"
          },
          {
            "status": 2,
            "type": 3,
            "caption": "Rebooting peer SP",
            "creationTime": "2025-03-25T09:05:34.887649",
            "estRemainTime": "00:14:15.000"
          },
          {
            "status": 2,
            "type": 2,
            "caption": "Restarting services on peer SP",
            "creationTime": "2025-03-25T09:05:34.887649",
            "estRemainTime": "00:05:00.000"
          },
          {
            "status": 2,
            "type": 2,
            "caption": "Installing new software on primary SP",
            "creationTime": "2025-03-25T09:05:34.887649",
            "estRemainTime": "00:13:30.000"
          },
          {
            "status": 2,
            "type": 3,
            "caption": "Rebooting the primary SP",
            "creationTime": "2025-03-25T09:05:34.887649",
            "estRemainTime": "00:13:55.000"
          },
          {
            "status": 2,
            "type": 2,
            "caption": "Restarting services on primary SP",
            "creationTime": "2025-03-25T09:05:34.887649",
            "estRemainTime": "00:05:10.000"
          },
          {
            "status": 2,
            "type": 2,
            "caption": "Final tasks",
            "creationTime": "2025-03-25T09:05:34.887649",
            "estRemainTime": "00:00:45.000"
          }
        ],
        "endTime": "2025-03-25T09:06:21.244021"
      },
      "links": [
        {
          "rel": "self",
          "href": "/0"
        }
      ],
      "updated": "2025-03-25T09:59:01.035Z"
    }
  ]
}
```

## Verifying Upgrade Eligibility
```json
{
  "eligible": true,
  "messages": [],
  "requiredPatches": [],
  "requiredHotfixes": []
}
```

## Testing Complete Upgrade Flow
This test will create an upgrade session and monitor it until completion

## Step 1: Creating dummy upgrade file

## Creating dummy upgrade file
Created dummy upgrade file: ./tests/scripts/test_results/test_upgrade_client.bin (10.0MB)

## Step 2: Uploading software package
```json
{
  "id": "file_ceeb5ee2-9250-4aee-ac8a-cf2235083f15",
  "filename": "./tests/scripts/test_results/test_upgrade_client.bin",
  "size": 10485760
}
```
Uploaded software package: file_ceeb5ee2-9250-4aee-ac8a-cf2235083f15

## Step 3: Verifying upgrade eligibility
```json
{
  "eligible": true,
  "messages": [],
  "requiredPatches": [],
  "requiredHotfixes": []
}
```
✅ System is eligible for upgrade

## Step 4: Preparing software
```json
{
  "id": "candidate_e7de9262-789d-461d-ad1b-67e4c07fa22a",
  "status": "SUCCESS"
}
```
Software prepared successfully

## Step 5: Getting candidate software versions
```json
{
  "@base": "http://localhost:8000/api/types/candidateSoftwareVersion/instances?per_page=2000",
  "updated": "2025-03-25T09:59:01.436Z",
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
        "id": "file_ceeb5ee2-9250-4aee-ac8a-cf2235083f15",
        "version": "5.4.0.0",
        "fullVersion": "Unity ./tests/scripts/test_results/test_upgrade_client.bin",
        "revision": 0,
        "releaseDate": "2025-03-25T09:59:01.268447",
        "type": "SOFTWARE",
        "rebootRequired": true,
        "canPauseBeforeReboot": true
      },
      "links": [
        {
          "rel": "self",
          "href": "/file_ceeb5ee2-9250-4aee-ac8a-cf2235083f15"
        }
      ],
      "updated": "2025-03-25T09:59:01.436Z"
    },
    {
      "@base": "http://localhost:8000/api/instances/candidateSoftwareVersion",
      "content": {
        "id": "candidate_e7de9262-789d-461d-ad1b-67e4c07fa22a",
        "version": "5.4.0",
        "fullVersion": "Unity 5.4.0.0 (Release, Build 150, 2023-06-18 19:02:01, 5.4.0.0.5.150)",
        "revision": 150,
        "releaseDate": "2025-03-25T09:59:01.385620",
        "type": "SOFTWARE",
        "rebootRequired": true,
        "canPauseBeforeReboot": true
      },
      "links": [
        {
          "rel": "self",
          "href": "/candidate_e7de9262-789d-461d-ad1b-67e4c07fa22a"
        }
      ],
      "updated": "2025-03-25T09:59:01.436Z"
    }
  ]
}
```
Found candidate ID: file_ceeb5ee2-9250-4aee-ac8a-cf2235083f15

## Step 6: Creating upgrade session
```json
{
  "id": "Upgrade_5.4.0.0",
  "content": {
    "id": "Upgrade_5.4.0.0",
    "type": 0,
    "candidate": "file_ceeb5ee2-9250-4aee-ac8a-cf2235083f15",
    "caption": "Upgrade to 5.4.0.0",
    "status": 1,
    "startTime": "2025-03-25T09:59:01.490301",
    "messages": [],
    "creationTime": "2025-03-25T09:59:01.490306",
    "elapsedTime": "PT0M",
    "percentComplete": 0,
    "tasks": [
      {
        "status": 1,
        "type": 0,
        "caption": "Preparing system",
        "creationTime": "2025-03-25T09:59:01.490170",
        "estRemainTime": "00:03:30.000"
      },
      {
        "status": 0,
        "type": 0,
        "caption": "Performing health checks",
        "creationTime": "2025-03-25T09:59:01.490170",
        "estRemainTime": "00:02:10.000"
      },
      {
        "status": 0,
        "type": 0,
        "caption": "Preparing system software",
        "creationTime": "2025-03-25T09:59:01.490170",
        "estRemainTime": "00:16:10.000"
      },
      {
        "status": 0,
        "type": 0,
        "caption": "Waiting for reboot command",
        "creationTime": "2025-03-25T09:59:01.490170",
        "estRemainTime": "00:00:05.000"
      },
      {
        "status": 0,
        "type": 0,
        "caption": "Performing health checks",
        "creationTime": "2025-03-25T09:59:01.490170",
        "estRemainTime": "00:01:05.000"
      },
      {
        "status": 0,
        "type": 2,
        "caption": "Installing new software on peer SP",
        "creationTime": "2025-03-25T09:59:01.490170",
        "estRemainTime": "00:16:50.000"
      },
      {
        "status": 0,
        "type": 3,
        "caption": "Rebooting peer SP",
        "creationTime": "2025-03-25T09:59:01.490170",
        "estRemainTime": "00:14:15.000"
      },
      {
        "status": 0,
        "type": 2,
        "caption": "Restarting services on peer SP",
        "creationTime": "2025-03-25T09:59:01.490170",
        "estRemainTime": "00:05:00.000"
      },
      {
        "status": 0,
        "type": 2,
        "caption": "Installing new software on primary SP",
        "creationTime": "2025-03-25T09:59:01.490170",
        "estRemainTime": "00:13:30.000"
      },
      {
        "status": 0,
        "type": 3,
        "caption": "Rebooting the primary SP",
        "creationTime": "2025-03-25T09:59:01.490170",
        "estRemainTime": "00:13:55.000"
      },
      {
        "status": 0,
        "type": 2,
        "caption": "Restarting services on primary SP",
        "creationTime": "2025-03-25T09:59:01.490170",
        "estRemainTime": "00:05:10.000"
      },
      {
        "status": 0,
        "type": 2,
        "caption": "Final tasks",
        "creationTime": "2025-03-25T09:59:01.490170",
        "estRemainTime": "00:00:45.000"
      }
    ]
  }
}
```
Created upgrade session: Upgrade_5.4.0.0

## Step 7: Monitoring upgrade progress
Monitoring the upgrade session until completion
| Time | Status | Progress | Tasks |
| --- | --- | --- | --- |
Upgrade completed successfully!
```json
{
  "@base": "http://localhost:8000/api/instances/upgradeSession",
  "content": {
    "id": "Upgrade_5.4.0.0",
    "type": 0,
    "candidate": "file_ceeb5ee2-9250-4aee-ac8a-cf2235083f15",
    "caption": "Upgrade to 5.4.0.0",
    "status": 2,
    "startTime": "2025-03-25T09:59:01.490301",
    "messages": [],
    "creationTime": "2025-03-25T09:59:01.490306",
    "elapsedTime": "PT0H0M46S",
    "percentComplete": 100,
    "tasks": [
      {
        "status": 2,
        "type": 0,
        "caption": "Preparing system",
        "creationTime": "2025-03-25T09:59:01.490170",
        "estRemainTime": "00:03:30.000"
      },
      {
        "status": 2,
        "type": 0,
        "caption": "Performing health checks",
        "creationTime": "2025-03-25T09:59:01.490170",
        "estRemainTime": "00:02:10.000"
      },
      {
        "status": 2,
        "type": 0,
        "caption": "Preparing system software",
        "creationTime": "2025-03-25T09:59:01.490170",
        "estRemainTime": "00:16:10.000"
      },
      {
        "status": 2,
        "type": 0,
        "caption": "Waiting for reboot command",
        "creationTime": "2025-03-25T09:59:01.490170",
        "estRemainTime": "00:00:05.000"
      },
      {
        "status": 2,
        "type": 0,
        "caption": "Performing health checks",
        "creationTime": "2025-03-25T09:59:01.490170",
        "estRemainTime": "00:01:05.000"
      },
      {
        "status": 2,
        "type": 2,
        "caption": "Installing new software on peer SP",
        "creationTime": "2025-03-25T09:59:01.490170",
        "estRemainTime": "00:16:50.000"
      },
      {
        "status": 2,
        "type": 3,
        "caption": "Rebooting peer SP",
        "creationTime": "2025-03-25T09:59:01.490170",
        "estRemainTime": "00:14:15.000"
      },
      {
        "status": 2,
        "type": 2,
        "caption": "Restarting services on peer SP",
        "creationTime": "2025-03-25T09:59:01.490170",
        "estRemainTime": "00:05:00.000"
      },
      {
        "status": 2,
        "type": 2,
        "caption": "Installing new software on primary SP",
        "creationTime": "2025-03-25T09:59:01.490170",
        "estRemainTime": "00:13:30.000"
      },
      {
        "status": 2,
        "type": 3,
        "caption": "Rebooting the primary SP",
        "creationTime": "2025-03-25T09:59:01.490170",
        "estRemainTime": "00:13:55.000"
      },
      {
        "status": 2,
        "type": 2,
        "caption": "Restarting services on primary SP",
        "creationTime": "2025-03-25T09:59:01.490170",
        "estRemainTime": "00:05:10.000"
      },
      {
        "status": 2,
        "type": 2,
        "caption": "Final tasks",
        "creationTime": "2025-03-25T09:59:01.490170",
        "estRemainTime": "00:00:45.000"
      }
    ],
    "endTime": "2025-03-25T09:59:47.844144"
  },
  "links": [
    {
      "rel": "self",
      "href": "/Upgrade_5.4.0.0"
    }
  ],
  "updated": "2025-03-25T09:59:49.840Z"
}
```

## Task Completion Summary
| Task Name | Status | Duration |
| --- | --- | --- |
| Preparing system | COMPLETED | N/A |
| Performing health checks | COMPLETED | N/A |
| Preparing system software | COMPLETED | N/A |
| Waiting for reboot command | COMPLETED | N/A |
| Performing health checks | COMPLETED | N/A |
| Installing new software on peer SP | COMPLETED | N/A |
| Rebooting peer SP | COMPLETED | N/A |
| Restarting services on peer SP | COMPLETED | N/A |
| Installing new software on primary SP | COMPLETED | N/A |
| Rebooting the primary SP | COMPLETED | N/A |
| Restarting services on primary SP | COMPLETED | N/A |
| Final tasks | COMPLETED | N/A |
