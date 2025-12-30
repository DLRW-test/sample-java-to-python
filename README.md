# Sample Project

A comprehensive Python sample project demonstrating fundamental algorithms, data structures, control flow patterns, and string manipulation techniques. This project serves as an educational resource and reference implementation for common programming concepts in Python 3.10+.

## Table of Contents

- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage Examples](#usage-examples)
- [Running the Demo](#running-the-demo)
- [Testing](#testing)
- [Development Tools](#development-tools)
- [Project Structure](#project-structure)

## Project Overview

This project showcases practical implementations of:

- **Algorithms**: Sorting (quicksort, Dutch flag partition), prime number operations (Sieve of Eratosthenes), heap-based selection
- **Data Structures**: Vector (list) operations, linked list implementation
- **Control Flow**: Single-loop and double-loop patterns for common computational tasks
- **String Operations**: Reversal and palindrome detection
- **Generators**: Random data generation utilities

Each module is fully type-annotated, tested, and documented with docstrings following Python best practices.

## Requirements

- **Python**: 3.10 or higher
- **Build System**: setuptools (specified in pyproject.toml)
- **Development Tools**: pytest, pytest-cov, mypy, black, ruff

No runtime dependencies are required for the core library - it uses only Python standard library modules.

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd sample-project
```

### 2. Create a Virtual Environment

**On Linux/macOS:**
```bash
python -m venv venv
source venv/bin/activate
```

**On Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

### 3. Install the Package

Install the package in editable mode with development dependencies:

```bash
pip install -e .
```

For development work, also install the development tools:

```bash
pip install pytest pytest-cov mypy black ruff
```

## Usage Examples

### Algorithms Module

**Sorting and Partitioning:**

```python
from sample_project.algorithms import sort

# Sort a list
data = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_data = sort.sort_vector(data)
print(sorted_data)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Dutch flag partition (three-way partitioning)
data = [3, 5, 2, 6, 8, 1, 0, 5, 5]
partitioned = sort.dutch_flag_partition(data, 5)
print(partitioned)  # [3, 2, 1, 0, 5, 5, 5, 6, 8]

# Find N largest elements
data = [3, 1, 4, 1, 5, 9, 2, 6]
largest_three = sort.max_n(data, 3)
print(largest_three)  # [9, 6, 5]
```

**Prime Number Operations:**

```python
from sample_project.algorithms import primes

# Check if a number is prime
print(primes.is_prime(17))  # True
print(primes.is_prime(4))   # False

# Sum all primes less than n
print(primes.sum_primes(10))  # 17 (2 + 3 + 5 + 7)

# Get all primes up to n
print(primes.get_all_primes_up_to(20))  # [2, 3, 5, 7, 11, 13, 17, 19]

# Find prime factors
print(primes.prime_factors(60))  # [2, 2, 3, 5]
```

### Control Flow Module

**Single-Loop Operations:**

```python
from sample_project.control import single

# Sum of range 1 to n-1
print(single.sum_range(10))  # 45

# Find maximum in array
print(single.max_array([1, 5, 3, 9, 2]))  # 9

# Sum of multiples of m less than n
print(single.sum_modulus(100, 3))  # 1683
```

**Double-Loop Operations:**

```python
from sample_project.control import double

# Sum of squares: sum of i*j for i,j in [1, n)
print(double.sum_square(10))  # 2025

# Sum of triangle: sum where j <= i
print(double.sum_triangle(10))  # 165

# Count duplicate pairs in array
print(double.count_pairs([1, 2, 3, 2, 4, 2]))  # 3

# Count duplicates between two arrays
print(double.count_duplicates([1, 2, 3], [2, 3, 4]))  # 2
```

### Data Structures Module

**Vector (List) Operations:**

```python
from sample_project.datastructures import vector

# Modify vector (add 1 to each element)
data = [1, 2, 3, 4, 5]
modified = vector.modify_vector(data.copy())
print(modified)  # [2, 3, 4, 5, 6]

# Search for value indices
data = [1, 2, 3, 2, 4]
indices = vector.search_vector(data, 2)
print(indices)  # [1, 3]

# Sort vector
sorted_data = vector.sort_vector([3, 1, 4, 1, 5])
print(sorted_data)  # [1, 1, 3, 4, 5]

# Reverse vector
reversed_data = vector.reverse_vector([1, 2, 3, 4, 5])
print(reversed_data)  # [5, 4, 3, 2, 1]

# Rotate vector left by n positions
rotated = vector.rotate_vector([1, 2, 3, 4, 5], 2)
print(rotated)  # [3, 4, 5, 1, 2]

# Merge two vectors
merged = vector.merge_vectors([1, 2, 3], [4, 5, 6])
print(merged)  # [1, 2, 3, 4, 5, 6]
```

### String Operations Module

```python
from sample_project.strings.operations import Strops

strops = Strops()

# Reverse a string
reversed_str = strops.reverse("hello")
print(reversed_str)  # "olleh"

# Check if palindrome
print(strops.is_palindrome("racecar"))  # True
print(strops.is_palindrome("hello"))    # False
```

### Generator Module

```python
from sample_project.generator import vector_gen

# Generate random vector of integers
random_vec = vector_gen.generate_vector(10, 0, 100)
print(random_vec)  # Random list of 10 integers between 0 and 100
```

## Running the Demo

The project includes a demo application that showcases all functionality:

```bash
python -m sample_project.app
```

This will execute demonstrations of:
- Single-loop control flow operations
- Double-loop control flow operations
- Vector manipulation
- Prime number algorithms
- Sorting and partitioning

**Expected output:**
```
SingleForLoop
-------------
SumRange(10): 45
MaxArray([1, 2, 3, 4, 5]): 5
SumModulus(100, 3): 1683

DoubleForLoop
-------------
SumSquare(10): 2025
...
```

## Testing

The project uses `pytest` for testing with comprehensive coverage reporting.

### Installation Testing

Before running the test suite, verify the package installs correctly:

```bash
# Run automated installation test
chmod +x test_installation.sh
./test_installation.sh

# Or validate CLI output manually
python validate_cli_output.py
```

See **[INSTALLATION_TEST.md](INSTALLATION_TEST.md)** for detailed installation testing documentation.

### Run All Tests

```bash
pytest
```

### Run Tests with Coverage Report

```bash
pytest --cov=sample_project --cov-report=html
```

This generates an HTML coverage report in the `htmlcov/` directory.

### View Coverage Report

After running tests with coverage:

```bash
# On Linux/macOS
open htmlcov/index.html

# On Windows
start htmlcov/index.html
```

### Run Specific Test Files

```bash
# Test a specific module
pytest tests/algorithms/test_sort.py

# Test a specific function
pytest tests/algorithms/test_sort.py::test_sort_vector
```

### Common Pytest Options

```bash
# Verbose output
pytest -v

# Stop at first failure
pytest -x

# Show print statements
pytest -s

# Run only tests matching a pattern
pytest -k "prime"
```

## Development Tools

This project uses modern Python development tools for code quality and consistency.

### Type Checking with Mypy

Run static type checking to catch type-related errors:

```bash
mypy src/sample_project
```

The project uses strict type checking with full type annotations. Configuration is in `pyproject.toml` under `[tool.mypy]`.

### Code Formatting with Black

Format code to maintain consistent style:

```bash
# Format all code
black src/ tests/

# Check formatting without making changes
black --check src/ tests/

# Show what would be changed
black --diff src/ tests/
```

Black is configured for Python 3.10+ with an 88-character line length.

### Linting with Ruff

Run fast Python linting to catch common issues:

```bash
# Lint all code
ruff check src/ tests/

# Auto-fix issues where possible
ruff check --fix src/ tests/

# Show all violations (including fixed)
ruff check --show-fixes src/ tests/
```

Ruff checks include:
- `E`, `F`: pycodestyle errors and pyflakes
- `I`: isort (import sorting)
- `UP`: pyupgrade (modern Python syntax)
- `B`: flake8-bugbear (common bugs)
- `C4`: flake8-comprehensions
- `SIM`: flake8-simplify

### Pre-commit Workflow

Before committing code, run:

```bash
# Format code
black src/ tests/

# Type check
mypy src/sample_project

# Lint
ruff check --fix src/ tests/

# Test
pytest
```

## Project Structure

```
sample-project/
├── src/
│   └── sample_project/           # Main package
│       ├── __init__.py
│       ├── app.py                # Demo application entry point
│       ├── algorithms/           # Algorithm implementations
│       │   ├── __init__.py
│       │   ├── primes.py         # Prime number operations
│       │   └── sort.py           # Sorting algorithms
│       ├── control/              # Control flow patterns
│       │   ├── __init__.py
│       │   ├── single.py         # Single-loop operations
│       │   └── double.py         # Double-loop operations
│       ├── datastructures/       # Data structure implementations
│       │   ├── __init__.py
│       │   ├── vector.py         # List operations
│       │   └── linked_list.py    # Linked list implementation
│       ├── generator/            # Data generators
│       │   ├── __init__.py
│       │   └── vector_gen.py     # Random vector generation
│       └── strings/              # String manipulation
│           ├── __init__.py
│           └── operations.py     # String operations class
├── tests/                        # Test suite (mirrors src structure)
│   ├── __init__.py
│   ├── test_app.py               # App module tests
│   ├── algorithms/               # Algorithm tests
│   ├── control/                  # Control flow tests
│   ├── datastructures/           # Data structure tests
│   ├── generator/                # Generator tests
│   └── strings/                  # String operation tests
├── pyproject.toml                # Project configuration and dependencies
├── README.md                     # This file
└── docs/                         # Additional documentation
```

### Key Files

- **`pyproject.toml`**: Project metadata, build configuration, and tool settings (black, mypy, ruff, pytest)
- **`src/sample_project/app.py`**: Main entry point demonstrating all functionality
- **`tests/`**: Complete test suite with unit tests for all modules

### Module Responsibilities

- **algorithms/**: Computational algorithms (sorting, primes, selection)
- **control/**: Control flow patterns and loop-based computations
- **datastructures/**: Data structure implementations and utilities
- **generator/**: Random data generation for testing and demos
- **strings/**: String manipulation operations

---

## Contributing

When contributing to this project:

1. Ensure all tests pass: `pytest`
2. Maintain type annotations: `mypy src/sample_project`
3. Format code with Black: `black src/ tests/`
4. Lint with Ruff: `ruff check src/ tests/`
5. Add tests for new functionality
6. Update docstrings following existing patterns

## License

MIT License - See LICENSE file for details
