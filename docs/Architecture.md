# Dell Unisphere Client Architecture

This document outlines the architecture, requirements, and use cases for the Dell Unisphere Client, a command-line interface (CLI) for interacting with the Dell Unisphere REST API.

## Table of Contents

- [Dell Unisphere Client Architecture](#dell-unisphere-client-architecture)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Architecture](#architecture)
    - [Component Diagram](#component-diagram)
      - [CLI Layer (cli.py)](#cli-layer-clipy)
      - [Business Logic (client.py)](#business-logic-clientpy)
      - [API Communication Layer (http\_client.py)](#api-communication-layer-http_clientpy)
      - [Model Layer (models.py)](#model-layer-modelspy)
    - [Sequence Diagrams](#sequence-diagrams)
      - [Authentication Flow](#authentication-flow)
  - [Requirements](#requirements)
    - [Functional Requirements](#functional-requirements)
    - [Non-Functional Requirements](#non-functional-requirements)
  - [Use Cases](#use-cases)
    - [Authentication](#authentication)
      - [UC-1: Configure Client](#uc-1-configure-client)
      - [UC-2: Login to Unisphere](#uc-2-login-to-unisphere)
    - [System Information](#system-information)
      - [UC-3: View System Information](#uc-3-view-system-information)
    - [Software Management](#software-management)
      - [UC-4: List Installed Software](#uc-4-list-installed-software)
      - [UC-5: List Candidate Software](#uc-5-list-candidate-software)
      - [UC-6: Upload Software Package](#uc-6-upload-software-package)
    - [Upgrade Workflow](#upgrade-workflow)
      - [UC-7: Verify Upgrade Eligibility](#uc-7-verify-upgrade-eligibility)
      - [UC-8: Create Upgrade Session](#uc-8-create-upgrade-session)
      - [UC-9: Resume Upgrade Session](#uc-9-resume-upgrade-session)

## Overview

The Dell Unisphere Client is a Python-based command-line interface that enables users to interact with Dell Unity storage systems through the Unisphere REST API. It provides a convenient and scriptable way to perform common operations such as retrieving system information, managing software versions, and performing software upgrades.

## Architecture

The Dell Unisphere Client follows a layered architecture pattern, separating concerns between the CLI interface, business logic, and API communication.

### Component Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                     Dell Unisphere Client                       │
├─────────────┬─────────────────────────┬─────────────────────────┤
│             │                         │                         │
│  CLI Layer  │    Business Logic       │   API Communication     │
│  (cli.py)   │    (client.py)          │   (http_client.py)      │
│             │                         │                         │
├─────────────┴─────────────────────────┴─────────────────────────┤
│                                                                 │
│                       Model Layer (models.py)                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### CLI Layer (cli.py)
- Handles command-line parsing using argparse
- Provides user interface for all commands
- Routes commands to appropriate business logic

#### Business Logic (client.py)
- Implements the core functionality
- Processes data between CLI and API layers
- Handles authentication and session management

#### API Communication Layer (http_client.py)
- Manages HTTP requests to the Unisphere REST API
- Handles authentication headers and tokens
- Processes API responses

#### Model Layer (models.py)
- Defines data structures using Pydantic
- Provides validation and serialization
- Represents API resources as Python objects

### Sequence Diagrams

#### Authentication Flow

```
┌─────┐          ┌──────────┐          ┌─────────┐          ┌─────────────┐
│ CLI │          │ Business │          │ API     │          │ Unisphere   │
│     │          │ Logic    │          │ Client  │          │ REST API    │
└──┬──┘          └────┬─────┘          └────┬────┘          └──────┬──────┘
   │                  │                     │                      │
   │ login command    │                     │                      │
   │─────────────────>│                     │                      │
   │                  │ check ~/.uniclient  │                      │
   │                  │ for session file    │                      │
   │                  │<────────────────────│                      │
   │                  │                     │                      │
   │                  │ session exists?     │                      │
   │                  │────────────────────>│                      │
   │                  │                     │                      │
   │                  │ yes: validate       │                      │
   │                  │ session timeout     │                      │
   │                  │────────────────────>│                      │
   │                  │                     │                      │
   │                  │ if valid: reuse     │                      │
   │                  │ else: authenticate  │                      │
   │                  │────────────────────>│                      │
   │                  │                     │ GET login session    │
   │                  │                     │─────────────────────>│
   │                  │                     │                      │
   │                  │                     │ 200 OK + CSRF token  │
   │                  │                     │<─────────────────────│
   │                  │ create session file │                      │
   │                  │ with timeout,       │                      │
   │                  │ CSRF token, cookie, │                      │
   │                  │ and credentials     │                      │
   │                  │<────────────────────│                      │
   │ success/failure  │                     │                      │
   │<─────────────────│                     │                      │
   │                  │                     │                      │
```

## Requirements

### Functional Requirements

1. **Authentication and Session Management**
   - The client must support authentication with the Unisphere API
   - The client must properly handle CSRF tokens and session cookies
   - The client must provide a logout mechanism
   - The client must cache session information in `~/.uniclient/session_<timestamped_id>`
   - Session files must contain:
     - idle_timeout period
     - CSRF token
     - session cookies
     - username/password (encrypted)
     - creation and last access timestamps
   - The client must reuse valid cached sessions when available
   - The client must automatically expire sessions after idle_timeout
   - The client must provide real-time progress updates during long-running operations
   - The client must cache sessions in ~/.uniclient/session_<timestamped_id> files
   - The client must reuse valid existing sessions
   - The client must validate session timeout on each operation

2. **Session Persistence**
   - Session files must be stored in JSON format with the following structure:
     * idle_timeout: Session timeout duration in seconds
     * csrf_token: CSRF token (if available)
     * session_cookie: Session cookie (if available)
     * username: Authentication username
     * password: Authentication password
     * creation_timestamp: Session creation time
     * last_access_timestamp: Last session access time
   - The ~/.uniclient directory must be created with 700 permissions
   - Session files must be created with 600 permissions
   - The client must handle corrupted or invalid session files
   - The client must delete session files on logout

3. **System Information**
   - The client must retrieve and display basic system information
   - The client must retrieve and display detailed system information

4. **Software Version Management**
   - The client must list installed software versions
   - The client must list candidate software versions
   - The client must support uploading software packages

5. **Software Upgrade Workflow**
   - The client must verify upgrade eligibility
   - The client must create upgrade sessions
   - The client must resume paused upgrade sessions
   - The client must display upgrade session status and progress

6. **Configuration Management**
   - The client must store and retrieve configuration (credentials, server URL)
   - The client must support configuration via command-line arguments

### Non-Functional Requirements

1. **Usability**
   - The client must provide clear, consistent command syntax
   - The client must display helpful error messages
   - The client must provide help text for all commands

2. **Security**
   - The client must securely handle credentials
   - The client must not store passwords in plain text
   - The client must support secure connections (HTTPS)
   - The client must maintain proper file permissions for session files

3. **Performance**
   - The client must respond to commands within a reasonable time
   - The client must handle large responses efficiently

4. **Compatibility**
   - The client must be compatible with Python 3.8+
   - The client must be installable via pip
   - The client must work on Linux, macOS, and Windows

5. **Maintainability**
   - The client must follow PEP 8 style guidelines
   - The client must include comprehensive tests
   - The client must use type hints for better code quality

## Use Cases

### Authentication

#### UC-1: Configure Client

**Description**: A user configures the client with server URL and credentials.

**Actors**: User, Client

**Preconditions**:
- The client is installed

**Flow**:
1. User runs `uniclient configure --url <url> --username <username> --password <password>`
2. Client validates the URL format
3. Client stores the configuration securely
4. Client confirms successful configuration

**Postconditions**:
- The client is configured with server URL and credentials

#### UC-2: Login to Unisphere

**Description**: A user logs in to establish a session.

**Actors**: User, Client, Unisphere API

**Preconditions**:
- The client is configured with server URL and credentials

**Flow**:
1. User runs `uniclient login`
2. Client checks for existing session file
3. If valid session exists:
   a. Client loads session data
   b. Client validates session timeout
4. If no valid session exists:
   a. Client retrieves stored credentials
   b. Client sends authentication request to Unisphere API
   c. Unisphere API validates credentials and returns session token
   d. Client creates session file
5. Client confirms successful login

**Postconditions**:
- The user has an active session
- The client has stored the session token
- A session file exists in ~/.uniclient

### System Information

#### UC-3: View System Information

**Description**: A user retrieves system information.

**Actors**: User, Client, Unisphere API

**Preconditions**:
- The user has an active session

**Flow**:
1. User runs `uniclient system-info`
2. Client validates session timeout
3. Client sends request to Unisphere API
4. Unisphere API returns system information
5. Client formats and displays the information
6. Client updates session file last_access_timestamp

**Postconditions**:
- The user sees system information
- The session file is updated

### Software Management

#### UC-4: List Installed Software

**Description**: A user lists installed software versions.

**Actors**: User, Client, Unisphere API

**Preconditions**:
- The user has an active session

**Flow**:
1. User runs `uniclient software-version`
2. Client validates session timeout
3. Client sends request to Unisphere API
4. Unisphere API returns installed software information
5. Client formats and displays the information
6. Client updates session file last_access_timestamp

**Postconditions**:
- The user sees installed software information
- The session file is updated

#### UC-5: List Candidate Software

**Description**: A user lists candidate software versions.

**Actors**: User, Client, Unisphere API

**Preconditions**:
- The user has an active session

**Flow**:
1. User runs `uniclient candidate-versions`
2. Client validates session timeout
3. Client sends request to Unisphere API
4. Unisphere API returns candidate software information
5. Client formats and displays the information
6. Client updates session file last_access_timestamp

**Postconditions**:
- The user sees candidate software information
- The session file is updated

#### UC-6: Upload Software Package

**Description**: A user uploads a software package.

**Actors**: User, Client, Unisphere API

**Preconditions**:
- The user has an active session
- The user has a valid software package file

**Flow**:
1. User runs `uniclient upload-package --file <path>`
2. Client validates session timeout
3. Client validates the file exists
4. Client uploads the file to Unisphere API
5. Unisphere API processes the upload
6. Client confirms successful upload
7. Client updates session file last_access_timestamp

**Postconditions**:
- The software package is uploaded to the Unisphere system
- The session file is updated

### Upgrade Workflow

#### UC-7: Verify Upgrade Eligibility

**Description**: A user verifies if a system is eligible for upgrade.

**Actors**: User, Client, Unisphere API

**Preconditions**:
- The user has an active session
- A candidate software version is available

**Flow**:
1. User runs `uniclient verify-upgrade --version <version>`
2. Client validates session timeout
3. Client sends verification request to Unisphere API
4. Unisphere API checks eligibility
5. Client displays eligibility results
6. Client updates session file last_access_timestamp

**Postconditions**:
- The user knows if the system is eligible for upgrade
- The session file is updated

#### UC-8: Create Upgrade Session

**Description**: A user creates an upgrade session.

**Actors**: User, Client, Unisphere API

**Preconditions**:
- The user has an active session
- The system is eligible for upgrade
- A candidate software version is available

**Flow**:
1. User runs `uniclient create-upgrade --version <version>`
2. Client validates session timeout
3. Client sends create request to Unisphere API
4. Unisphere API creates upgrade session
5. Client displays session information
6. Client updates session file last_access_timestamp

**Postconditions**:
- An upgrade session is created
- The session file is updated

#### UC-9: Resume Upgrade Session

**Description**: A user resumes a paused upgrade session.

**Actors**: User, Client, Unisphere API

**Preconditions**:
- The user has an active session
- A paused upgrade session exists

**Flow**:
1. User runs `uniclient resume-upgrade --id <session_id>`
2. Client validates session timeout
3. Client sends resume request to Unisphere API
4. Unisphere API resumes the session
5. Client displays session status
6. Client updates session file last_access_timestamp

**Postconditions**:
- The upgrade session is resumed
- The session file is updated
