# Test Execution and Coverage Analysis Guide

This document provides comprehensive instructions for executing the Python test suite with coverage reporting and validating all functionality.

## Quick Start

### Prerequisites

Ensure you have the required testing dependencies installed:

```bash
pip install pytest pytest-cov
```

### Run Tests with Coverage

**Option 1: Use the provided script (recommended)**

```bash
chmod +x run_tests.sh
./run_tests.sh
```

**Option 2: Run pytest directly**

```bash
pytest --cov=sample_project --cov-report=html --cov-report=term --cov-report=xml
```

**Option 3: Use pyproject.toml defaults**

```bash
pytest
```

The `pyproject.toml` file already contains the coverage configuration in `[tool.pytest.ini_options]`.

---

## Test Suite Structure

The test suite provides comprehensive coverage for all Python modules:

### Source Modules → Test Modules Mapping

| Source Module | Test Module | Functions/Classes Tested |
|---------------|-------------|--------------------------|
| `sample_project.app` | `tests.test_app` | main(), single(), double_(), vector(), primes(), sort() |
| `sample_project.control.single` | `tests.control.test_single` | sum_range(), max_array(), sum_modulus() |
| `sample_project.control.double` | `tests.control.test_double` | sum_square(), sum_triangle(), count_pairs(), count_duplicates(), sum_matrix() |
| `sample_project.datastructures.vector` | `tests.datastructures.test_vector` | modify_vector(), search_vector(), sort_vector(), reverse_vector(), rotate_vector(), merge_vectors() |
| `sample_project.datastructures.linked_list` | `tests.datastructures.test_linked_list` | shuffle(), slice_list() |
| `sample_project.algorithms.primes` | `tests.algorithms.test_primes` | is_prime(), sum_primes(), prime_factors(), generate_sieve(), get_all_primes_up_to(), sum_primes_using_sieve() |
| `sample_project.algorithms.sort` | `tests.algorithms.test_sort` | sort_vector(), dutch_flag_partition(), max_n() |
| `sample_project.generator.vector_gen` | `tests.generator.test_vector_gen` | generate_vector() |
| `sample_project.strings.operations` | `tests.strings.test_operations` | Strops.reverse(), Strops.is_palindrome() |

**Total Coverage:**
- **9 Source Modules** (including `__init__.py` files)
- **9 Test Modules**
- **30+ Functions/Methods** tested
- **250+ Test Cases**

---

## Test Categories

The test suite includes comprehensive coverage across multiple categories:

### 1. **Basic Functionality Tests**
- Verify core algorithm correctness
- Test expected outputs for typical inputs
- Validate mathematical operations

### 2. **Edge Case Tests**
- Empty inputs (empty lists, empty strings, zero values)
- Single element inputs
- Boundary values (minimum/maximum valid values)
- Special values (None, negative numbers, duplicates)

### 3. **Error Handling Tests**
- `TypeError` for None/null inputs
- `ValueError` for invalid parameters (negative values, out-of-range)
- `IndexError` scenarios
- Validation error messages

### 4. **Immutability Tests**
- Verify functions that should create new objects don't modify originals
- Test reference equality vs value equality

### 5. **Randomness/Statistical Tests**
- For `shuffle()` and `generate_vector()`
- Verify distribution properties
- Check for expected variety in random outputs

### 6. **Performance Validation Tests**
- Large input handling (100+ elements)
- Scalability verification

---

## Coverage Expectations

### Target Metrics

Based on the comprehensive test suite:

| Metric | Target | Notes |
|--------|--------|-------|
| **Line Coverage** | ≥ 90% | All main code paths tested |
| **Branch Coverage** | ≥ 85% | Most conditional branches tested |
| **Function Coverage** | 100% | All public functions have tests |

### Expected Coverage by Module

| Module | Expected Line Coverage | Notes |
|--------|------------------------|-------|
| `app.py` | ~80-90% | Demo/smoke tests, not all output paths |
| `control.single` | ~95-100% | Comprehensive tests with error handling |
| `control.double` | ~95-100% | Comprehensive tests with error handling |
| `datastructures.vector` | ~95-100% | All functions tested with edge cases |
| `datastructures.linked_list` | ~90-95% | Statistical tests for randomness |
| `algorithms.primes` | ~95-100% | Comprehensive mathematical validation |
| `algorithms.sort` | ~95-100% | All sorting variants tested |
| `generator.vector_gen` | ~95-100% | Boundary and randomness tests |
| `strings.operations` | ~95-100% | Known bug test included |

### Lines Intentionally Not Covered

Some lines may intentionally have lower coverage:

1. **Debug/logging code** - Not always executed in tests
2. **`if __name__ == "__main__"`** - Entry point blocks
3. **Exception handling for system errors** - File I/O, OS errors
4. **Defensive assertions** - Type hints handled by mypy

---

## Interpreting Coverage Reports

### HTML Coverage Report

After running tests, open `htmlcov/index.html` in a browser:

```bash
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows
```

**What to look for:**

1. **Overall Coverage Percentage** - Should be ≥90%
2. **Module-by-Module Breakdown** - Identify low-coverage modules
3. **Red Lines** - Uncovered code (click module names to see details)
4. **Yellow Lines** - Partially covered branches
5. **Green Lines** - Fully covered code

### Terminal Coverage Report

The terminal output shows:

```
Name                                       Stmts   Miss  Cover   Missing
------------------------------------------------------------------------
src/sample_project/__init__.py                 0      0   100%
src/sample_project/algorithms/__init__.py      0      0   100%
src/sample_project/algorithms/primes.py       45      2    96%   23, 67
...
------------------------------------------------------------------------
TOTAL                                        450     18    96%
```

**Key Columns:**
- **Stmts**: Total statements in file
- **Miss**: Uncovered statements
- **Cover**: Coverage percentage
- **Missing**: Line numbers not covered

### XML Coverage Report

The `coverage.xml` file can be used by CI/CD tools or coverage tracking services.

---

## Validation Checklist

### Verification Checklist

After running tests with coverage, verify:

- [ ] **All tests pass** - No failures or errors
- [ ] **Coverage ≥ 90%** - Meets target
- [ ] **All source modules tested** - Every `.py` file has corresponding tests
- [ ] **Error handling tested** - TypeError, ValueError scenarios covered
- [ ] **Edge cases tested** - Empty inputs, None values, boundary conditions
- [ ] **Algorithm correctness** - Expected outputs are correct
- [ ] **Immutability preserved** - Functions that shouldn't modify inputs don't

### Known Issues

Based on `CRITICAL_BUGS.md`, the following test may fail:

**Test:** `tests.strings.test_operations::test_is_palindrome_empty_string_should_return_true`

This test verifies Bug #1 (if it still exists). If this test **passes**, the bug has been fixed. If it **fails**, the bug still exists and requires fixing.

---

## Success Criteria

The test execution is considered successful when:

✅ **All tests pass** - No failures, no errors  
✅ **Coverage ≥ 90%** - Line coverage meets or exceeds target  
✅ **No critical functionality untested** - All public APIs have tests  
✅ **Edge cases covered** - Empty inputs, None, boundaries tested  
✅ **Error handling validated** - Exception scenarios tested  
✅ **Performance validated** - Large inputs handled correctly  

---

## Failure Investigation

If tests fail or coverage is insufficient:

### Test Failures

1. **Read the failure message** - pytest provides detailed output
2. **Check the specific test** - Review test expectations
3. **Verify expected behavior** - Check function documentation
4. **Run single test for debugging**:
   ```bash
   pytest tests/path/to/test_file.py::test_function_name -v
   ```

### Low Coverage

1. **Review HTML report** - Identify uncovered lines
2. **Determine if coverage gap is intentional** - Debug code, defensive checks
3. **Add missing tests if needed** - Follow existing test patterns
4. **Document coverage gaps** - Justify intentionally uncovered code

### Common Issues

- **Import errors** - Ensure `src/` is in PYTHONPATH
- **Missing dependencies** - Install with `pip install -r requirements.txt`
- **Permission errors** - Make scripts executable with `chmod +x`

---

## Continuous Integration

For CI/CD integration:

```yaml
# Example GitHub Actions workflow
- name: Run tests with coverage
  run: |
    pip install pytest pytest-cov
    pytest --cov=sample_project --cov-report=xml --cov-report=term
    
- name: Upload coverage
  uses: codecov/codecov-action@v3
  with:
    file: ./coverage.xml
```

---

## Additional Resources

- **pytest documentation**: https://docs.pytest.org/
- **pytest-cov documentation**: https://pytest-cov.readthedocs.io/
- **Coverage.py documentation**: https://coverage.readthedocs.io/
- **Project bugs**: See `CRITICAL_BUGS.md`

---

## Summary

This test suite provides comprehensive validation of all Python functionality. With 250+ test cases covering functionality, edge cases, error handling, and performance, the test suite ensures correctness and maintains code quality standards.

**Next Steps:**
1. Run `./run_tests.sh`
2. Review coverage report at `htmlcov/index.html`
3. Verify ≥90% coverage achieved
4. Document any gaps or failures
5. Proceed to type checking validation (mypy)
