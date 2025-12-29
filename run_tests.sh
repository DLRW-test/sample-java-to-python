#!/bin/bash
# Test Execution Script for Python Test Suite with Coverage
# This script runs the comprehensive pytest suite with coverage reporting
# for all Python modules translated from the Java implementation.

set -e  # Exit on any error

echo "========================================="
echo "Python Test Suite Execution with Coverage"
echo "========================================="
echo ""

# Check if pytest is installed
if ! command -v pytest &> /dev/null; then
    echo "ERROR: pytest is not installed."
    echo "Please install it with: pip install pytest pytest-cov"
    exit 1
fi

# Check if pytest-cov is installed
if ! python -c "import pytest_cov" 2>/dev/null; then
    echo "ERROR: pytest-cov is not installed."
    echo "Please install it with: pip install pytest-cov"
    exit 1
fi

echo "Running pytest with coverage..."
echo ""

# Execute pytest with coverage flags
# Note: Configuration is already in pyproject.toml, but we can override here
pytest \
    --cov=sample_project \
    --cov-report=html \
    --cov-report=term-missing \
    --cov-report=xml \
    --verbose \
    tests/

# Capture exit code
EXIT_CODE=$?

echo ""
echo "========================================="
echo "Test Execution Complete"
echo "========================================="
echo ""

if [ $EXIT_CODE -eq 0 ]; then
    echo "✓ All tests passed successfully!"
    echo ""
    echo "Coverage Reports Generated:"
    echo "  - HTML: htmlcov/index.html"
    echo "  - Terminal: (shown above)"
    echo "  - XML: coverage.xml"
    echo ""
    echo "To view HTML coverage report:"
    echo "  open htmlcov/index.html"
    echo ""
else
    echo "✗ Test execution failed with exit code: $EXIT_CODE"
    echo ""
    echo "Please review the test output above for details."
    echo ""
    exit $EXIT_CODE
fi

exit 0
