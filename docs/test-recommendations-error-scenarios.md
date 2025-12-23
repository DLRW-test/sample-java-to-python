# Test Improvement Recommendations for Error Scenarios

**Project:** Java Algorithms & Data Structures Library  
**Document Version:** 1.0  
**Date:** 2024  
**Purpose:** Comprehensive testing strategy for error handling coverage using JUnit 5  
**Audience:** Code quality exercise demonstrating industry-standard testing best practices

---

## Executive Summary

This document provides **actionable recommendations** for implementing comprehensive error scenario testing across the test suite. Based on the error handling audit that identified **28 vulnerabilities** (5 CRITICAL, 15 HIGH, 8 MEDIUM) and the error handling recommendations, this guide establishes:

- ✅ **JUnit 5 assertThrows() patterns** for exception testing
- ✅ **Test naming conventions** following industry best practices
- ✅ **Test organization strategy** separating error tests from happy path tests
- ✅ **Specific test cases** mapped to all 28 identified vulnerabilities
- ✅ **Edge case testing guidance** covering null, empty, boundary, and negative scenarios
- ✅ **Coverage goals** targeting 100% validation logic coverage
- ✅ **Error message verification** techniques for meaningful exceptions

### Current State Assessment

**Critical Finding:** **ZERO exception tests currently exist in the test suite**

**Evidence:**
- ❌ **No usage of `assertThrows()`** in any test class
- ❌ **No exception testing** for any method accepting null/invalid inputs
- ❌ **Only happy path coverage** - all tests assume valid inputs
- ❌ **Assertions used:** Only `assertEquals()`, `assertTrue()`, `assertFalse()`, `assertSame()`, `assertNotSame()`

**Test Coverage Gap:**
- **28 error handling paths** identified but **0 tested** (0% coverage)
- **All public methods** accept potentially invalid inputs but **none validate** or test validation
- **Critical vulnerabilities** (maxArray null/empty, sumModulus divide-by-zero) completely untested

**Impact:**
- Error handling code (once implemented) will have **zero test coverage**
- Risk of **silent regressions** when adding validation logic
- **No verification** that exceptions provide meaningful error messages
- **Cannot verify** fail-fast behavior

---

## Table of Contents

1. [JUnit 5 assertThrows() Patterns](#junit-5-assertthrows-patterns)
2. [Test Naming Conventions](#test-naming-conventions)
3. [Test Organization Strategy](#test-organization-strategy)
4. [Specific Test Cases by Class](#specific-test-cases-by-class)
   - [SingleTest.java](#singletestjava)
   - [DoubleTest.java](#doubletestjava)
   - [DsVectorTest.java](#dsvectortestjava)
   - [DsLinkedListTest.java](#dslinkedlisttestjava)
   - [PrimesTest.java](#primestestjava)
   - [SortTest.java](#sorttestjava)
   - [StropsTest.java](#stropstestjava)
   - [GenVectorTest.java](#genvectortestjava)
   - [AppTest.java](#apptestjava)
5. [Edge Case Testing Guidance](#edge-case-testing-guidance)
6. [Coverage Goals](#coverage-goals)
7. [Error Message Verification](#error-message-verification)
8. [Implementation Roadmap](#implementation-roadmap)

---

## JUnit 5 assertThrows() Patterns

### Basic Pattern

```java
import static org.junit.jupiter.api.Assertions.assertThrows;

@Test
public void testMethodName_whenInvalidInput_throwsExpectedException() {
    assertThrows(ExpectedException.class, () -> {
        ClassName.methodName(invalidInput);
    });
}
```

### Pattern with Exception Message Verification

```java
@Test
public void testMethodName_whenInvalidInput_throwsExceptionWithMessage() {
    Exception exception = assertThrows(ExpectedException.class, () -> {
        ClassName.methodName(invalidInput);
    });
    
    assertTrue(exception.getMessage().contains("expected message fragment"));
    // Or more specific:
    assertEquals("Expected exact message", exception.getMessage());
}
```

### Pattern for Multiple Parameters

```java
@Test
public void testMethodName_whenFirstParamNull_throwsNPE() {
    assertThrows(NullPointerException.class, () -> {
        ClassName.methodName(null, validParam2);
    });
}

@Test
public void testMethodName_whenSecondParamNull_throwsNPE() {
    assertThrows(NullPointerException.class, () -> {
        ClassName.methodName(validParam1, null);
    });
}
```

### Pattern for Boundary Conditions

```java
@Test
public void testMethodName_whenNegativeIndex_throwsIllegalArgument() {
    assertThrows(IllegalArgumentException.class, () -> {
        ClassName.methodName(validParam, -1);
    });
}

@Test
public void testMethodName_whenIndexTooLarge_throwsIndexOutOfBounds() {
    ArrayList<Integer> list = new ArrayList<>(Arrays.asList(1, 2, 3));
    assertThrows(IndexOutOfBoundsException.class, () -> {
        ClassName.methodName(list, 10);
    });
}
```

### Pattern Using @DisplayName for Readability

```java
@Test
@DisplayName("maxArray() should throw NullPointerException when array is null")
public void testMaxArray_whenNull_throwsNPE() {
    assertThrows(NullPointerException.class, () -> {
        Single.maxArray(null);
    });
}
```

### Pattern for Division by Zero

```java
@Test
public void testSumModulus_whenModulusZero_throwsArithmeticException() {
    Exception exception = assertThrows(ArithmeticException.class, () -> {
        Single.sumModulus(10, 0);
    });
    
    assertTrue(exception.getMessage().contains("zero") || 
               exception.getMessage().contains("cannot be zero"),
               "Exception message should mention zero divisor");
}
```

### Pattern Organized with @Nested

```java
@Nested
@DisplayName("Error Scenario Tests")
class ErrorScenarioTests {
    
    @Test
    @DisplayName("Null input throws NullPointerException")
    public void testNullInput() {
        assertThrows(NullPointerException.class, () -> {
            ClassName.methodName(null);
        });
    }
    
    @Test
    @DisplayName("Empty input throws IllegalArgumentException")
    public void testEmptyInput() {
        assertThrows(IllegalArgumentException.class, () -> {
            ClassName.methodName(new int[0]);
        });
    }
}
```

---

## Test Naming Conventions

### Recommended Convention

**Format:** `test<MethodName>_when<Condition>_throws<ExceptionType>`

**Examples:**
```java
testMaxArray_whenNull_throwsNPE()
testMaxArray_whenEmpty_throwsIllegalArgument()
testSumModulus_whenModulusZero_throwsArithmeticException()
testRotateVector_whenNegativeRotation_throwsIllegalArgument()
testRotateVector_whenRotationExceedsSize_throwsIndexOutOfBounds()
testSlice_whenStartNegative_throwsIndexOutOfBounds()
testSlice_whenEndExceedsSize_throwsIndexOutOfBounds()
testSlice_whenStartGreaterThanEnd_throwsIllegalArgument()
```

### Alternative Convention (when using @DisplayName)

**Format:** Descriptive sentence starting with method name

**Examples:**
```java
@DisplayName("maxArray() throws NullPointerException when array is null")
@DisplayName("maxArray() throws IllegalArgumentException when array is empty")
@DisplayName("sumModulus() throws ArithmeticException when modulus is zero")
@DisplayName("rotateVector() throws IllegalArgumentException when rotation is negative")
```

### Grouping Error Tests

Use `@Nested` classes to separate error tests from happy path tests:

```java
public class SingleTest {
    
    // Happy path tests (existing)
    @Test
    public void testSumRange() { /* ... */ }
    
    // Error scenario tests (new)
    @Nested
    @DisplayName("maxArray() Error Scenarios")
    class MaxArrayErrorTests {
        @Test
        public void whenNull_throwsNPE() { /* ... */ }
        
        @Test
        public void whenEmpty_throwsIllegalArgument() { /* ... */ }
    }
    
    @Nested
    @DisplayName("sumModulus() Error Scenarios")
    class SumModulusErrorTests {
        @Test
        public void whenModulusZero_throwsArithmeticException() { /* ... */ }
        
        @Test
        public void whenModulusNegative_throwsIllegalArgument() { /* ... */ }
    }
}
```

---

## Test Organization Strategy

### 1. Separate Error Tests from Happy Path Tests

**Recommendation:** Add error scenario tests as new `@Nested` classes at the end of existing test files.

**Rationale:**
- Maintains backward compatibility with existing tests
- Clear separation of concerns
- Easy to identify coverage gaps
- Allows running error tests separately if needed

**Example Structure:**
```java
public class DsVectorTest {
    // ==================== Existing Happy Path Tests ====================
    @Test
    public void testModifyVector_EmptyVector() { /* ... */ }
    
    @Test
    public void testModifyVector_SingleElement() { /* ... */ }
    
    // ... more happy path tests ...
    
    // ==================== Error Scenario Tests ====================
    
    @Nested
    @DisplayName("modifyVector() Error Scenarios")
    class ModifyVectorErrorTests {
        @Test
        @DisplayName("Null vector throws NullPointerException")
        public void whenVectorNull_throwsNPE() {
            assertThrows(NullPointerException.class, () -> {
                DsVector.modifyVector(null);
            });
        }
    }
    
    @Nested
    @DisplayName("rotateVector() Error Scenarios")
    class RotateVectorErrorTests {
        @Test
        public void whenVectorNull_throwsNPE() { /* ... */ }
        
        @Test
        public void whenRotationNegative_throwsIllegalArgument() { /* ... */ }
        
        @Test
        public void whenRotationExceedsSize_throwsIndexOutOfBounds() { /* ... */ }
    }
}
```

### 2. Group Related Error Tests

**Group by method:** Each method gets its own `@Nested` class for error tests

**Group by error type within method:** If a method has many error cases, sub-group by:
- Null/reference validation
- Range validation
- Boundary validation

**Example:**
```java
@Nested
@DisplayName("slice() Error Scenarios")
class SliceErrorTests {
    
    @Nested
    @DisplayName("Null/Reference Validation")
    class NullValidationTests {
        @Test
        public void whenListNull_throwsNPE() { /* ... */ }
    }
    
    @Nested
    @DisplayName("Index Boundary Validation")
    class BoundaryValidationTests {
        @Test
        public void whenStartNegative_throwsIndexOutOfBounds() { /* ... */ }
        
        @Test
        public void whenEndExceedsSize_throwsIndexOutOfBounds() { /* ... */ }
        
        @Test
        public void whenStartGreaterThanEnd_throwsIllegalArgument() { /* ... */ }
    }
}
```

### 3. Test Execution Order

**Recommendation:** Error tests should run AFTER happy path tests

**Rationale:**
- If basic functionality is broken, error handling tests will also fail
- Fail-fast on fundamental issues
- Easier debugging when tests fail

**Implementation:** Natural with `@Nested` classes added at end of file

---

## Specific Test Cases by Class

### SingleTest.java

**Current State:** 3 test methods, all happy path only

**Vulnerabilities to Test:**
1. `maxArray(int[] arr)` - CRITICAL: null array, empty array
2. `sumModulus(int n, int m)` - CRITICAL: division by zero (m=0)
3. `sumRange(int n)` - HIGH: negative input validation

#### Recommended New Tests (7 tests)

```java
@Nested
@DisplayName("maxArray() Error Scenarios")
class MaxArrayErrorTests {
    
    @Test
    @DisplayName("Null array throws NullPointerException")
    public void whenArrayNull_throwsNPE() {
        Exception exception = assertThrows(NullPointerException.class, () -> {
            Single.maxArray(null);
        });
        assertTrue(exception.getMessage().contains("null") || 
                   exception.getMessage().contains("Array"),
                   "Error message should mention null array");
    }
    
    @Test
    @DisplayName("Empty array throws IllegalArgumentException")
    public void whenArrayEmpty_throwsIllegalArgument() {
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            Single.maxArray(new int[0]);
        });
        assertTrue(exception.getMessage().contains("empty") || 
                   exception.getMessage().contains("length"),
                   "Error message should mention empty array");
    }
}

@Nested
@DisplayName("sumModulus() Error Scenarios")
class SumModulusErrorTests {
    
    @Test
    @DisplayName("Modulus zero throws ArithmeticException")
    public void whenModulusZero_throwsArithmeticException() {
        Exception exception = assertThrows(ArithmeticException.class, () -> {
            Single.sumModulus(10, 0);
        });
        assertTrue(exception.getMessage().contains("zero") || 
                   exception.getMessage().contains("cannot be zero"),
                   "Error message should mention division by zero");
    }
    
    @Test
    @DisplayName("Negative modulus throws IllegalArgumentException")
    public void whenModulusNegative_throwsIllegalArgument() {
        assertThrows(IllegalArgumentException.class, () -> {
            Single.sumModulus(10, -5);
        });
    }
    
    @Test
    @DisplayName("Negative n throws IllegalArgumentException")
    public void whenNNegative_throwsIllegalArgument() {
        assertThrows(IllegalArgumentException.class, () -> {
            Single.sumModulus(-1, 5);
        });
    }
}

@Nested
@DisplayName("sumRange() Error Scenarios")
class SumRangeErrorTests {
    
    @Test
    @DisplayName("Negative n throws IllegalArgumentException")
    public void whenNNegative_throwsIllegalArgument() {
        assertThrows(IllegalArgumentException.class, () -> {
            Single.sumRange(-1);
        });
    }
    
    @Test
    @DisplayName("Integer.MIN_VALUE throws IllegalArgumentException")
    public void whenNMinValue_throwsIllegalArgument() {
        assertThrows(IllegalArgumentException.class, () -> {
            Single.sumRange(Integer.MIN_VALUE);
        });
    }
}
```

**Test Count:**
- Existing: 3 happy path
- New error tests: 7
- Total: 10 tests
- Error coverage: 3/3 methods (100%)

---

### DoubleTest.java

**Current State:** 5 test methods, all happy path only

**Vulnerabilities to Test:**
1. `countPairs(int[] arr)` - HIGH: null array
2. `countDuplicates(int[] arr0, int[] arr1)` - HIGH: null arrays, length mismatch
3. `sumMatrix(int[][] arr)` - CRITICAL: null matrix, null rows, non-square matrix
4. `sumSquare(int n)` - HIGH: negative input
5. `sumTriangle(int n)` - HIGH: negative input

#### Recommended New Tests (12 tests)

```java
@Nested
@DisplayName("countPairs() Error Scenarios")
class CountPairsErrorTests {
    
    @Test
    public void whenArrayNull_throwsNPE() {
        assertThrows(NullPointerException.class, () -> {
            Double.countPairs(null);
        });
    }
    
    @Test
    public void whenArrayEmpty_returnsZero() {
        // Note: Empty array is valid, should return 0, not throw
        // This is a boundary test, not an error test
        assertEquals(0, Double.countPairs(new int[0]));
    }
}

@Nested
@DisplayName("countDuplicates() Error Scenarios")
class CountDuplicatesErrorTests {
    
    @Test
    public void whenFirstArrayNull_throwsNPE() {
        assertThrows(NullPointerException.class, () -> {
            Double.countDuplicates(null, new int[]{1, 2, 3});
        });
    }
    
    @Test
    public void whenSecondArrayNull_throwsNPE() {
        assertThrows(NullPointerException.class, () -> {
            Double.countDuplicates(new int[]{1, 2, 3}, null);
        });
    }
    
    @Test
    public void whenBothArraysNull_throwsNPE() {
        assertThrows(NullPointerException.class, () -> {
            Double.countDuplicates(null, null);
        });
    }
    
    @Test
    public void whenArrayLengthMismatch_throwsIllegalArgument() {
        assertThrows(IllegalArgumentException.class, () -> {
            Double.countDuplicates(new int[]{1, 2, 3}, new int[]{1, 2});
        });
    }
}

@Nested
@DisplayName("sumMatrix() Error Scenarios")
class SumMatrixErrorTests {
    
    @Test
    public void whenMatrixNull_throwsNPE() {
        assertThrows(NullPointerException.class, () -> {
            Double.sumMatrix(null);
        });
    }
    
    @Test
    public void whenMatrixEmpty_throwsIllegalArgument() {
        assertThrows(IllegalArgumentException.class, () -> {
            Double.sumMatrix(new int[0][0]);
        });
    }
    
    @Test
    public void whenRowNull_throwsNPE() {
        int[][] matrix = new int[3][];
        matrix[0] = new int[]{1, 2, 3};
        matrix[1] = null; // Null row
        matrix[2] = new int[]{7, 8, 9};
        
        assertThrows(NullPointerException.class, () -> {
            Double.sumMatrix(matrix);
        });
    }
    
    @Test
    public void whenMatrixNotSquare_throwsIllegalArgument() {
        // 2x3 matrix (not square)
        int[][] matrix = {{1, 2, 3}, {4, 5, 6}};
        
        assertThrows(IllegalArgumentException.class, () -> {
            Double.sumMatrix(matrix);
        });
    }
}

@Nested
@DisplayName("sumSquare() Error Scenarios")
class SumSquareErrorTests {
    
    @Test
    public void whenNNegative_throwsIllegalArgument() {
        assertThrows(IllegalArgumentException.class, () -> {
            Double.sumSquare(-1);
        });
    }
}

@Nested
@DisplayName("sumTriangle() Error Scenarios")
class SumTriangleErrorTests {
    
    @Test
    public void whenNNegative_throwsIllegalArgument() {
        assertThrows(IllegalArgumentException.class, () -> {
            Double.sumTriangle(-1);
        });
    }
}
```

**Test Count:**
- Existing: 5 happy path
- New error tests: 12
- Total: 17 tests
- Error coverage: 5/5 methods (100%)

---

### DsVectorTest.java

**Current State:** ~40+ test methods (comprehensive happy path coverage)

**Vulnerabilities to Test:**
1. `modifyVector(ArrayList<Integer> v)` - HIGH: null vector
2. `searchVector(ArrayList<Integer> v, int x)` - HIGH: null vector
3. `sortVector(ArrayList<Integer> v)` - HIGH: null vector
4. `reverseVector(ArrayList<Integer> v)` - HIGH: null vector
5. `rotateVector(ArrayList<Integer> v, int n)` - CRITICAL: null vector, negative rotation, rotation > size
6. `filterVector(ArrayList<Integer> v, int x)` - HIGH: null vector

#### Recommended New Tests (9 tests)

```java
// ==================== Error Scenario Tests ====================

@Nested
@DisplayName("modifyVector() Error Scenarios")
class ModifyVectorErrorTests {
    
    @Test
    public void whenVectorNull_throwsNPE() {
        assertThrows(NullPointerException.class, () -> {
            DsVector.modifyVector(null);
        });
    }
}

@Nested
@DisplayName("searchVector() Error Scenarios")
class SearchVectorErrorTests {
    
    @Test
    public void whenVectorNull_throwsNPE() {
        assertThrows(NullPointerException.class, () -> {
            DsVector.searchVector(null, 5);
        });
    }
}

@Nested
@DisplayName("sortVector() Error Scenarios")
class SortVectorErrorTests {
    
    @Test
    public void whenVectorNull_throwsNPE() {
        assertThrows(NullPointerException.class, () -> {
            DsVector.sortVector(null);
        });
    }
}

@Nested
@DisplayName("reverseVector() Error Scenarios")
class ReverseVectorErrorTests {
    
    @Test
    public void whenVectorNull_throwsNPE() {
        assertThrows(NullPointerException.class, () -> {
            DsVector.reverseVector(null);
        });
    }
}

@Nested
@DisplayName("rotateVector() Error Scenarios")
class RotateVectorErrorTests {
    
    @Test
    public void whenVectorNull_throwsNPE() {
        assertThrows(NullPointerException.class, () -> {
            DsVector.rotateVector(null, 2);
        });
    }
    
    @Test
    @DisplayName("Negative rotation throws IllegalArgumentException")
    public void whenRotationNegative_throwsIllegalArgument() {
        ArrayList<Integer> v = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
        
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            DsVector.rotateVector(v, -1);
        });
        
        assertTrue(exception.getMessage().contains("negative") || 
                   exception.getMessage().contains("cannot be negative"),
                   "Error message should mention negative rotation");
    }
    
    @Test
    @DisplayName("Rotation exceeding size throws IndexOutOfBoundsException")
    public void whenRotationExceedsSize_throwsIndexOutOfBounds() {
        ArrayList<Integer> v = new ArrayList<>(Arrays.asList(1, 2, 3));
        
        Exception exception = assertThrows(IndexOutOfBoundsException.class, () -> {
            DsVector.rotateVector(v, 10);
        });
        
        assertTrue(exception.getMessage().contains("exceeds") || 
                   exception.getMessage().contains("size"),
                   "Error message should mention size constraint");
    }
}

@Nested
@DisplayName("filterVector() Error Scenarios")
class FilterVectorErrorTests {
    
    @Test
    public void whenVectorNull_throwsNPE() {
        assertThrows(NullPointerException.class, () -> {
            DsVector.filterVector(null, 5);
        });
    }
}
```

**Test Count:**
- Existing: ~40 happy path
- New error tests: 9
- Total: ~49 tests
- Error coverage: 6/6 methods (100%)

---

### DsLinkedListTest.java

**Current State:** Comprehensive tests with @Nested organization

**Vulnerabilities to Test:**
1. `shuffle(LinkedList<Integer> l)` - HIGH: null list
2. `slice(LinkedList<Integer> l, int start, int end)` - CRITICAL: null list, negative start, end > size, start > end

#### Recommended New Tests (6 tests)

```java
@Nested
@DisplayName("shuffle() Error Scenarios")
class ShuffleErrorTests {
    
    @Test
    @DisplayName("Null list throws NullPointerException")
    public void whenListNull_throwsNPE() {
        assertThrows(NullPointerException.class, () -> {
            DsLinkedList.shuffle(null);
        });
    }
}

@Nested
@DisplayName("slice() Error Scenarios")
class SliceErrorTests {
    
    @Test
    @DisplayName("Null list throws NullPointerException")
    public void whenListNull_throwsNPE() {
        assertThrows(NullPointerException.class, () -> {
            DsLinkedList.slice(null, 0, 5);
        });
    }
    
    @Test
    @DisplayName("Negative start index throws IndexOutOfBoundsException")
    public void whenStartNegative_throwsIndexOutOfBounds() {
        LinkedList<Integer> list = new LinkedList<>(Arrays.asList(1, 2, 3, 4, 5));
        
        Exception exception = assertThrows(IndexOutOfBoundsException.class, () -> {
            DsLinkedList.slice(list, -1, 3);
        });
        
        assertTrue(exception.getMessage().contains("negative") || 
                   exception.getMessage().contains("Start"),
                   "Error message should mention negative start index");
    }
    
    @Test
    @DisplayName("End index exceeding size throws IndexOutOfBoundsException")
    public void whenEndExceedsSize_throwsIndexOutOfBounds() {
        LinkedList<Integer> list = new LinkedList<>(Arrays.asList(1, 2, 3));
        
        Exception exception = assertThrows(IndexOutOfBoundsException.class, () -> {
            DsLinkedList.slice(list, 0, 10);
        });
        
        assertTrue(exception.getMessage().contains("exceeds") || 
                   exception.getMessage().contains("size") ||
                   exception.getMessage().contains("End"),
                   "Error message should mention size constraint");
    }
    
    @Test
    @DisplayName("Start greater than end throws IllegalArgumentException")
    public void whenStartGreaterThanEnd_throwsIllegalArgument() {
        LinkedList<Integer> list = new LinkedList<>(Arrays.asList(1, 2, 3, 4, 5));
        
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            DsLinkedList.slice(list, 4, 2);
        });
        
        assertTrue(exception.getMessage().contains("Start") || 
                   exception.getMessage().contains("cannot exceed") ||
                   exception.getMessage().contains("greater"),
                   "Error message should mention start/end relationship");
    }
    
    @Test
    @DisplayName("Start equals end returns empty list (boundary case)")
    public void whenStartEqualsEnd_returnsEmptyList() {
        LinkedList<Integer> list = new LinkedList<>(Arrays.asList(1, 2, 3, 4, 5));
        LinkedList<Integer> result = DsLinkedList.slice(list, 2, 2);
        
        assertEquals(0, result.size(), "Slice with start==end should return empty list");
    }
}
```

**Test Count:**
- Existing: ~20 happy path tests
- New error tests: 6
- Total: ~26 tests
- Error coverage: 2/2 methods (100%)

---

### PrimesTest.java

**Current State:** Well-organized with @Nested classes, comprehensive happy path

**Vulnerabilities to Test:**
1. `primeFactors(int n)` - MEDIUM: zero input, negative input

#### Recommended New Tests (3 tests)

```java
@Nested
@DisplayName("primeFactors() Error Scenarios")
class PrimeFactorsErrorTests {
    
    @Test
    @DisplayName("Zero input throws IllegalArgumentException")
    public void whenNZero_throwsIllegalArgument() {
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            Primes.primeFactors(0);
        });
        
        assertTrue(exception.getMessage().contains("positive") || 
                   exception.getMessage().contains("must be") ||
                   exception.getMessage().contains("greater than zero"),
                   "Error message should indicate n must be positive");
    }
    
    @Test
    @DisplayName("Negative input throws IllegalArgumentException")
    public void whenNNegative_throwsIllegalArgument() {
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            Primes.primeFactors(-5);
        });
        
        assertTrue(exception.getMessage().contains("positive") || 
                   exception.getMessage().contains("negative"),
                   "Error message should indicate n cannot be negative");
    }
    
    @Test
    @DisplayName("Integer.MIN_VALUE throws IllegalArgumentException")
    public void whenNMinValue_throwsIllegalArgument() {
        assertThrows(IllegalArgumentException.class, () -> {
            Primes.primeFactors(Integer.MIN_VALUE);
        });
    }
}
```

**Test Count:**
- Existing: ~25 happy path tests (well organized)
- New error tests: 3
- Total: ~28 tests
- Error coverage: 1/4 methods (primeFactors needs validation, others handle edge cases correctly)

---

### SortTest.java

**Current State:** Well-organized with @Nested classes

**Vulnerabilities to Test:**
1. `sortVector(ArrayList<Integer> v)` - HIGH: null vector
2. `dutchFlagPartition(ArrayList<Integer> v, int pivot)` - HIGH: null vector
3. `maxN(ArrayList<Integer> v, int n)` - MEDIUM: null vector, n <= 0, n > size

#### Recommended New Tests (8 tests)

```java
@Nested
@DisplayName("sortVector() Error Scenarios")
class SortVectorErrorTests {
    
    @Test
    public void whenVectorNull_throwsNPE() {
        assertThrows(NullPointerException.class, () -> {
            Sort.sortVector(null);
        });
    }
}

@Nested
@DisplayName("dutchFlagPartition() Error Scenarios")
class DutchFlagPartitionErrorTests {
    
    @Test
    public void whenVectorNull_throwsNPE() {
        assertThrows(NullPointerException.class, () -> {
            Sort.dutchFlagPartition(null, 5);
        });
    }
}

@Nested
@DisplayName("maxN() Error Scenarios")
class MaxNErrorTests {
    
    @Test
    public void whenVectorNull_throwsNPE() {
        assertThrows(NullPointerException.class, () -> {
            Sort.maxN(null, 3);
        });
    }
    
    @Test
    @DisplayName("n = 0 throws IllegalArgumentException")
    public void whenNZero_throwsIllegalArgument() {
        ArrayList<Integer> v = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
        
        assertThrows(IllegalArgumentException.class, () -> {
            Sort.maxN(v, 0);
        });
    }
    
    @Test
    @DisplayName("Negative n throws IllegalArgumentException")
    public void whenNNegative_throwsIllegalArgument() {
        ArrayList<Integer> v = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
        
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            Sort.maxN(v, -1);
        });
        
        assertTrue(exception.getMessage().contains("positive") || 
                   exception.getMessage().contains("negative"),
                   "Error message should indicate n must be positive");
    }
    
    @Test
    @DisplayName("n exceeding vector size throws IllegalArgumentException")
    public void whenNExceedsSize_throwsIllegalArgument() {
        ArrayList<Integer> v = new ArrayList<>(Arrays.asList(1, 2, 3));
        
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            Sort.maxN(v, 10);
        });
        
        assertTrue(exception.getMessage().contains("exceeds") || 
                   exception.getMessage().contains("size"),
                   "Error message should mention size constraint");
    }
    
    @Test
    @DisplayName("Empty vector with n > 0 throws IllegalArgumentException")
    public void whenVectorEmptyAndNPositive_throwsIllegalArgument() {
        ArrayList<Integer> v = new ArrayList<>();
        
        assertThrows(IllegalArgumentException.class, () -> {
            Sort.maxN(v, 1);
        });
    }
}
```

**Test Count:**
- Existing: ~30 happy path tests
- New error tests: 8
- Total: ~38 tests
- Error coverage: 3/3 methods (100%)

---

### StropsTest.java

**Current State:** Comprehensive tests with good documentation

**Vulnerabilities to Test:**
1. `reverse(String str)` - HIGH: null string
2. `isPalindrome(String str)` - HIGH: null string

#### Recommended New Tests (2 tests)

```java
// ==================== Error Scenario Tests ====================

@Nested
@DisplayName("reverse() Error Scenarios")
class ReverseErrorTests {
    
    @Test
    @DisplayName("Null string throws NullPointerException")
    public void whenStringNull_throwsNPE() {
        Exception exception = assertThrows(NullPointerException.class, () -> {
            strops.reverse(null);
        });
        
        assertTrue(exception.getMessage().contains("null") || 
                   exception.getMessage().contains("String"),
                   "Error message should mention null string");
    }
}

@Nested
@DisplayName("isPalindrome() Error Scenarios")
class IsPalindromeErrorTests {
    
    @Test
    @DisplayName("Null string throws NullPointerException")
    public void whenStringNull_throwsNPE() {
        Exception exception = assertThrows(NullPointerException.class, () -> {
            strops.isPalindrome(null);
        });
        
        assertTrue(exception.getMessage().contains("null") || 
                   exception.getMessage().contains("String"),
                   "Error message should mention null string");
    }
}
```

**Test Count:**
- Existing: ~24 happy path tests
- New error tests: 2
- Total: ~26 tests
- Error coverage: 2/2 methods (100%)

**Note:** StropsTest already has excellent documentation of bugs. Error tests complement this by verifying null handling.

---

### GenVectorTest.java

**Current State:** Comprehensive coverage with randomness verification

**Vulnerabilities to Test:**
1. `generateVector(int n, int m)` - CRITICAL: negative n, m <= 0

#### Recommended New Tests (5 tests)

```java
// ==================== Error Scenario Tests ====================

@Nested
@DisplayName("generateVector() Error Scenarios")
class GenerateVectorErrorTests {
    
    @Test
    @DisplayName("Negative n throws IllegalArgumentException")
    public void whenNNegative_throwsIllegalArgument() {
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            GenVector.generateVector(-1, 10);
        });
        
        assertTrue(exception.getMessage().contains("negative") || 
                   exception.getMessage().contains("cannot be negative"),
                   "Error message should mention negative size");
    }
    
    @Test
    @DisplayName("m = 0 throws IllegalArgumentException")
    public void whenMZero_throwsIllegalArgument() {
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            GenVector.generateVector(10, 0);
        });
        
        assertTrue(exception.getMessage().contains("positive") || 
                   exception.getMessage().contains("must be positive") ||
                   exception.getMessage().contains("greater than zero"),
                   "Error message should indicate m must be positive");
    }
    
    @Test
    @DisplayName("Negative m throws IllegalArgumentException")
    public void whenMNegative_throwsIllegalArgument() {
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            GenVector.generateVector(10, -5);
        });
        
        assertTrue(exception.getMessage().contains("positive") || 
                   exception.getMessage().contains("negative"),
                   "Error message should indicate m must be positive");
    }
    
    @Test
    @DisplayName("Integer.MIN_VALUE for n throws IllegalArgumentException")
    public void whenNMinValue_throwsIllegalArgument() {
        assertThrows(IllegalArgumentException.class, () -> {
            GenVector.generateVector(Integer.MIN_VALUE, 10);
        });
    }
    
    @Test
    @DisplayName("Integer.MIN_VALUE for m throws IllegalArgumentException")
    public void whenMMinValue_throwsIllegalArgument() {
        assertThrows(IllegalArgumentException.class, () -> {
            GenVector.generateVector(10, Integer.MIN_VALUE);
        });
    }
}
```

**Test Count:**
- Existing: ~15 happy path tests
- New error tests: 5
- Total: ~20 tests
- Error coverage: 1/1 methods (100%)

---

### AppTest.java

**Current State:** File exists but likely minimal/placeholder

**Recommendation:** App.java error handling should focus on graceful degradation, not throwing exceptions

**Test Strategy:**
1. **Not testing for exceptions** - App.java should catch exceptions internally
2. **Test for graceful handling** - Verify app doesn't crash on invalid input
3. **Test error messages** - Verify user-friendly error output

#### Recommended Approach

```java
public class AppTest {
    
    @Test
    @DisplayName("App handles invalid input gracefully without crashing")
    public void testGracefulErrorHandling() {
        // This is more of an integration test
        // Verify App.main() doesn't throw uncaught exceptions
        
        // Redirect System.out to capture output
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(outContent));
        
        try {
            // Test that app doesn't crash
            // Actual implementation depends on App.java structure
            assertDoesNotThrow(() -> {
                // App.someMethod() that might encounter errors
            });
        } finally {
            System.setOut(originalOut);
        }
    }
}
```

**Test Count:**
- Focus on integration-level error handling
- Not counting toward vulnerability coverage (App.java is application layer, not library API)

---

## Edge Case Testing Guidance

### Categories of Edge Cases

#### 1. Null References
**Always test:** Every method accepting reference types (arrays, ArrayLists, LinkedLists, Strings)

**Pattern:**
```java
@Test
public void whenParameterNull_throwsNPE() {
    assertThrows(NullPointerException.class, () -> {
        ClassName.methodName(null);
    });
}
```

**Coverage Target:** 15 methods accept reference parameters → 15 null tests required

#### 2. Empty Collections
**Test when:** Method expects non-empty input OR empty input has special meaning

**Pattern:**
```java
@Test
public void whenArrayEmpty_throwsIllegalArgument() {
    assertThrows(IllegalArgumentException.class, () -> {
        Single.maxArray(new int[0]);
    });
}

@Test
public void whenVectorEmpty_returnsEmptyResult() {
    ArrayList<Integer> v = new ArrayList<>();
    ArrayList<Integer> result = DsVector.sortVector(v);
    assertEquals(0, result.size());
}
```

**Decision:** Throw exception if empty is invalid, return empty/default if valid

**Coverage Target:** 8 methods may reject empty input

#### 3. Boundary Values

**Integer boundaries:**
```java
@Test
public void whenNIntegerMaxValue_handlesCorrectly() {
    // May overflow or throw, depending on method
    assertThrows(ArithmeticException.class, () -> {
        Single.sumRange(Integer.MAX_VALUE);
    });
}

@Test
public void whenNIntegerMinValue_throwsIllegalArgument() {
    assertThrows(IllegalArgumentException.class, () -> {
        Single.sumRange(Integer.MIN_VALUE);
    });
}
```

**Index boundaries:**
```java
@Test
public void whenIndexNegative_throwsIndexOutOfBounds() {
    assertThrows(IndexOutOfBoundsException.class, () -> {
        // method with negative index
    });
}

@Test
public void whenIndexEqualsSize_throwsIndexOutOfBounds() {
    ArrayList<Integer> v = new ArrayList<>(Arrays.asList(1, 2, 3));
    assertThrows(IndexOutOfBoundsException.class, () -> {
        // method accessing v.get(3) when size=3
    });
}
```

**Coverage Target:** All methods with int parameters (check for MIN_VALUE, MAX_VALUE, -1, 0, 1)

#### 4. Negative Numbers (Where Invalid)

**Pattern:**
```java
@Test
public void whenNNegative_throwsIllegalArgument() {
    assertThrows(IllegalArgumentException.class, () -> {
        ClassName.methodName(-1);
    });
}
```

**Methods requiring non-negative inputs:**
- Array sizes/lengths
- Loop bounds (sumRange, sumSquare, sumTriangle)
- Rotation indices
- Count parameters (maxN)
- Vector generation size

**Coverage Target:** 10+ methods should reject negative numbers

#### 5. Zero (Special Case)

**Division by zero:**
```java
@Test
public void whenDivisorZero_throwsArithmeticException() {
    assertThrows(ArithmeticException.class, () -> {
        Single.sumModulus(10, 0);
    });
}
```

**Zero as size/count:**
```java
@Test
public void whenNZero_throwsIllegalArgument() {
    // For methods where zero is invalid (like maxN)
    assertThrows(IllegalArgumentException.class, () -> {
        Sort.maxN(list, 0);
    });
}

@Test
public void whenNZero_returnsEmptyOrZero() {
    // For methods where zero is valid (like generateVector)
    ArrayList<Integer> result = GenVector.generateVector(0, 10);
    assertEquals(0, result.size());
}
```

**Coverage Target:** All methods with divisors, all methods with count/size parameters

#### 6. Array/Collection Length Mismatches

**Pattern:**
```java
@Test
public void whenArrayLengthMismatch_throwsIllegalArgument() {
    assertThrows(IllegalArgumentException.class, () -> {
        Double.countDuplicates(new int[]{1, 2, 3}, new int[]{1, 2});
    });
}
```

**Methods with multiple collection parameters:**
- `countDuplicates(int[] arr0, int[] arr1)` - must be same length

**Coverage Target:** 1 method currently requires same-length arrays

#### 7. Invalid Ranges/Ordering

**Pattern:**
```java
@Test
public void whenStartGreaterThanEnd_throwsIllegalArgument() {
    assertThrows(IllegalArgumentException.class, () -> {
        DsLinkedList.slice(list, 5, 2);
    });
}
```

**Methods with range parameters:**
- `slice(list, start, end)` - requires start <= end
- `rotateVector(v, n)` - requires 0 <= n <= size

**Coverage Target:** 2 methods have range constraints

---

## Coverage Goals

### Overall Error Handling Coverage Goal: 100%

**Definition:** Every validation check (if statement throwing exception) must be tested

### Per-Class Coverage Goals

| Test Class | Methods Needing Validation | Error Tests Required | Happy Path Tests | Total Tests |
|------------|----------------------------|---------------------|------------------|-------------|
| SingleTest.java | 3/3 (100%) | 7 | 3 | 10 |
| DoubleTest.java | 5/5 (100%) | 12 | 5 | 17 |
| DsVectorTest.java | 6/6 (100%) | 9 | ~40 | ~49 |
| DsLinkedListTest.java | 2/2 (100%) | 6 | ~20 | ~26 |
| PrimesTest.java | 1/4 (25%) | 3 | ~25 | ~28 |
| SortTest.java | 3/3 (100%) | 8 | ~30 | ~38 |
| StropsTest.java | 2/2 (100%) | 2 | ~24 | ~26 |
| GenVectorTest.java | 1/1 (100%) | 5 | ~15 | ~20 |
| **TOTAL** | **23/26 (88%)** | **52** | **~162** | **~214** |

**Note:** Not all methods require error handling (e.g., methods that safely handle all inputs)

### Line Coverage Goals (Once Error Handling Implemented)

**Target:** 100% coverage of all validation blocks

**Example:**
```java
// This entire block must be covered by tests
if (arr == null) {
    throw new NullPointerException("Array cannot be null");
}
if (arr.length == 0) {
    throw new IllegalArgumentException("Array cannot be empty");
}
```

**Required Tests:**
1. Test with null → throws NullPointerException ✓
2. Test with empty array → throws IllegalArgumentException ✓
3. Test with valid array → normal execution ✓ (already covered by existing tests)

**Verification Method:**
- Run tests with coverage tool (JaCoCo, IntelliJ coverage)
- Verify 100% coverage of validation blocks
- Verify exception messages are tested (not just exception types)

### Branch Coverage Goals

**Target:** 100% branch coverage for validation logic

**Example:**
```java
if (n < 0) {
    throw new IllegalArgumentException("n must be non-negative");
}
if (m <= 0) {
    throw new IllegalArgumentException("m must be positive");
}
```

**Required Tests:**
- n < 0 → branch taken (exception thrown) ✓
- n >= 0 → branch not taken (continue) ✓
- m <= 0 → branch taken (exception thrown) ✓
- m > 0 → branch not taken (continue) ✓

---

## Error Message Verification

### Why Verify Error Messages?

**Benefits:**
1. **User Experience:** Meaningful messages help developers debug
2. **Documentation:** Messages document what went wrong
3. **Debugging:** Clear messages reduce time-to-fix
4. **Professional Quality:** Industry-standard practice

### Pattern: Basic Message Verification

```java
@Test
public void testMaxArray_whenNull_throwsNPEWithMessage() {
    Exception exception = assertThrows(NullPointerException.class, () -> {
        Single.maxArray(null);
    });
    
    assertTrue(exception.getMessage().contains("null") || 
               exception.getMessage().contains("Array"),
               "Error message should mention null array");
}
```

### Pattern: Specific Message Verification

```java
@Test
public void testRotateVector_whenNegative_throwsWithSpecificMessage() {
    ArrayList<Integer> v = new ArrayList<>(Arrays.asList(1, 2, 3));
    
    Exception exception = assertThrows(IllegalArgumentException.class, () -> {
        DsVector.rotateVector(v, -5);
    });
    
    String message = exception.getMessage();
    assertTrue(message.contains("Rotation") || message.contains("rotation"),
               "Message should mention 'rotation'");
    assertTrue(message.contains("negative") || message.contains("cannot be negative"),
               "Message should mention negative constraint");
    assertTrue(message.contains("-5"),
               "Message should include actual invalid value");
}
```

### Pattern: Exact Message Verification (Use Sparingly)

```java
@Test
public void testSumModulus_whenZero_throwsWithExactMessage() {
    Exception exception = assertThrows(ArithmeticException.class, () -> {
        Single.sumModulus(10, 0);
    });
    
    // Only use exact match if message is part of API contract
    assertEquals("Modulus 'm' cannot be zero", exception.getMessage());
}
```

**Warning:** Exact message matching is brittle. Prefer partial matching with `contains()`.

### Required Elements in Error Messages

**Good error messages should include:**

1. **Parameter name:** Which parameter is invalid?
   ```java
   "Parameter 'n' must be non-negative"
   "Array 'arr' cannot be null"
   "Rotation index 'n' cannot be negative"
   ```

2. **Constraint violated:** What rule was broken?
   ```java
   "must be non-negative"
   "cannot be null"
   "must be positive"
   "cannot exceed size"
   ```

3. **Actual value (when helpful):** What was the invalid value?
   ```java
   "got: -5"
   "Rotation index 'n' (-5) cannot be negative"
   "End index (10) exceeds list size (3)"
   ```

4. **Suggested fix (optional but helpful):**
   ```java
   "Start index (5) cannot exceed end index (2). Ensure start <= end."
   "Modulus 'm' must be positive, got: 0. Use a non-zero divisor."
   ```

### Message Verification Test Template

```java
@Test
public void testMethodName_whenCondition_throwsWithInformativeMessage() {
    Exception exception = assertThrows(ExpectedException.class, () -> {
        ClassName.methodName(invalidInput);
    });
    
    String message = exception.getMessage();
    
    // Verify message contains parameter name
    assertTrue(message.contains("paramName") || message.contains("parameter"),
               "Message should identify which parameter is invalid");
    
    // Verify message describes constraint
    assertTrue(message.contains("constraint keyword"),
               "Message should describe what constraint was violated");
    
    // Optionally verify message includes actual value
    assertTrue(message.contains(String.valueOf(invalidValue)),
               "Message should include the actual invalid value for debugging");
}
```

### Coverage Goal for Message Verification

**Recommendation:** Verify messages for **CRITICAL** and **HIGH** severity errors

**CRITICAL errors (5):** Verify exact message content
- maxArray(null)
- maxArray(empty)
- sumModulus(n, 0)
- rotateVector(v, negative)
- rotateVector(v, exceeds size)

**HIGH errors (15):** Verify key terms present
- Null parameter checks (use contains("null"))
- Range violations (use contains("negative") or contains("positive"))

**MEDIUM errors (8):** Basic verification acceptable
- Just verify exception type, message optional

**Total message verification tests:** 20-25 (for most important error paths)

---

## Implementation Roadmap

### Phase 1: Critical Error Tests (Priority 1)
**Estimated Time:** 2-3 hours

**Tasks:**
1. Add error tests for Single.java CRITICAL vulnerabilities
   - maxArray null/empty (2 tests)
   - sumModulus divide-by-zero (1 test)
2. Add error tests for DsVector.rotateVector CRITICAL vulnerabilities
   - null, negative, exceeds size (3 tests)
3. Add error tests for DsLinkedList.slice CRITICAL vulnerabilities
   - null, boundary violations (4 tests)
4. Add error tests for Double.sumMatrix CRITICAL vulnerability
   - null, empty, null rows, non-square (4 tests)
5. Add error tests for GenVector.generateVector CRITICAL vulnerability
   - negative n, non-positive m (5 tests)

**Total Tests:** 19 critical error tests

**Success Criteria:**
- All CRITICAL vulnerabilities have exception tests
- Messages verified for critical paths
- Tests fail initially (no validation implemented yet)
- Tests follow naming conventions

### Phase 2: High-Severity Error Tests (Priority 2)
**Estimated Time:** 3-4 hours

**Tasks:**
1. Add null checks for all methods accepting ArrayLists (9 tests)
   - DsVector: modifyVector, searchVector, sortVector, reverseVector, filterVector
   - Sort: sortVector, dutchFlagPartition
   - Double: countPairs
2. Add null checks for all methods accepting arrays (3 tests)
   - Double: countDuplicates (2 tests for 2 arrays)
3. Add null checks for all methods accepting Strings (2 tests)
   - Strops: reverse, isPalindrome
4. Add null checks for LinkedList methods (1 test)
   - DsLinkedList: shuffle
5. Add negative input validation tests (5 tests)
   - Single: sumRange
   - Double: sumSquare, sumTriangle
   - Double: countDuplicates array length mismatch

**Total Tests:** 20 high-severity error tests

**Success Criteria:**
- All HIGH severity vulnerabilities have exception tests
- Null checks comprehensively tested
- Negative input validation covered

### Phase 3: Medium-Severity Error Tests (Priority 3)
**Estimated Time:** 2 hours

**Tasks:**
1. Add error tests for Sort.maxN edge cases (5 tests)
   - null, n<=0, n>size
2. Add error tests for Primes.primeFactors edge cases (3 tests)
   - zero, negative, Integer.MIN_VALUE
3. Add boundary tests for sumModulus negative modulus (1 test)
4. Add Integer.MIN_VALUE/MAX_VALUE boundary tests (3 tests)

**Total Tests:** 12 medium-severity error tests

### Phase 4: Error Message Verification Enhancement (Priority 4)
**Estimated Time:** 1-2 hours

**Tasks:**
1. Enhance critical tests with message verification (19 tests)
2. Add message verification to high-severity tests (10 most important)
3. Document expected message format in test comments

**Total Tests:** ~30 tests enhanced with message verification

### Phase 5: Documentation and Organization (Priority 5)
**Estimated Time:** 1 hour

**Tasks:**
1. Add @Nested class organization to all error tests
2. Add @DisplayName annotations for readability
3. Update test class documentation with error testing strategy
4. Verify test naming consistency

**Total Effort:** 9-12 hours for complete error testing implementation

---

## Summary Statistics

### Test Suite Transformation

| Metric | Current State | After Implementation | Change |
|--------|--------------|---------------------|---------|
| Total Test Methods | ~162 | ~214 | +52 (+32%) |
| Exception Tests | 0 | 52 | +52 |
| Methods with Error Coverage | 0/26 | 23/26 | +88% |
| assertThrows() Usage | 0 | 52 | +52 |
| Test Organization (@Nested) | Some | All error tests | Improved |
| Error Message Verification | 0 | ~30 | +30 |

### Coverage by Severity

| Severity | Vulnerabilities | Error Tests | Coverage |
|----------|----------------|-------------|----------|
| CRITICAL | 5 | 19 | 100% |
| HIGH | 15 | 20 | 100% |
| MEDIUM | 8 | 13 | 100% |
| **TOTAL** | **28** | **52** | **100%** |

**Note:** Some methods require multiple error tests (e.g., slice has 4 boundary conditions)

### Expected Test Outcomes

**Before Error Handling Implementation:**
- All 52 new error tests will **FAIL** (methods don't throw exceptions yet)
- Existing 162 happy path tests will **PASS** (functionality works)

**After Error Handling Implementation:**
- All 52 error tests should **PASS** (validation added)
- All 162 happy path tests should **PASS** (functionality preserved)
- **Total: 214 passing tests**

**Code Coverage (After Implementation):**
- **Validation logic:** 100% coverage (all error paths tested)
- **Happy paths:** ~95%+ coverage (already well tested)
- **Overall:** Target 90%+ line coverage

---

## Conclusion

This test recommendation document provides a comprehensive roadmap for achieving **100% error handling test coverage** across the codebase. By implementing the recommended 52 error scenario tests, the test suite will:

✅ **Verify all 28 identified vulnerabilities** are properly handled  
✅ **Follow industry-standard JUnit 5 patterns** using assertThrows()  
✅ **Maintain clear organization** with @Nested classes and naming conventions  
✅ **Verify exception messages** for better debugging and user experience  
✅ **Enable refactoring confidence** through comprehensive error path coverage  
✅ **Demonstrate professional testing practices** suitable for code quality exercises

**Next Steps:**
1. Review and approve this testing strategy
2. Implement error handling in source code (Task #4)
3. Implement error tests following this guide (Task #5)
4. Verify 100% coverage of validation logic
5. Run full test suite: target 214 passing tests

**Key Success Metrics:**
- Zero failures in error scenario tests after error handling implementation
- 100% coverage of validation code paths
- All error messages tested for informativeness
- Clear separation between happy path and error scenario tests
