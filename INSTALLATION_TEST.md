# Installation and CLI Entry Point Testing

This document provides comprehensive guidance for testing the package installation process and CLI entry point to ensure the project is properly pip-installable and executable.

## Overview

The installation testing validates:

- ✅ Package installation via `pip install -e .`
- ✅ Dependency resolution
- ✅ Module import resolution
- ✅ CLI entry point execution (`python -m sample_project.app`)
- ✅ Console output validation against Java version's demo behavior

## Quick Start

### Automated Testing (Recommended)

Run the comprehensive installation test script:

```bash
chmod +x test_installation.sh
./test_installation.sh
```

This script performs all validation steps automatically and provides a detailed report.

### Manual Validation

Use the Python validation script after installation:

```bash
python validate_cli_output.py
```

## Test Components

### 1. Installation Test Script (`test_installation.sh`)

**Purpose**: Comprehensive end-to-end installation validation

**What it does**:
1. Creates a clean virtual environment (`test_venv`)
2. Activates the virtual environment
3. Upgrades pip to the latest version
4. Installs the package in editable mode: `pip install -e .`
5. Verifies the package is installed correctly
6. Tests basic package import: `import sample_project`
7. Tests individual module imports (all submodules)
8. Executes the CLI entry point: `python -m sample_project.app`
9. Validates console output against expected patterns
10. Generates a detailed test report

**Usage**:
```bash
./test_installation.sh
```

**Expected Output**:
```
=========================================
Package Installation and CLI Test
=========================================

Step 1: Cleaning up existing test environment...
Step 2: Creating clean virtual environment...
Step 3: Activating virtual environment...
Step 4: Upgrading pip...
Step 5: Installing package in editable mode...
...
=========================================
✓ ALL INSTALLATION TESTS PASSED
=========================================
```

### 2. CLI Output Validator (`validate_cli_output.py`)

**Purpose**: Detailed validation of CLI output

**What it does**:
1. Executes `python -m sample_project.app`
2. Captures stdout and stderr
3. Validates output against expected patterns from Java version
4. Generates a detailed validation report

**Usage**:
```bash
python validate_cli_output.py
```

**Expected Output**:
```
============================================================
CLI Entry Point Validation
============================================================

✓ CLI execution completed successfully

============================================================
CLI Output Validation Report
============================================================

✓ [REQUIRED] SingleForLoop
✓ [REQUIRED] SumRange(10): 45
✓ [REQUIRED] MaxArray([1, 2, 3, 4, 5]): 5
...

Results: 24/24 required patterns found

✓ ALL VALIDATIONS PASSED
============================================================
```

## Manual Testing Steps

If you prefer to test manually, follow these steps:

### Step 1: Create Clean Virtual Environment

```bash
python -m venv test_venv
```

### Step 2: Activate Virtual Environment

**Linux/macOS**:
```bash
source test_venv/bin/activate
```

**Windows**:
```cmd
test_venv\Scripts\activate
```

### Step 3: Upgrade pip

```bash
pip install --upgrade pip
```

### Step 4: Install Package in Editable Mode

```bash
pip install -e .
```

**Expected behavior**: Installation completes without errors.

### Step 5: Verify Installation

```bash
pip show sample_project
```

**Expected output**:
```
Name: sample_project
Version: 0.1.0
Location: /path/to/project/src
...
```

### Step 6: Test Basic Import

```bash
python -c "import sample_project"
```

**Expected behavior**: No output, no errors.

### Step 7: Test Individual Module Imports

```bash
python -c "from sample_project.control import single"
python -c "from sample_project.control import double"
python -c "from sample_project.datastructures import vector"
python -c "from sample_project.algorithms import primes"
python -c "from sample_project.algorithms import sort"
python -c "from sample_project.generator import vector_gen"
python -c "from sample_project.strings.operations import Strops"
```

**Expected behavior**: All imports succeed without errors.

### Step 8: Test CLI Entry Point

```bash
python -m sample_project.app
```

**Expected output**:
```
SingleForLoop
-------------
SumRange(10): 45
MaxArray([1, 2, 3, 4, 5]): 5
SumModulus(100, 3): 1683

DoubleForLoop
-------------
SumSquare(10): 2025
SumTriangle(10): 165
CountPairs([1, 2, 3, 4, 5, 2]): 3
CountDuplicates([1, 2, 3, 4, 5], [1, 3, 2, 4, 5]): 5

Vector
------
ModifyVector([...]): [...]
SearchVector([...], 5): ...
SortVector([...]): [...]
ReverseVector([...]): [...]
RotateVector([...], 3): [...]
MergeVectors([...], [...]): [...]

Primes
------
IsPrime(10): False
SumPrimes(10): 17
PrimeFactors(10): [2, 5]

Sort
------
SortVector([...]): [...]
DutchFlagPartition([...], 5): [...]
MaxN([...], 5): [...]
```

**Note**: Vector and Sort sections will have different values each run due to random data generation.

### Step 9: Deactivate Virtual Environment

```bash
deactivate
```

## Success Criteria

The installation testing is considered successful when:

✅ **Package Installation**: `pip install -e .` completes without errors  
✅ **Package Visibility**: `pip show sample_project` displays package information  
✅ **Basic Import**: `import sample_project` executes without errors  
✅ **Module Imports**: All individual module imports succeed  
✅ **CLI Execution**: `python -m sample_project.app` runs without errors  
✅ **Output Validation**: Console output contains all expected demo sections  
✅ **No Import Errors**: No `ModuleNotFoundError` or `ImportError` exceptions  
✅ **Function Execution**: All demo functions execute (single, double_, vector, primes, sort)  

## Expected Demo Functions

The CLI entry point (`app.py`) executes these demo functions in sequence:

1. **single()**: Single-loop control flow operations
   - `sum_range(10)` → 45
   - `max_array([1, 2, 3, 4, 5])` → 5
   - `sum_modulus(100, 3)` → 1683

2. **double_()**: Double-loop control flow operations
   - `sum_square(10)` → 2025
   - `sum_triangle(10)` → 165
   - `count_pairs([1, 2, 3, 4, 5, 2])` → 3
   - `count_duplicates([1, 2, 3, 4, 5], [1, 3, 2, 4, 5])` → 5

3. **vector()**: Vector manipulation operations (randomized data)
   - `modify_vector()`: Add 1 to each element
   - `search_vector()`: Find indices of value 5
   - `sort_vector()`: Sort the vector
   - `reverse_vector()`: Reverse the vector
   - `rotate_vector()`: Rotate left by 3 positions
   - `merge_vectors()`: Merge two vectors

4. **primes()**: Prime number operations
   - `is_prime(10)` → False
   - `sum_primes(10)` → 17 (sum of 2, 3, 5, 7)
   - `prime_factors(10)` → [2, 5]

5. **sort()**: Sorting and partitioning operations (randomized data)
   - `sort_vector()`: In-place quicksort
   - `dutch_flag_partition()`: Three-way partition around pivot
   - `max_n()`: Find N largest elements

## Troubleshooting

### Import Errors

**Problem**: `ModuleNotFoundError: No module named 'sample_project'`

**Solution**:
1. Ensure you've installed the package: `pip install -e .`
2. Verify you're in the correct virtual environment
3. Check that `src/sample_project` exists and contains `__init__.py`
4. Verify `pyproject.toml` has correct `[tool.setuptools.packages.find]` configuration

### CLI Execution Errors

**Problem**: `python -m sample_project.app` fails

**Solution**:
1. Verify the package is installed: `pip show sample_project`
2. Check that `src/sample_project/app.py` exists
3. Test basic import first: `python -c "import sample_project.app"`
4. Check for syntax errors in `app.py`

### Missing Dependencies

**Problem**: Import errors for specific submodules

**Solution**:
1. Verify all `__init__.py` files exist in subdirectories
2. Check module structure matches package configuration
3. Reinstall the package: `pip install -e . --force-reinstall`

### Output Validation Failures

**Problem**: Validation script reports missing patterns

**Solution**:
1. Manually run `python -m sample_project.app` and review output
2. Check that all demo functions are being called in `main()`
3. Verify function implementations match expected behavior
4. Note: Vector/Sort sections use random data, so exact values will vary

## Comparison with Java Version

The Python implementation should produce functionally equivalent output to the Java version:

| Section | Java Output | Python Output | Notes |
|---------|-------------|---------------|-------|
| SumRange(10) | 45 | 45 | Identical |
| MaxArray([1,2,3,4,5]) | 5 | 5 | Identical |
| SumModulus(100, 3) | 1683 | 1683 | Identical |
| SumSquare(10) | 2025 | 2025 | Identical |
| SumTriangle(10) | 165 | 165 | Identical |
| IsPrime(10) | false | False | Python boolean |
| SumPrimes(10) | 17 | 17 | Identical |
| PrimeFactors(10) | [2, 5] | [2, 5] | Identical |
| Vector operations | Random | Random | Values differ, behavior same |
| Sort operations | Random | Random | Values differ, behavior same |

## Configuration Files

### pyproject.toml

The package configuration is defined in `pyproject.toml`:

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "sample_project"
version = "0.1.0"
requires-python = ">=3.10"

[tool.setuptools.packages.find]
where = ["src"]
```

**Key points**:
- Package name: `sample_project`
- Source location: `src/` directory
- Minimum Python version: 3.10
- Build backend: setuptools

### Package Structure

```
sample_project/
├── src/
│   └── sample_project/
│       ├── __init__.py
│       ├── app.py                    # CLI entry point
│       ├── algorithms/
│       │   ├── __init__.py
│       │   ├── primes.py
│       │   └── sort.py
│       ├── control/
│       │   ├── __init__.py
│       │   ├── single.py
│       │   └── double.py
│       ├── datastructures/
│       │   ├── __init__.py
│       │   ├── vector.py
│       │   └── linked_list.py
│       ├── generator/
│       │   ├── __init__.py
│       │   └── vector_gen.py
│       └── strings/
│           ├── __init__.py
│           └── operations.py
├── tests/
│   └── ...
├── pyproject.toml
├── test_installation.sh             # Installation test script
└── validate_cli_output.py           # CLI output validator
```

## CI/CD Integration

These test scripts can be integrated into CI/CD pipelines:

```yaml
# Example GitHub Actions workflow
- name: Test Installation
  run: |
    chmod +x test_installation.sh
    ./test_installation.sh

- name: Validate CLI Output
  run: |
    python validate_cli_output.py
```

## Additional Resources

- **README.md**: General project documentation and usage examples
- **TEST_EXECUTION_GUIDE.md**: Guide for running the test suite
- **pyproject.toml**: Package configuration
- **app.py**: CLI entry point source code

## Maintenance

To update the validation tests when functionality changes:

1. **Update `test_installation.sh`**: Modify `EXPECTED_SECTIONS` array
2. **Update `validate_cli_output.py`**: Modify `EXPECTED_PATTERNS` list
3. **Update this documentation**: Reflect changes in expected output
4. **Update README.md**: Keep usage examples synchronized

## Summary

The installation testing ensures the Python implementation is:

- **Installable**: Can be installed via pip in a clean environment
- **Importable**: All modules resolve correctly
- **Executable**: CLI entry point runs without errors
- **Functional**: Output matches expected behavior from Java version
- **Maintainable**: Comprehensive validation catches regressions

Both automated scripts (`test_installation.sh` and `validate_cli_output.py`) provide thorough validation with detailed reporting to ensure the package meets all installation and execution requirements.
