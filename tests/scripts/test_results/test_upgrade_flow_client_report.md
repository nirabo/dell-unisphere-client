# Dell Unisphere Client - Comprehensive Test Report
Generated on: 2025-03-28 19:18:05


## Checking if API is running
API is running at http://localhost:8000

## Running General API Tests

## Login (unisphere system login)
Login successful

## Getting Basic System Info (unisphere system info)
```json
{
  "@base": "http://localhost:8000/api/types/basicSystemInfo/instances?per_page=2000",
  "updated": "2025-03-28T19:18:05.474Z",
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
      "updated": "2025-03-28T19:18:05.474Z"
    }
  ]
}
```

## Getting Installed Software Version (unisphere system software-version)
```json
{
  "@base": "http://localhost:8000/api/types/installedSoftwareVersion/instances?per_page=2000",
  "updated": "2025-03-28T19:18:05.525Z",
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
        "releaseDate": "2025-03-28T19:14:45.326699",
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
            "releaseDate": "2025-03-28T19:14:45.326709",
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
      "updated": "2025-03-28T19:18:05.525Z"
    }
  ]
}
```

## Getting Candidate Software Versions (unisphere candidate version)
```json
{
  "@base": "http://localhost:8000/api/types/candidateSoftwareVersion/instances?per_page=2000",
  "updated": "2025-03-28T19:18:05.580Z",
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
        "id": "candidate_0cf2c04a-c504-419f-b391-1cdbbfd9a958",
        "version": "5.4.0",
        "fullVersion": "Unity 5.4.0.0 (Release, Build 150, 2023-06-18 19:02:01, 5.4.0.0.5.150)",
        "revision": 150,
        "releaseDate": "2025-03-28T19:14:47.854065",
        "type": "SOFTWARE",
        "rebootRequired": true,
        "canPauseBeforeReboot": true
      },
      "links": [
        {
          "rel": "self",
          "href": "/candidate_0cf2c04a-c504-419f-b391-1cdbbfd9a958"
        }
      ],
      "updated": "2025-03-28T19:18:05.580Z"
    }
  ]
}
```

## Getting Software Upgrade Sessions (unisphere upgrade sessions)
```json
{
  "@base": "http://localhost:8000/api/types/upgradeSession/instances?per_page=2000",
  "updated": "2025-03-28T19:18:05.635Z",
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
        "candidate": "file_f73bd2cf-3abe-492d-a8d4-c209b80d2635",
        "caption": "Upgrade to 5.4.0.0",
        "status": 2,
        "startTime": "2025-03-28T19:14:47.961991",
        "messages": [],
        "creationTime": "2025-03-28T19:14:47.961995",
        "elapsedTime": "PT0H2M18S",
        "percentComplete": 100,
        "tasks": [
          {
            "status": 2,
            "type": 0,
            "caption": "Preparing system",
            "creationTime": "2025-03-28T19:14:47.961845",
            "estRemainTime": "00:03:30.000"
          },
          {
            "status": 2,
            "type": 0,
            "caption": "Performing health checks",
            "creationTime": "2025-03-28T19:14:47.961845",
            "estRemainTime": "00:02:10.000"
          },
          {
            "status": 2,
            "type": 0,
            "caption": "Preparing system software",
            "creationTime": "2025-03-28T19:14:47.961845",
            "estRemainTime": "00:16:10.000"
          },
          {
            "status": 2,
            "type": 0,
            "caption": "Waiting for reboot command",
            "creationTime": "2025-03-28T19:14:47.961845",
            "estRemainTime": "00:00:05.000"
          },
          {
            "status": 2,
            "type": 0,
            "caption": "Performing health checks",
            "creationTime": "2025-03-28T19:14:47.961845",
            "estRemainTime": "00:01:05.000"
          },
          {
            "status": 2,
            "type": 2,
            "caption": "Installing new software on peer SP",
            "creationTime": "2025-03-28T19:14:47.961845",
            "estRemainTime": "00:16:50.000"
          },
          {
            "status": 2,
            "type": 3,
            "caption": "Rebooting peer SP",
            "creationTime": "2025-03-28T19:14:47.961845",
            "estRemainTime": "00:14:15.000"
          },
          {
            "status": 2,
            "type": 2,
            "caption": "Restarting services on peer SP",
            "creationTime": "2025-03-28T19:14:47.961845",
            "estRemainTime": "00:05:00.000"
          },
          {
            "status": 2,
            "type": 2,
            "caption": "Installing new software on primary SP",
            "creationTime": "2025-03-28T19:14:47.961845",
            "estRemainTime": "00:13:30.000"
          },
          {
            "status": 2,
            "type": 3,
            "caption": "Rebooting the primary SP",
            "creationTime": "2025-03-28T19:14:47.961845",
            "estRemainTime": "00:13:55.000"
          },
          {
            "status": 2,
            "type": 2,
            "caption": "Restarting services on primary SP",
            "creationTime": "2025-03-28T19:14:47.961845",
            "estRemainTime": "00:05:10.000"
          },
          {
            "status": 2,
            "type": 2,
            "caption": "Final tasks",
            "creationTime": "2025-03-28T19:14:47.961845",
            "estRemainTime": "00:00:45.000"
          }
        ],
        "endTime": "2025-03-28T19:17:06.795213"
      },
      "links": [
        {
          "rel": "self",
          "href": "/0"
        }
      ],
      "updated": "2025-03-28T19:18:05.635Z"
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

## Step 2: Uploading software package (unisphere candidate upload)
```json
{
  "id": "file_f33f1ecf-d827-4c01-9670-40433b93be17",
  "filename": "./tests/scripts/test_results/test_upgrade_client.bin",
  "size": 10485760
}
```
Uploaded software package: file_f33f1ecf-d827-4c01-9670-40433b93be17

## Step 3: Verifying upgrade eligibility (unisphere upgrade verify)
Raw eligibility response:
```json
{
  "updated": "2025-03-28T19:18:05.930383Z",
  "content": {
    "statusMessage": "",
    "overallStatus": false
  }
}
```
Processed eligibility response:
```json
{
  "eligible": true,
  "messages": [],
  "requiredPatches": [],
  "requiredHotfixes": []
}
```
✅ System is eligible for upgrade

## Step 4: Preparing software (unisphere candidate prepare)
```json
{
  "id": "candidate_d0635afe-3428-4c88-b26e-4458b8d7898e",
  "status": "SUCCESS"
}
```
Software prepared successfully

## Step 5: Getting candidate software versions (unisphere candidate version)
```json
{
  "@base": "http://localhost:8000/api/types/candidateSoftwareVersion/instances?per_page=2000",
  "updated": "2025-03-28T19:18:06.095Z",
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
        "id": "file_f33f1ecf-d827-4c01-9670-40433b93be17",
        "version": "5.4.0.0",
        "fullVersion": "Unity ./tests/scripts/test_results/test_upgrade_client.bin",
        "revision": 0,
        "releaseDate": "2025-03-28T19:18:05.868710",
        "type": "SOFTWARE",
        "rebootRequired": true,
        "canPauseBeforeReboot": true
      },
      "links": [
        {
          "rel": "self",
          "href": "/file_f33f1ecf-d827-4c01-9670-40433b93be17"
        }
      ],
      "updated": "2025-03-28T19:18:06.095Z"
    },
    {
      "@base": "http://localhost:8000/api/instances/candidateSoftwareVersion",
      "content": {
        "id": "candidate_d0635afe-3428-4c88-b26e-4458b8d7898e",
        "version": "5.4.0",
        "fullVersion": "Unity 5.4.0.0 (Release, Build 150, 2023-06-18 19:02:01, 5.4.0.0.5.150)",
        "revision": 150,
        "releaseDate": "2025-03-28T19:18:06.038929",
        "type": "SOFTWARE",
        "rebootRequired": true,
        "canPauseBeforeReboot": true
      },
      "links": [
        {
          "rel": "self",
          "href": "/candidate_d0635afe-3428-4c88-b26e-4458b8d7898e"
        }
      ],
      "updated": "2025-03-28T19:18:06.095Z"
    }
  ]
}
```
Found candidate ID: file_f33f1ecf-d827-4c01-9670-40433b93be17

## Step 6: Creating upgrade session (unisphere upgrade create)
```json
{
  "id": "Upgrade_5.4.0.0",
  "content": {
    "id": "Upgrade_5.4.0.0",
    "type": 0,
    "candidate": "file_f33f1ecf-d827-4c01-9670-40433b93be17",
    "caption": "Upgrade to 5.4.0.0",
    "status": 1,
    "startTime": "2025-03-28T19:18:06.153286",
    "messages": [],
    "creationTime": "2025-03-28T19:18:06.153290",
    "elapsedTime": "PT0M",
    "percentComplete": 0,
    "tasks": [
      {
        "status": 1,
        "type": 0,
        "caption": "Preparing system",
        "creationTime": "2025-03-28T19:18:06.153158",
        "estRemainTime": "00:03:30.000"
      },
      {
        "status": 0,
        "type": 0,
        "caption": "Performing health checks",
        "creationTime": "2025-03-28T19:18:06.153158",
        "estRemainTime": "00:02:10.000"
      },
      {
        "status": 0,
        "type": 0,
        "caption": "Preparing system software",
        "creationTime": "2025-03-28T19:18:06.153158",
        "estRemainTime": "00:16:10.000"
      },
      {
        "status": 0,
        "type": 0,
        "caption": "Waiting for reboot command",
        "creationTime": "2025-03-28T19:18:06.153158",
        "estRemainTime": "00:00:05.000"
      },
      {
        "status": 0,
        "type": 0,
        "caption": "Performing health checks",
        "creationTime": "2025-03-28T19:18:06.153158",
        "estRemainTime": "00:01:05.000"
      },
      {
        "status": 0,
        "type": 2,
        "caption": "Installing new software on peer SP",
        "creationTime": "2025-03-28T19:18:06.153158",
        "estRemainTime": "00:16:50.000"
      },
      {
        "status": 0,
        "type": 3,
        "caption": "Rebooting peer SP",
        "creationTime": "2025-03-28T19:18:06.153158",
        "estRemainTime": "00:14:15.000"
      },
      {
        "status": 0,
        "type": 2,
        "caption": "Restarting services on peer SP",
        "creationTime": "2025-03-28T19:18:06.153158",
        "estRemainTime": "00:05:00.000"
      },
      {
        "status": 0,
        "type": 2,
        "caption": "Installing new software on primary SP",
        "creationTime": "2025-03-28T19:18:06.153158",
        "estRemainTime": "00:13:30.000"
      },
      {
        "status": 0,
        "type": 3,
        "caption": "Rebooting the primary SP",
        "creationTime": "2025-03-28T19:18:06.153158",
        "estRemainTime": "00:13:55.000"
      },
      {
        "status": 0,
        "type": 2,
        "caption": "Restarting services on primary SP",
        "creationTime": "2025-03-28T19:18:06.153158",
        "estRemainTime": "00:05:10.000"
      },
      {
        "status": 0,
        "type": 2,
        "caption": "Final tasks",
        "creationTime": "2025-03-28T19:18:06.153158",
        "estRemainTime": "00:00:45.000"
      }
    ]
  }
}
```
Created upgrade session: Upgrade_5.4.0.0

## Step 7: Monitoring upgrade progress (unisphere upgrade monitor)
Monitoring the upgrade session until completion
| Time | Status | Progress | Tasks |
| --- | --- | --- | --- |
Error monitoring upgrade: UnisphereClient.monitor_upgrade_session() got an unexpected keyword argument 'session_id'
