# Changelog

All notable changes to the Dell Unisphere Client will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.6.0] - 2025-03-28

### Added
- New nested CLI command structure with three main command groups
- New `cancel` upgrade command placeholder for future implementation
- Version information now displayed in the help banner
- New stateless method `monitor_upgrade_sessions` in UnisphereClient class
- Comprehensive Marp presentation document for client implementation
- Enhanced monitoring interface with estimated time display for each task
- Total estimated remaining time calculation in status bar
- Cumulative total estimated time display in status bar
- Clear indication when no upgrade session is detected
- Robust version management system with pyproject.toml as single source of truth
- Version consistency testing to prevent version mismatches

### Changed
- Reorganized CLI commands into logical groups: `system`, `candidate`, and `upgrade`
- Removed standalone version command in favor of integrated version display
- Updated all tests and documentation to reflect the new command structure
- Improved command discoverability with better organization
- Removed session management code to implement fully stateless approach
- Updated client to use correct schema for creating upgrade sessions
- Replaced print statements with proper logging in API modules
- Improved logging format with clear section separators and better JSON formatting
- Improved layout with tasks table as the main focus
- Reordered task columns to show estimated time before status
- Integrated progress bar into the status header
- Improved reconnection handling with consistent UI layout
- Enhanced error messaging during connection issues
- Better time formatting for improved readability
- CLI now always reads version from pyproject.toml for consistency

## [0.3.0] - 2025-03-24

### Added
- Verbose CLI functionality with `--verbose` flag for all commands
- Detailed request and response visualization for API calls
- Enhanced debugging capabilities for API interactions

### Changed
- Improved error handling for authentication failures
- Enhanced code formatting and style consistency
- Updated test suite to support verbose mode

## [0.2.0] - 2025-03-23

### Added
- Session management with persistent sessions
- Upgrade monitoring capabilities
- Comprehensive error handling
- Enhanced CSRF token handling
- Improved test coverage with E2E tests
- Upgrade flow testing script

### Changed
- Refactored API client structure
- Enhanced CLI output formatting
- Improved error messages
- Updated documentation

### Fixed
- Session timeout handling
- CSRF token refresh mechanism
- Error handling during upgrade process

## [0.1.0] - 2025-02-15

### Added
- Initial release
- Basic API client for Dell Unisphere REST API
- Command-line interface for core API operations
- Authentication and session management
- CSRF token handling
- Software upgrade management
- File upload support
- Unit and integration tests
