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
- Provides user interface for all commands organized in three main categories:
  - `system`: Commands for system operations (login, logout, configure, info, software-version)
  - `candidate`: Commands for candidate software operations (version, upload, prepare)
  - `upgrade`: Commands for software upgrade operations (sessions, verify, create, resume, cancel, monitor)
- Routes commands to appropriate business logic

#### Business Logic (client.py)
- Implements the core functionality
- Processes data between CLI and API layers
- Uses a stateless approach for all operations
- Authenticates with each API call instead of maintaining session state

#### API Communication Layer (http_client.py)
- Manages HTTP requests to the Unisphere REST API
- Handles authentication headers and tokens
- Processes API responses

#### Model Layer (models.py)
- Defines data structures using Pydantic
- Provides validation and serialization
- Represents API resources as Python objects

### Sequence Diagrams

#### Stateless Authentication Flow

```
┌─────┐          ┌──────────┐          ┌─────────┐          ┌─────────────┐
│ CLI │          │ Business │          │ API     │          │ Unisphere   │
│     │          │ Logic    │          │ Client  │          │ REST API    │
└──┬──┘          └────┬─────┘          └────┬────┘          └──────┬──────┘
   │                  │                     │                      │
   │ system login     │                     │                      │
   │─────────────────>│                     │                      │
   │                  │ load configuration  │                      │
   │                  │ from ~/.unisphere   │                      │
   │                  │ config.json         │                      │
   │                  │────────────────────>│                      │
   │                  │                     │                      │
   │                  │ authenticate with   │                      │
   │                  │ each API call       │                      │
   │                  │────────────────────>│                      │
   │                  │                     │ POST /api/login      │
   │                  │                     │─────────────────────>│
   │                  │                     │                      │
   │                  │                     │ 200 OK + CSRF token  │
   │                  │                     │<─────────────────────│
   │                  │ store credentials   │                      │
   │                  │ in config           │                      │
   │                  │<────────────────────│                      │
   │ success/failure  │                     │                      │
   │<─────────────────│                     │                      │
   │                  │                     │                      │
```

#### Stateless API Request Flow

```
┌─────┐          ┌──────────┐          ┌─────────┐          ┌─────────────┐
│ CLI │          │ Business │          │ API     │          │ Unisphere   │
│     │          │ Logic    │          │ Client  │          │ REST API    │
└──┬──┘          └────┬─────┘          └────┬────┘          └──────┬──────┘
   │                  │                     │                      │
   │ any command      │                     │                      │
   │─────────────────>│                     │                      │
   │                  │ load configuration  │                      │
   │                  │────────────────────>│                      │
   │                  │                     │                      │
   │                  │ prepare request     │                      │
   │                  │ with auth headers   │                      │
   │                  │────────────────────>│                      │
   │                  │                     │ API request with     │
   │                  │                     │ auth headers         │
   │                  │                     │─────────────────────>│
   │                  │                     │                      │
   │                  │                     │ 200 OK + response    │
   │                  │                     │<─────────────────────│
   │                  │ process response    │                      │
   │                  │<────────────────────│                      │
   │ formatted output │                     │                      │
   │<─────────────────│                     │                      │
   │                  │                     │                      │
```

## Requirements

### Functional Requirements

1. **Authentication and API Access**
   - The client must support authentication with the Unisphere API
   - The client must properly handle CSRF tokens and authentication headers
   - The client must provide a logout mechanism
   - The client must store configuration in `~/.unisphere/config.json`
   - Configuration file must contain:
     - base_url: Unisphere API endpoint URL
     - username: Authentication username
     - password: Authentication password (encrypted)
     - verify_ssl: Whether to verify SSL certificates
   - The client must authenticate with each API call (stateless approach)
   - The client must provide real-time progress updates during long-running operations

2. **Configuration Management**
   - Configuration file must be stored in JSON format with the following structure:
     * base_url: Unisphere API endpoint URL
     * username: Authentication username
     * password: Authentication password (encrypted)
     * verify_ssl: Whether to verify SSL certificates
   - The ~/.unisphere directory must be created with 700 permissions
   - Configuration file must be created with 600 permissions
   - The client must handle corrupted or invalid configuration files
   - The client must support configuration via command-line arguments

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
1. User runs `unisphere system configure --url <url> --username <username> --password <password>`
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
1. User runs `unisphere system login`
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
- A session file exists in ~/.unisphere

### System Information

#### UC-3: View System Information

**Description**: A user retrieves system information.

**Actors**: User, Client, Unisphere API

**Preconditions**:
- The user has an active session

**Flow**:
1. User runs `unisphere system info`
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
1. User runs `unisphere system software-version`
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
1. User runs `unisphere candidate version`
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
1. User runs `unisphere candidate upload --file <path>`
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
- The client is configured with valid credentials
- A candidate software version is available

**Flow**:
1. User runs `unisphere upgrade verify --version <version>`
2. Client loads configuration
3. Client authenticates with Unisphere API
4. Client sends verification request to Unisphere API
5. Unisphere API checks eligibility
6. Client displays eligibility results

**Postconditions**:
- The user knows if the system is eligible for upgrade

#### UC-8: Create Upgrade Session

**Description**: A user creates an upgrade session.

**Actors**: User, Client, Unisphere API

**Preconditions**:
- The client is configured with valid credentials
- The system is eligible for upgrade
- A candidate software version is available

**Flow**:
1. User runs `unisphere upgrade create --version <version>`
2. Client loads configuration
3. Client authenticates with Unisphere API
4. Client sends create request to Unisphere API with proper JSON structure
5. Unisphere API creates upgrade session
6. Client displays session information

**Postconditions**:
- An upgrade session is created

#### UC-10: Monitor Upgrade Session

**Description**: A user monitors the progress of an upgrade session in real-time.

**Actors**: User, Client, Unisphere API

**Preconditions**:
- The client is configured with valid credentials
- An active upgrade session exists

**Flow**:
1. User runs `unisphere upgrade monitor --interval <seconds>`
2. Client loads configuration
3. Client authenticates with Unisphere API
4. Client sends monitoring request to Unisphere API
5. Client displays upgrade status with:
   - Header with session information
   - Progress bar showing completion percentage
   - Task table with individual task status and estimated time
6. Client periodically refreshes the display at specified interval
7. Client handles connection issues with reconnection attempts
8. Client continues until upgrade completes or user interrupts

**Postconditions**:
- User has real-time visibility into upgrade progress

#### UC-11: Cancel Upgrade Session

**Description**: A user resumes a paused upgrade session.

**Actors**: User, Client, Unisphere API

**Preconditions**:
- The client is configured with valid credentials
- A paused upgrade session exists

**Flow**:
1. User runs `unisphere upgrade resume --id <session_id>`
2. Client loads configuration
3. Client authenticates with Unisphere API
4. Client sends resume request to Unisphere API
5. Unisphere API resumes the session
6. Client displays session status

**Postconditions**:
- The upgrade session is resumed
