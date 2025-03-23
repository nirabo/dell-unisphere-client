# Dell Unisphere Client - Comprehensive Test Report
Generated on: 2025-03-23 14:49:28


## Testing Complete Upgrade Flow
This test will create an upgrade session and monitor it until completion

## Step 1: Creating dummy upgrade file

## Creating dummy upgrade file
Created dummy upgrade file: ./tests/scripts/test_results/test_upgrade_client.bin (10.0MB)

## Step 2: Uploading software package
```json
{
  "id": "file_7701a4ca-b9ef-486f-9fca-ff143e79544b",
  "filename": "./tests/scripts/test_results/test_upgrade_client.bin",
  "size": 10485760
}
```
Uploaded software package: file_7701a4ca-b9ef-486f-9fca-ff143e79544b

## Step 3: Preparing software
```json
{
  "id": "candidate_8d65c7a0-fb65-4432-9653-8bca2baf3b4d",
  "status": "SUCCESS"
}
```
Software prepared successfully

## Step 4: Getting candidate software versions
```json
{
  "@base": "http://localhost:8000/api/types/candidateSoftwareVersion/instances?per_page=2000",
  "updated": "2025-03-23T14:49:28.378Z",
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
        "id": "file_7701a4ca-b9ef-486f-9fca-ff143e79544b",
        "version": "5.4.0.0",
        "fullVersion": "Unity ./tests/scripts/test_results/test_upgrade_client.bin",
        "revision": 0,
        "releaseDate": "2025-03-23T14:49:28.280561",
        "type": "SOFTWARE",
        "rebootRequired": true,
        "canPauseBeforeReboot": true
      },
      "links": [
        {
          "rel": "self",
          "href": "/file_7701a4ca-b9ef-486f-9fca-ff143e79544b"
        }
      ],
      "updated": "2025-03-23T14:49:28.378Z"
    },
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
      "updated": "2025-03-23T14:49:28.378Z"
    }
  ]
}
```
Found candidate ID: file_7701a4ca-b9ef-486f-9fca-ff143e79544b

## Step 5: Creating upgrade session
```json
{
  "id": "Upgrade_5.4.0.0",
  "content": {
    "id": "Upgrade_5.4.0.0",
    "type": 0,
    "candidate": "file_7701a4ca-b9ef-486f-9fca-ff143e79544b",
    "caption": "Upgrade to 5.4.0.0",
    "status": 1,
    "startTime": "2025-03-23T14:49:28.426072",
    "messages": [],
    "creationTime": "2025-03-23T14:49:28.426074",
    "elapsedTime": "PT0M",
    "percentComplete": 0,
    "tasks": [
      {
        "status": 1,
        "type": 0,
        "caption": "Preparing system",
        "creationTime": "2025-03-23T14:49:28.426004",
        "estRemainTime": "00:03:30.000"
      },
      {
        "status": 0,
        "type": 0,
        "caption": "Performing health checks",
        "creationTime": "2025-03-23T14:49:28.426004",
        "estRemainTime": "00:02:10.000"
      },
      {
        "status": 0,
        "type": 0,
        "caption": "Preparing system software",
        "creationTime": "2025-03-23T14:49:28.426004",
        "estRemainTime": "00:16:10.000"
      },
      {
        "status": 0,
        "type": 0,
        "caption": "Waiting for reboot command",
        "creationTime": "2025-03-23T14:49:28.426004",
        "estRemainTime": "00:00:05.000"
      },
      {
        "status": 0,
        "type": 0,
        "caption": "Performing health checks",
        "creationTime": "2025-03-23T14:49:28.426004",
        "estRemainTime": "00:01:05.000"
      },
      {
        "status": 0,
        "type": 2,
        "caption": "Installing new software on peer SP",
        "creationTime": "2025-03-23T14:49:28.426004",
        "estRemainTime": "00:16:50.000"
      },
      {
        "status": 0,
        "type": 3,
        "caption": "Rebooting peer SP",
        "creationTime": "2025-03-23T14:49:28.426004",
        "estRemainTime": "00:14:15.000"
      },
      {
        "status": 0,
        "type": 2,
        "caption": "Restarting services on peer SP",
        "creationTime": "2025-03-23T14:49:28.426004",
        "estRemainTime": "00:05:00.000"
      },
      {
        "status": 0,
        "type": 2,
        "caption": "Installing new software on primary SP",
        "creationTime": "2025-03-23T14:49:28.426004",
        "estRemainTime": "00:13:30.000"
      },
      {
        "status": 0,
        "type": 3,
        "caption": "Rebooting the primary SP",
        "creationTime": "2025-03-23T14:49:28.426004",
        "estRemainTime": "00:13:55.000"
      },
      {
        "status": 0,
        "type": 2,
        "caption": "Restarting services on primary SP",
        "creationTime": "2025-03-23T14:49:28.426004",
        "estRemainTime": "00:05:10.000"
      },
      {
        "status": 0,
        "type": 2,
        "caption": "Final tasks",
        "creationTime": "2025-03-23T14:49:28.426004",
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
