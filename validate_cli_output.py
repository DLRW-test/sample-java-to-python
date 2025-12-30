#!/usr/bin/env python3
"""Validate CLI Output Script.

This script validates that the CLI entry point (python -m sample_project.app)
produces the expected output matching the Java version's demo behavior.

It can be used standalone or as part of the installation test suite.
"""

import subprocess
import sys
from typing import List, Tuple


class CLIOutputValidator:
    """Validator for CLI output from sample_project.app."""

    # Expected output patterns based on Java version
    EXPECTED_PATTERNS = [
        # Single Loop section
        ("SingleForLoop", True),
        ("SumRange(10): 45", True),
        ("MaxArray([1, 2, 3, 4, 5]): 5", True),
        ("SumModulus(100, 3): 1683", True),
        # Double Loop section
        ("DoubleForLoop", True),
        ("SumSquare(10): 2025", True),
        ("SumTriangle(10): 165", True),
        ("CountPairs", True),
        ("CountDuplicates", True),
        # Vector section (exact values vary due to random generation)
        ("Vector", True),
        ("ModifyVector", True),
        ("SearchVector", True),
        ("SortVector", True),
        ("ReverseVector", True),
        ("RotateVector", True),
        ("MergeVectors", True),
        # Primes section
        ("Primes", True),
        ("IsPrime(10): False", True),
        ("SumPrimes(10): 17", True),
        ("PrimeFactors(10): [2, 5]", True),
        # Sort section (exact values vary due to random generation)
        ("Sort", True),
        ("SortVector", True),
        ("DutchFlagPartition", True),
        ("MaxN", True),
    ]

    def __init__(self, output: str):
        """Initialize validator with CLI output.

        Args:
            output: The complete output from running the CLI.
        """
        self.output = output
        self.results: List[Tuple[str, bool, bool]] = []

    def validate(self) -> bool:
        """Validate all expected patterns in the output.

        Returns:
            True if all required patterns are found, False otherwise.
        """
        all_passed = True

        for pattern, required in self.EXPECTED_PATTERNS:
            found = pattern in self.output
            self.results.append((pattern, required, found))

            if required and not found:
                all_passed = False

        return all_passed

    def print_report(self) -> None:
        """Print a detailed validation report."""
        print("\n" + "=" * 60)
        print("CLI Output Validation Report")
        print("=" * 60)
        print()

        required_count = sum(1 for _, req, _ in self.results if req)
        found_count = sum(1 for _, req, found in self.results if req and found)

        for pattern, required, found in self.results:
            status = "✓" if found else "✗"
            req_marker = "[REQUIRED]" if required else "[OPTIONAL]"
            print(f"{status} {req_marker} {pattern}")

        print()
        print(f"Results: {found_count}/{required_count} required patterns found")
        print()

        if found_count == required_count:
            print("✓ ALL VALIDATIONS PASSED")
            print("=" * 60)
            return True
        else:
            print("✗ VALIDATION FAILED")
            print("=" * 60)
            return False


def run_cli() -> Tuple[int, str, str]:
    """Run the CLI entry point and capture output.

    Returns:
        Tuple of (exit_code, stdout, stderr).
    """
    try:
        result = subprocess.run(
            [sys.executable, "-m", "sample_project.app"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "CLI execution timed out after 10 seconds"
    except Exception as e:
        return -1, "", f"Error running CLI: {e}"


def main() -> int:
    """Main entry point for the validation script.

    Returns:
        Exit code: 0 if validation passes, 1 otherwise.
    """
    print("=" * 60)
    print("CLI Entry Point Validation")
    print("=" * 60)
    print()
    print("Running: python -m sample_project.app")
    print()

    # Run the CLI
    exit_code, stdout, stderr = run_cli()

    # Check execution success
    if exit_code != 0:
        print(f"✗ CLI execution failed with exit code: {exit_code}")
        print()
        if stderr:
            print("Error output:")
            print(stderr)
        return 1

    print("✓ CLI execution completed successfully")
    print()

    # Show the output
    print("=" * 60)
    print("CLI Output:")
    print("=" * 60)
    print(stdout)
    print("=" * 60)

    # Validate the output
    validator = CLIOutputValidator(stdout)
    validation_passed = validator.validate()
    validator.print_report()

    # Check for any error output
    if stderr:
        print()
        print("⚠ Warning: CLI produced error output:")
        print(stderr)

    return 0 if validation_passed else 1


if __name__ == "__main__":
    sys.exit(main())
