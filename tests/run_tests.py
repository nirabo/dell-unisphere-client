#!/usr/bin/env python
"""
Test runner script for Dell Unisphere Client.

This script provides a command-line interface for running tests with various options.
"""

import argparse
import os
import subprocess
import sys


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Run Dell Unisphere Client tests")

    parser.add_argument(
        "--unit", action="store_true", default=False, help="Run unit tests only"
    )
    parser.add_argument(
        "--integration",
        action="store_true",
        default=False,
        help="Run integration tests only",
    )
    parser.add_argument(
        "--e2e", action="store_true", default=False, help="Run end-to-end tests only"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        default=False,
        help="Run all tests (unit, integration, and e2e)",
    )
    parser.add_argument(
        "--coverage",
        action="store_true",
        default=False,
        help="Generate coverage report",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", default=False, help="Verbose output"
    )
    parser.add_argument(
        "--skip-e2e",
        action="store_true",
        default=False,
        help="Skip end-to-end tests even if --all or --e2e is specified",
    )
    parser.add_argument(
        "pytest_args", nargs="*", help="Additional arguments to pass to pytest"
    )

    return parser.parse_args()


def run_tests(args):
    """Run tests based on command line arguments."""
    # Determine which tests to run
    if not any([args.unit, args.integration, args.e2e, args.all]):
        # Default to all tests if none specified
        args.all = True

    # Build pytest command
    cmd = ["pytest"]

    # Add verbosity
    if args.verbose:
        cmd.append("-v")

    # Add coverage if requested
    if args.coverage:
        cmd.extend(
            [
                "--cov=dell_unisphere_client",
                "--cov-report=term",
                "--cov-report=html:coverage_html",
                "--cov-report=xml:coverage.xml",
            ]
        )

    # Determine test paths
    test_paths = []
    if args.all or args.unit:
        test_paths.append("tests/unit")
    if args.all or args.integration:
        test_paths.append("tests/integration")
    if (args.all or args.e2e) and not args.skip_e2e:
        test_paths.append("tests/e2e")

    # Add test paths to command
    cmd.extend(test_paths)

    # Add additional pytest arguments
    cmd.extend(args.pytest_args)

    # Set environment variables
    env = os.environ.copy()
    if args.skip_e2e:
        env["SKIP_E2E_TESTS"] = "1"

    # Print command if verbose
    if args.verbose:
        print(f"Running command: {' '.join(cmd)}")

    # Run the tests
    return subprocess.call(cmd, env=env)


def main():
    """Main entry point."""
    args = parse_args()
    return run_tests(args)


if __name__ == "__main__":
    sys.exit(main())
