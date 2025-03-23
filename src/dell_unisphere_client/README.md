# Dell Unisphere Client - Modular Structure

This directory contains the Dell Unisphere Client implementation, which has been refactored into a modular structure to improve maintainability and reduce mental overload.

## Directory Structure

- `__init__.py` - Package initialization and exports
- `client_new.py` - Main client class that orchestrates the different modules
- `exceptions/` - Exception classes used throughout the client
- `session/` - Session management functionality
- `api/` - API modules for different endpoints
  - `base.py` - Base API client with common functionality
  - `system.py` - System-related API endpoints
  - `software.py` - Software-related API endpoints
  - `upgrade.py` - Upgrade-related API endpoints

## Design Principles

1. **Separation of Concerns**: Each module has a specific responsibility
2. **Modularity**: Components can be developed and tested independently
3. **Reusability**: Common functionality is extracted into base classes
4. **Maintainability**: Smaller files are easier to understand and modify

## Usage

The main client class (`UnisphereClient`) provides the same interface as before, but internally delegates to the appropriate modules. This ensures backward compatibility while improving the code structure.

```python
from dell_unisphere_client import UnisphereClient

# Create a client
client = UnisphereClient(
    base_url="https://unisphere.example.com",
    username="admin",
    password="password",
    verify_ssl=True
)

# Use the client as before
client.login()
system_info = client.get_system_info()
client.logout()
```

## Testing

The modular structure makes it easier to test individual components in isolation. Each module can be tested independently, which simplifies the testing process and improves test coverage.

## Migration

To migrate to the new structure:

1. The package exports the same interface, so existing code should continue to work
2. Update imports to use the new module structure if you were importing specific components
3. Run tests to ensure compatibility

## Future Improvements

- Add more specific API modules as needed
- Improve error handling and logging
- Add more comprehensive documentation
