# Makefile for Dell Unisphere Client

# Variables
PYTHON := python
PIP := pip
UV := uv
APP_NAME := dell-unisphere-client
SRC_DIR := src
TEST_DIR := tests
VENV := .venv

# Check if uv is available, otherwise use pip
ifeq ($(shell which uv >/dev/null 2>&1; echo $$?), 0)
	PKG_MANAGER := uv
else
	PKG_MANAGER := pip
endif

# Default target
all: install test lint

# Create virtual environment
venv:
	$(PYTHON) -m venv $(VENV)
	@echo "Virtual environment created. Activate with 'source $(VENV)/bin/activate'"

# Install dependencies
install:
ifeq ($(PKG_MANAGER), uv)
	$(UV) pip install -e .
else
	$(PIP) install -e .
endif

# Install in development mode
dev:
ifeq ($(PKG_MANAGER), uv)
	$(UV) pip install -e ".[dev]"
else
	$(PIP) install -e ".[dev]"
endif

# Run tests
test:
ifeq ($(PKG_MANAGER), uv)
	$(UV) run python -m pytest $(TEST_DIR) --cov=$(SRC_DIR) --cov-report=term
else
	$(PYTHON) -m pytest $(TEST_DIR) --cov=$(SRC_DIR) --cov-report=term
endif

# Run unit tests only
test-unit:
ifeq ($(PKG_MANAGER), uv)
	$(UV) run python -m pytest $(TEST_DIR)/unit --cov=$(SRC_DIR) --cov-report=term
else
	$(PYTHON) -m pytest $(TEST_DIR)/unit --cov=$(SRC_DIR) --cov-report=term
endif

# Run integration tests only
test-integration:
ifeq ($(PKG_MANAGER), uv)
	$(UV) run python -m pytest $(TEST_DIR)/integration --cov=$(SRC_DIR) --cov-report=term
else
	$(PYTHON) -m pytest $(TEST_DIR)/integration --cov=$(SRC_DIR) --cov-report=term
endif

# Run end-to-end tests only
test-e2e:
ifeq ($(PKG_MANAGER), uv)
	UNISPHERE_URL=http://localhost:8000 UNISPHERE_USERNAME=admin UNISPHERE_PASSWORD=Password123! UNISPHERE_VERIFY_SSL=false $(UV) run python -m pytest $(TEST_DIR)/e2e --cov=$(SRC_DIR) --cov-report=term
else
	UNISPHERE_URL=http://localhost:8000 UNISPHERE_USERNAME=admin UNISPHERE_PASSWORD=Password123! UNISPHERE_VERIFY_SSL=false $(PYTHON) -m pytest $(TEST_DIR)/e2e --cov=$(SRC_DIR) --cov-report=term
endif

# Generate coverage report
coverage:
ifeq ($(PKG_MANAGER), uv)
	$(UV) run python -m pytest $(TEST_DIR) --cov=$(SRC_DIR) --cov-report=term --cov-report=html:coverage_html --cov-report=xml:coverage.xml
else
	$(PYTHON) -m pytest $(TEST_DIR) --cov=$(SRC_DIR) --cov-report=term --cov-report=html:coverage_html --cov-report=xml:coverage.xml
endif

# Run the CLI
run:
ifeq ($(PKG_MANAGER), uv)
	$(UV) run python -m dell_unisphere_client.cli
else
	$(PYTHON) -m dell_unisphere_client.cli
endif

# Lint code
lint:
ifeq ($(PKG_MANAGER), uv)
	$(UV) run ruff check $(SRC_DIR)
else
	ruff check $(SRC_DIR)
endif

# Format code
format:
ifeq ($(PKG_MANAGER), uv)
	$(UV) run ruff format $(SRC_DIR)
else
	ruff format $(SRC_DIR)
endif

# Clean build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name "*.pyc" -delete

# Build package
build:
ifeq ($(PKG_MANAGER), uv)
	$(UV) run python -m build
else
	$(PYTHON) -m build
endif

# Install package from PyPI
pip-install:
ifeq ($(PKG_MANAGER), uv)
	$(UV) pip install $(APP_NAME)
else
	$(PIP) install $(APP_NAME)
endif

# Uninstall package
pip-uninstall:
ifeq ($(PKG_MANAGER), uv)
	$(UV) pip uninstall -y $(APP_NAME)
else
	$(PIP) uninstall -y $(APP_NAME)
endif

# Upload to PyPI (requires credentials)
upload:
ifeq ($(PKG_MANAGER), uv)
	$(UV) run python -m twine upload dist/*
else
	$(PYTHON) -m twine upload dist/*
endif

# Upload to TestPyPI (for testing)
upload-test:
ifeq ($(PKG_MANAGER), uv)
	$(UV) run python -m twine upload --repository testpypi dist/*
else
	$(PYTHON) -m twine upload --repository testpypi dist/*
endif

# Help
help:
	@echo "Available targets:"
	@echo "  all           - Install dependencies, run tests, and lint code"
	@echo "  venv          - Create a virtual environment"
	@echo "  install       - Install package dependencies"
	@echo "  dev           - Install package in development mode"
	@echo "  test          - Run tests"
	@echo "  test-unit     - Run unit tests only"
	@echo "  test-integration - Run integration tests only"
	@echo "  test-e2e      - Run end-to-end tests only"
	@echo "  coverage      - Generate coverage report"
	@echo "  run           - Run the CLI"
	@echo "  lint          - Check code style"
	@echo "  format        - Format code"
	@echo "  clean         - Remove build artifacts"
	@echo "  build         - Build package"
	@echo "  pip-install   - Install package from PyPI"
	@echo "  pip-uninstall - Uninstall package"
	@echo "  upload        - Upload to PyPI"
	@echo "  upload-test   - Upload to TestPyPI"
	@echo "  help          - Show this help message"

.PHONY: all venv install dev test test-unit test-integration test-e2e coverage run lint format clean build pip-install pip-uninstall upload upload-test help
