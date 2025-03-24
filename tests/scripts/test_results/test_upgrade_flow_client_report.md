# Dell Unisphere Client - Comprehensive Test Report
Generated on: 2025-03-24 15:44:03


## Checking if API is running
API is running at http://localhost:8000

## Running General API Tests

## Login
Login successful

## Getting Basic System Info
```json
{
  "@base": "http://localhost:8000/api/types/basicSystemInfo/instances?per_page=2000",
  "updated": "2025-03-24T15:44:03.172Z",
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
      "updated": "2025-03-24T15:44:03.172Z"
    }
  ]
}
```

## Getting Installed Software Version
```json
{
  "@base": "http://localhost:8000/api/types/installedSoftwareVersion/instances?per_page=2000",
  "updated": "2025-03-24T15:44:03.219Z",
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
        "releaseDate": "2025-03-24T10:44:17.157716",
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
            "releaseDate": "2025-03-24T10:44:17.157726",
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
      "updated": "2025-03-24T15:44:03.219Z"
    }
  ]
}
```

## Getting Candidate Software Versions
```json
{
  "@base": "http://localhost:8000/api/types/candidateSoftwareVersion/instances?per_page=2000",
  "updated": "2025-03-24T15:44:03.266Z",
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
        "id": "candidate_95586edb-0c2f-4387-be47-0fad9e7b7992",
        "version": "5.4.0",
        "fullVersion": "Unity 5.4.0.0 (Release, Build 150, 2023-06-18 19:02:01, 5.4.0.0.5.150)",
        "revision": 150,
        "releaseDate": "2025-03-24T15:39:26.640727",
        "type": "SOFTWARE",
        "rebootRequired": true,
        "canPauseBeforeReboot": true
      },
      "links": [
        {
          "rel": "self",
          "href": "/candidate_95586edb-0c2f-4387-be47-0fad9e7b7992"
        }
      ],
      "updated": "2025-03-24T15:44:03.266Z"
    }
  ]
}
```

## Getting Software Upgrade Sessions
```json
{
  "@base": "http://localhost:8000/api/types/upgradeSession/instances?per_page=2000",
  "updated": "2025-03-24T15:44:03.313Z",
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
        "candidate": "file_b22d1f31-887b-4e9a-bc83-a811f8bd0647",
        "caption": "Upgrade to 5.4.0.0",
        "status": 2,
        "startTime": "2025-03-24T15:39:26.736446",
        "messages": [],
        "creationTime": "2025-03-24T15:39:26.736450",
        "elapsedTime": "PT0H0M46S",
        "percentComplete": 100,
        "tasks": [
          {
            "status": 2,
            "type": 0,
            "caption": "Preparing system",
            "creationTime": "2025-03-24T15:39:26.736307",
            "estRemainTime": "00:03:30.000"
          },
          {
            "status": 2,
            "type": 0,
            "caption": "Performing health checks",
            "creationTime": "2025-03-24T15:39:26.736307",
            "estRemainTime": "00:02:10.000"
          },
          {
            "status": 2,
            "type": 0,
            "caption": "Preparing system software",
            "creationTime": "2025-03-24T15:39:26.736307",
            "estRemainTime": "00:16:10.000"
          },
          {
            "status": 2,
            "type": 0,
            "caption": "Waiting for reboot command",
            "creationTime": "2025-03-24T15:39:26.736307",
            "estRemainTime": "00:00:05.000"
          },
          {
            "status": 2,
            "type": 0,
            "caption": "Performing health checks",
            "creationTime": "2025-03-24T15:39:26.736307",
            "estRemainTime": "00:01:05.000"
          },
          {
            "status": 2,
            "type": 2,
            "caption": "Installing new software on peer SP",
            "creationTime": "2025-03-24T15:39:26.736307",
            "estRemainTime": "00:16:50.000"
          },
          {
            "status": 2,
            "type": 3,
            "caption": "Rebooting peer SP",
            "creationTime": "2025-03-24T15:39:26.736307",
            "estRemainTime": "00:14:15.000"
          },
          {
            "status": 2,
            "type": 2,
            "caption": "Restarting services on peer SP",
            "creationTime": "2025-03-24T15:39:26.736307",
            "estRemainTime": "00:05:00.000"
          },
          {
            "status": 2,
            "type": 2,
            "caption": "Installing new software on primary SP",
            "creationTime": "2025-03-24T15:39:26.736307",
            "estRemainTime": "00:13:30.000"
          },
          {
            "status": 2,
            "type": 3,
            "caption": "Rebooting the primary SP",
            "creationTime": "2025-03-24T15:39:26.736307",
            "estRemainTime": "00:13:55.000"
          },
          {
            "status": 2,
            "type": 2,
            "caption": "Restarting services on primary SP",
            "creationTime": "2025-03-24T15:39:26.736307",
            "estRemainTime": "00:05:10.000"
          },
          {
            "status": 2,
            "type": 2,
            "caption": "Final tasks",
            "creationTime": "2025-03-24T15:39:26.736307",
            "estRemainTime": "00:00:45.000"
          }
        ],
        "endTime": "2025-03-24T15:40:13.091223"
      },
      "links": [
        {
          "rel": "self",
          "href": "/0"
        }
      ],
      "updated": "2025-03-24T15:44:03.313Z"
    }
  ]
}
```

## Verifying Upgrade Eligibility
```json
{
  "eligible": false,
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
  "id": "file_bdfd72cd-bd8f-4319-a3e4-8e8c2dfc73ca",
  "filename": "./tests/scripts/test_results/test_upgrade_client.bin",
  "size": 10485760
}
```
Uploaded software package: file_bdfd72cd-bd8f-4319-a3e4-8e8c2dfc73ca

## Step 3: Preparing software
```json
{
  "id": "candidate_9467b1ae-4a03-481c-a96e-52ad70f7b3a8",
  "status": "SUCCESS"
}
```
Software prepared successfully

## Step 4: Getting candidate software versions
```json
{
  "@base": "http://localhost:8000/api/types/candidateSoftwareVersion/instances?per_page=2000",
  "updated": "2025-03-24T15:44:03.585Z",
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
        "id": "file_bdfd72cd-bd8f-4319-a3e4-8e8c2dfc73ca",
        "version": "5.4.0.0",
        "fullVersion": "Unity ./tests/scripts/test_results/test_upgrade_client.bin",
        "revision": 0,
        "releaseDate": "2025-03-24T15:44:03.527559",
        "type": "SOFTWARE",
        "rebootRequired": true,
        "canPauseBeforeReboot": true
      },
      "links": [
        {
          "rel": "self",
          "href": "/file_bdfd72cd-bd8f-4319-a3e4-8e8c2dfc73ca"
        }
      ],
      "updated": "2025-03-24T15:44:03.585Z"
    },
    {
      "@base": "http://localhost:8000/api/instances/candidateSoftwareVersion",
      "content": {
        "id": "candidate_9467b1ae-4a03-481c-a96e-52ad70f7b3a8",
        "version": "5.4.0",
        "fullVersion": "Unity 5.4.0.0 (Release, Build 150, 2023-06-18 19:02:01, 5.4.0.0.5.150)",
        "revision": 150,
        "releaseDate": "2025-03-24T15:44:03.539715",
        "type": "SOFTWARE",
        "rebootRequired": true,
        "canPauseBeforeReboot": true
      },
      "links": [
        {
          "rel": "self",
          "href": "/candidate_9467b1ae-4a03-481c-a96e-52ad70f7b3a8"
        }
      ],
      "updated": "2025-03-24T15:44:03.585Z"
    }
  ]
}
```
Found candidate ID: file_bdfd72cd-bd8f-4319-a3e4-8e8c2dfc73ca

## Step 5: Creating upgrade session
```json
{
  "id": "Upgrade_5.4.0.0",
  "content": {
    "id": "Upgrade_5.4.0.0",
    "type": 0,
    "candidate": "file_bdfd72cd-bd8f-4319-a3e4-8e8c2dfc73ca",
    "caption": "Upgrade to 5.4.0.0",
    "status": 1,
    "startTime": "2025-03-24T15:44:03.634113",
    "messages": [],
    "creationTime": "2025-03-24T15:44:03.634117",
    "elapsedTime": "PT0M",
    "percentComplete": 0,
    "tasks": [
      {
        "status": 1,
        "type": 0,
        "caption": "Preparing system",
        "creationTime": "2025-03-24T15:44:03.633982",
        "estRemainTime": "00:03:30.000"
      },
      {
        "status": 0,
        "type": 0,
        "caption": "Performing health checks",
        "creationTime": "2025-03-24T15:44:03.633982",
        "estRemainTime": "00:02:10.000"
      },
      {
        "status": 0,
        "type": 0,
        "caption": "Preparing system software",
        "creationTime": "2025-03-24T15:44:03.633982",
        "estRemainTime": "00:16:10.000"
      },
      {
        "status": 0,
        "type": 0,
        "caption": "Waiting for reboot command",
        "creationTime": "2025-03-24T15:44:03.633982",
        "estRemainTime": "00:00:05.000"
      },
      {
        "status": 0,
        "type": 0,
        "caption": "Performing health checks",
        "creationTime": "2025-03-24T15:44:03.633982",
        "estRemainTime": "00:01:05.000"
      },
      {
        "status": 0,
        "type": 2,
        "caption": "Installing new software on peer SP",
        "creationTime": "2025-03-24T15:44:03.633982",
        "estRemainTime": "00:16:50.000"
      },
      {
        "status": 0,
        "type": 3,
        "caption": "Rebooting peer SP",
        "creationTime": "2025-03-24T15:44:03.633982",
        "estRemainTime": "00:14:15.000"
      },
      {
        "status": 0,
        "type": 2,
        "caption": "Restarting services on peer SP",
        "creationTime": "2025-03-24T15:44:03.633982",
        "estRemainTime": "00:05:00.000"
      },
      {
        "status": 0,
        "type": 2,
        "caption": "Installing new software on primary SP",
        "creationTime": "2025-03-24T15:44:03.633982",
        "estRemainTime": "00:13:30.000"
      },
      {
        "status": 0,
        "type": 3,
        "caption": "Rebooting the primary SP",
        "creationTime": "2025-03-24T15:44:03.633982",
        "estRemainTime": "00:13:55.000"
      },
      {
        "status": 0,
        "type": 2,
        "caption": "Restarting services on primary SP",
        "creationTime": "2025-03-24T15:44:03.633982",
        "estRemainTime": "00:05:10.000"
      },
      {
        "status": 0,
        "type": 2,
        "caption": "Final tasks",
        "creationTime": "2025-03-24T15:44:03.633982",
        "estRemainTime": "00:00:45.000"
      }
    ]
  }
}
```
Created upgrade session: Upgrade_5.4.0.0

## Step 6: Monitoring upgrade progress
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
    "candidate": "file_bdfd72cd-bd8f-4319-a3e4-8e8c2dfc73ca",
    "caption": "Upgrade to 5.4.0.0",
    "status": 2,
    "startTime": "2025-03-24T15:44:03.634113",
    "messages": [],
    "creationTime": "2025-03-24T15:44:03.634117",
    "elapsedTime": "PT0H0M46S",
    "percentComplete": 100,
    "tasks": [
      {
        "status": 2,
        "type": 0,
        "caption": "Preparing system",
        "creationTime": "2025-03-24T15:44:03.633982",
        "estRemainTime": "00:03:30.000"
      },
      {
        "status": 2,
        "type": 0,
        "caption": "Performing health checks",
        "creationTime": "2025-03-24T15:44:03.633982",
        "estRemainTime": "00:02:10.000"
      },
      {
        "status": 2,
        "type": 0,
        "caption": "Preparing system software",
        "creationTime": "2025-03-24T15:44:03.633982",
        "estRemainTime": "00:16:10.000"
      },
      {
        "status": 2,
        "type": 0,
        "caption": "Waiting for reboot command",
        "creationTime": "2025-03-24T15:44:03.633982",
        "estRemainTime": "00:00:05.000"
      },
      {
        "status": 2,
        "type": 0,
        "caption": "Performing health checks",
        "creationTime": "2025-03-24T15:44:03.633982",
        "estRemainTime": "00:01:05.000"
      },
      {
        "status": 2,
        "type": 2,
        "caption": "Installing new software on peer SP",
        "creationTime": "2025-03-24T15:44:03.633982",
        "estRemainTime": "00:16:50.000"
      },
      {
        "status": 2,
        "type": 3,
        "caption": "Rebooting peer SP",
        "creationTime": "2025-03-24T15:44:03.633982",
        "estRemainTime": "00:14:15.000"
      },
      {
        "status": 2,
        "type": 2,
        "caption": "Restarting services on peer SP",
        "creationTime": "2025-03-24T15:44:03.633982",
        "estRemainTime": "00:05:00.000"
      },
      {
        "status": 2,
        "type": 2,
        "caption": "Installing new software on primary SP",
        "creationTime": "2025-03-24T15:44:03.633982",
        "estRemainTime": "00:13:30.000"
      },
      {
        "status": 2,
        "type": 3,
        "caption": "Rebooting the primary SP",
        "creationTime": "2025-03-24T15:44:03.633982",
        "estRemainTime": "00:13:55.000"
      },
      {
        "status": 2,
        "type": 2,
        "caption": "Restarting services on primary SP",
        "creationTime": "2025-03-24T15:44:03.633982",
        "estRemainTime": "00:05:10.000"
      },
      {
        "status": 2,
        "type": 2,
        "caption": "Final tasks",
        "creationTime": "2025-03-24T15:44:03.633982",
        "estRemainTime": "00:00:45.000"
      }
    ],
    "endTime": "2025-03-24T15:44:49.993950"
  },
  "links": [
    {
      "rel": "self",
      "href": "/Upgrade_5.4.0.0"
    }
  ],
  "updated": "2025-03-24T15:44:51.959Z"
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
