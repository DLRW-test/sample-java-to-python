# Logging Framework Recommendations and Implementation Guide

## Document Information
- **Project**: Java 17 Sample Project
- **Purpose**: Comprehensive logging framework adoption guidance
- **Date**: 2024
- **Target Framework**: SLF4J 2.0.x + Logback 1.4.x

---

## 1. Logging Framework Selection

### Recommended Framework: SLF4J + Logback

**Primary Recommendation**: Use **SLF4J 2.0.x** as the logging facade with **Logback 1.4.x** as the implementation.

### Rationale

#### Why SLF4J + Logback?

1. **Industry Standard**: Most widely adopted logging solution in the Java ecosystem
2. **Java 17 Compatibility**: SLF4J 2.0.x and Logback 1.4.x are fully compatible with Java 17 and Jakarta EE 9+
3. **Performance**: Logback offers excellent performance with minimal overhead
4. **Flexibility**: Easy configuration through XML, with support for programmatic configuration
5. **Feature-Rich**: Supports automatic reloading of configuration, filtering, conditional processing, and more
6. **Native SLF4J Implementation**: Logback is the native implementation of SLF4J, ensuring optimal integration

#### Comparison with Alternatives

| Feature | SLF4J + Logback | Log4j2 | java.util.logging |
|---------|-----------------|--------|-------------------|
| **Performance** | Excellent | Excellent | Good |
| **Configuration** | XML, Groovy | XML, JSON, YAML, Properties | Properties, Programmatic |
| **Async Logging** | Yes | Yes | Limited |
| **Java 17 Support** | Full (2.0.x/1.4.x) | Full (2.20.x+) | Native |
| **Community** | Very Large | Large | Standard Library |
| **Learning Curve** | Low | Medium | Low |
| **Dependencies** | Minimal | More Complex | None (JDK) |
| **Adoption** | Very High | High | Declining |
| **Security** | Strong track record | Recovering (post-Log4Shell) | Limited features |

**Why Not Log4j2?**
- While Log4j2 has recovered from the Log4Shell vulnerability, it has a more complex dependency tree
- Log4j2's advanced features (plugins, custom appenders) are often overkill for this project's needs
- SLF4J + Logback provides simpler configuration for typical use cases

**Why Not java.util.logging (JUL)?**
- Limited configuration options and less flexible
- Poorer performance compared to modern frameworks
- Less structured logging support
- Smaller ecosystem and fewer integrations

---

## 2. Build Configuration

### Version Compatibility Matrix

For **Java 17** projects, use these specific versions:

| Dependency | Version | Notes |
|------------|---------|-------|
| SLF4J API | 2.0.9 | Latest stable for Java 17 |
| Logback Classic | 1.4.14 | Latest stable for SLF4J 2.x |
| Logback Core | 1.4.14 | Automatically managed by Logback Classic |

### Gradle Configuration (Kotlin DSL)

#### Step 1: Update `gradle/libs.versions.toml`

Add the following to your version catalog:

```toml
[versions]
guava = "32.1.2-jre"
junit-jupiter = "5.10.0"
slf4j = "2.0.9"
logback = "1.4.14"

[libraries]
guava = { module = "com.google.guava:guava", version.ref = "guava" }
junit-jupiter = { module = "org.junit.jupiter:junit-jupiter", version.ref = "junit-jupiter" }
slf4j-api = { module = "org.slf4j:slf4j-api", version.ref = "slf4j" }
logback-classic = { module = "ch.qos.logback:logback-classic", version.ref = "logback" }
```

#### Step 2: Update `app/build.gradle.kts`

Add these dependencies to your build file:

```kotlin
dependencies {
    // Existing dependencies
    testImplementation(libs.junit.jupiter)
    testRuntimeOnly("org.junit.platform:junit-platform-launcher")
    implementation(libs.guava)
    
    // Logging dependencies
    implementation(libs.slf4j.api)
    implementation(libs.logback.classic)
}
```

**Note**: `logback-classic` automatically includes `logback-core` as a transitive dependency, so you don't need to declare it explicitly.

#### Alternative: Direct Version Declaration

If not using a version catalog, add directly to `app/build.gradle.kts`:

```kotlin
dependencies {
    // Logging framework
    implementation("org.slf4j:slf4j-api:2.0.9")
    implementation("ch.qos.logback:logback-classic:1.4.14")
}
```

### Verification

After adding dependencies, verify with:

```bash
./gradlew dependencies --configuration runtimeClasspath
```

Look for:
- `org.slf4j:slf4j-api:2.0.9`
- `ch.qos.logback:logback-classic:1.4.14`
- `ch.qos.logback:logback-core:1.4.14` (transitive)

---

## 3. Logger Initialization Patterns

### Standard Logger Declaration

#### Pattern 1: Class-Based Logger (Recommended)

Use this pattern for all classes:

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class MyClass {
    private static final Logger logger = LoggerFactory.getLogger(MyClass.class);
    
    // Class implementation
}
```

**Why This Pattern?**
- **Type-safe**: Uses class literal, preventing typos
- **Refactoring-friendly**: Automatically updates if class is renamed
- **Industry standard**: Most widely recognized pattern
- **Performance**: Static final ensures single logger instance per class

#### Pattern 2: Custom Named Logger (Special Cases)

Use when you need custom logger hierarchies:

```java
private static final Logger logger = LoggerFactory.getLogger("custom.logger.name");
```

**When to Use**:
- Shared logging across related classes
- Framework or library integration
- Special monitoring requirements

### Logger Initialization by Class Type

#### Utility Classes (Final with Private Constructor)

**Current Examples**: `Single`, `Double`, `Primes`, `Sort`, `DsVector`, `GenVector`, `Strops`

```java
package control;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public final class Single {
    private static final Logger logger = LoggerFactory.getLogger(Single.class);
    
    private Single() {
        throw new UnsupportedOperationException("Utility class");
    }
    
    public static int sumRange(int n) {
        logger.debug("Calculating sum range for n={}", n);
        
        if (n < 0) {
            logger.error("Invalid input: n must be non-negative, got: {}", n);
            throw new IllegalArgumentException("n must be non-negative, got: " + n);
        }
        
        int result = n * (n - 1) / 2;
        logger.debug("Sum range result: {} for n={}", result, n);
        return result;
    }
}
```

#### Application Runner Classes

**Current Example**: `App`

```java
package run.java;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class App {
    private static final Logger logger = LoggerFactory.getLogger(App.class);
    
    public static void main(String[] args) {
        logger.info("Application starting");
        try {
            single();
            double_();
            vector();
            primes();
            sort();
            logger.info("Application completed successfully");
        } catch (Exception e) {
            logger.error("Application error: {}", e.getMessage(), e);
            logger.error("The application encountered an error and will terminate.");
            System.exit(1);
        }
    }
}
```

### Naming Conventions

- **Logger Variable Name**: Always use `logger` (lowercase, singular)
- **Logger Declaration**: Always `private static final`
- **Import Organization**: Place SLF4J imports with other infrastructure imports

**Avoid**:
- ❌ `log` (too generic, conflicts with Math.log)
- ❌ `LOG` (outdated convention)
- ❌ `LOGGER` (uppercase unnecessary, violates Java naming for non-constants)
- ❌ Non-static loggers (creates unnecessary instances)
- ❌ Non-final loggers (prevents optimization)

---

## 4. Log Level Guidelines

### Log Level Definitions and Usage

#### TRACE
**Purpose**: Extremely detailed diagnostic information

**When to Use**:
- Step-by-step algorithm execution (each iteration of a loop)
- Entry/exit of every method
- Variable state at each step

**Project Usage**: Generally not needed for this project (disabled in production)

#### DEBUG
**Purpose**: Detailed diagnostic information useful for development and troubleshooting

**When to Use**:
- Method parameters and return values
- Algorithm intermediate steps
- Data structure state changes
- Performance measurements (execution time)
- Detailed flow through complex logic

**Project Examples**:
- Sieve of Eratosthenes steps in `Primes.generateSieve()`
- Prime factorization iterations in `Primes.primeFactors()`
- Sorting algorithm steps in `Sort.dutchFlagPartition()`
- Vector operation input/output in `DsVector` methods

#### INFO
**Purpose**: Significant application events and milestones

**When to Use**:
- Application startup/shutdown
- Major operation completion
- Successful execution of significant operations
- Configuration information
- High-level operation results

**Project Examples**:
- Application start/end in `App.main()`
- Section headers (SingleForLoop, DoubleForLoop, etc.)
- Operation results in `App` demonstration methods

#### WARN
**Purpose**: Potentially harmful situations that don't prevent operation

**When to Use**:
- Recoverable errors
- Deprecated API usage
- Performance concerns (slow operations)
- Unexpected but handled conditions
- Resource constraints

**Project Examples**:
- Large sieve generation (memory warning for `n > 10,000,000`)
- Empty array operations that return default values
- Performance degradation warnings

#### ERROR
**Purpose**: Error events that might still allow the application to continue

**When to Use**:
- Exceptions that are caught and handled
- Validation failures
- Unrecoverable operation failures
- Data integrity issues

**Project Examples**:
- Invalid input exceptions (negative values, null arrays)
- Validation failures before throwing exceptions
- Caught exceptions in `App` methods

### Mapping Current System.out.println to Log Levels

#### App.java Current Output Analysis

| Line | Current Output | Recommended Level | Rationale |
|------|----------------|-------------------|-----------|
| 14 | `"SingleForLoop"` | INFO | Section header, significant milestone |
| 15 | `"-------------"` | Remove | Visual separator, not needed in logs |
| 16 | `SumRange(10): %s` | INFO | Operation result demonstration |
| 17-19 | `MaxArray([1, 2, 3, 4, 5]): %s` | INFO | Operation result demonstration |
| 20-21 | `SumModulus(100, 3): %s` | INFO | Operation result demonstration |
| 21 | Empty line | Remove | Visual spacing, not needed in logs |
| 25 | `"DoubleForLoop"` | INFO | Section header, significant milestone |
| 26 | `"-------------"` | Remove | Visual separator, not needed in logs |
| 27-29 | `SumSquare(10): %s` | INFO | Operation result demonstration |
| 29-31 | `SumTriangle(10): %s` | INFO | Operation result demonstration |
| 31-34 | `CountPairs([...]): %s` | INFO | Operation result demonstration |
| 34-38 | `CountDuplicates([...]): %s` | INFO | Operation result demonstration |
| 38 | Empty line | Remove | Visual spacing, not needed in logs |
| 45 | `"Vector"` | INFO | Section header, significant milestone |
| 46 | `"------"` | Remove | Visual separator, not needed in logs |
| 47-50 | `ModifyVector(%s): %s` | INFO | Operation result demonstration |
| 50-53 | `SearchVector(%s, 5): %s` | INFO | Operation result demonstration |
| 53-55 | `SortVector(%s): %s` | INFO | Operation result demonstration |
| 55-58 | `ReverseVector(%s): %s` | INFO | Operation result demonstration |
| 58-62 | `RotateVector(%s, 3): %s` | INFO | Operation result demonstration |
| 62-65 | `MergeVectors(%s, %s): %s` | INFO | Operation result demonstration |
| 76 | Empty line | Remove | Visual spacing, not needed in logs |
| 85 | `"Primes"` | INFO | Section header, significant milestone |
| 86 | `"------"` | Remove | Visual separator, not needed in logs |
| 87 | `IsPrime(10): %s` | INFO | Operation result demonstration |
| 88-89 | `SumPrimes(10): %s` | INFO | Operation result demonstration |
| 90-91 | `PrimeFactors(10): %s` | INFO | Operation result demonstration |
| 92 | Empty line | Remove | Visual spacing, not needed in logs |
| 102 | `"Sort"` | INFO | Section header, significant milestone |
| 103 | `"------"` | Remove | Visual separator, not needed in logs |
| 106-107 | `SortVector(%s): %s` | INFO | Operation result demonstration |
| 110-112 | `DutchFlagPartition(%s, 5): %s` | INFO | Operation result demonstration |
| 113-114 | `MaxN(%s, 5): %s` | INFO | Operation result demonstration |
| 115 | Empty line | Remove | Visual spacing, not needed in logs |

#### System.err Usage Analysis

| Line | Current Output | Recommended Level | Rationale |
|------|----------------|-------------------|-----------|
| 24 | `"Error in single loop operations: ..."` | ERROR | Exception handling |
| 46 | `"Error in double loop operations: ..."` | ERROR | Exception handling |
| 78 | `"Error in vector operations: ..."` | ERROR | Exception handling |
| 94 | `"Error in prime operations: ..."` | ERROR | Exception handling |
| 117 | `"Error in sort operations: ..."` | ERROR | Exception handling |
| 130 | `"Application error: ..."` | ERROR | Top-level exception |
| 131 | `"The application encountered an error..."` | ERROR | Shutdown message |

---

## 5. Logging Placement Recommendations

### General Principles

1. **Method Entry/Exit**: For complex operations, log entry with parameters and exit with results
2. **Error Conditions**: Always log before throwing exceptions
3. **Algorithm Steps**: Log significant steps in algorithms at DEBUG level
4. **Performance**: Log execution time for expensive operations
5. **Validation**: Log validation failures before throwing

### Class-by-Class Recommendations

#### 5.1 run.java.App

**Purpose**: Application runner and demonstration harness

**Logging Strategy**:
- INFO: Application lifecycle events
- INFO: Section headers and operation results
- ERROR: Exception handling

**Recommended Changes**:

```java
package run.java;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
// ... other imports

public class App {
    private static final Logger logger = LoggerFactory.getLogger(App.class);
    
    public static void single() {
        try {
            logger.info("=== SingleForLoop Operations ===");
            logger.info("SumRange(10): {}", Single.sumRange(10));
            logger.info("MaxArray([1, 2, 3, 4, 5]): {}", 
                Single.maxArray(new int[] { 1, 2, 3, 4, 5 }));
            logger.info("SumModulus(100, 3): {}", Single.sumModulus(100, 3));
        } catch (IllegalArgumentException | NullPointerException e) {
            logger.error("Error in single loop operations: {}", e.getMessage(), e);
            throw e;
        }
    }
    
    public static void double_() {
        try {
            logger.info("=== DoubleForLoop Operations ===");
            logger.info("SumSquare(10): {}", Double.sumSquare(10));
            logger.info("SumTriangle(10): {}", Double.sumTriangle(10));
            logger.info("CountPairs([1, 2, 3, 4, 5, 2]): {}", 
                Double.countPairs(new int[] { 1, 2, 3, 4, 5, 2 }));
            logger.info("CountDuplicates([1, 2, 3, 4, 5], [1, 3, 2, 4, 5]): {}", 
                Double.countDuplicates(new int[] { 1, 2, 3, 4, 5 }, 
                                      new int[] { 1, 3, 2, 4, 5 }));
        } catch (IllegalArgumentException | NullPointerException e) {
            logger.error("Error in double loop operations: {}", e.getMessage(), e);
            throw e;
        }
    }
    
    public static void vector() {
        try {
            ArrayList<Integer> inputVec = GenVector.generateVector(10, 10);
            ArrayList<Integer> inputVec2 = GenVector.generateVector(10, 10);
            
            logger.info("=== Vector Operations ===");
            logger.info("ModifyVector({}): {}", inputVec, DsVector.modifyVector(inputVec));
            logger.info("SearchVector({}, 5): {}", inputVec, DsVector.searchVector(inputVec, 5));
            logger.info("SortVector({}): {}", inputVec, DsVector.sortVector(inputVec));
            logger.info("ReverseVector({}): {}", inputVec, DsVector.reverseVector(inputVec));
            logger.info("RotateVector({}, 3): {}", inputVec, DsVector.rotateVector(inputVec, 3));
            logger.info("MergeVectors({}, {}): {}", inputVec, inputVec2, 
                DsVector.mergeVectors(inputVec, inputVec2));
        } catch (IllegalArgumentException | NullPointerException e) {
            logger.error("Error in vector operations: {}", e.getMessage(), e);
            throw e;
        }
    }
    
    public static void primes() {
        try {
            logger.info("=== Primes Operations ===");
            logger.info("IsPrime(10): {}", Primes.isPrime(10));
            logger.info("SumPrimes(10): {}", Primes.sumPrimes(10));
            logger.info("PrimeFactors(10): {}", Primes.primeFactors(10));
        } catch (IllegalArgumentException e) {
            logger.error("Error in prime operations: {}", e.getMessage(), e);
            throw e;
        }
    }
    
    public static void sort() {
        try {
            ArrayList<Integer> initialVec = GenVector.generateVector(20, 10);
            logger.info("=== Sort Operations ===");
            
            ArrayList<Integer> inputVec0 = new ArrayList<>(initialVec);
            Sort.sortVector(inputVec0);
            logger.info("SortVector({}): {}", initialVec, inputVec0);
            
            ArrayList<Integer> inputVec1 = new ArrayList<>(initialVec);
            Sort.dutchFlagPartition(inputVec1, 5);
            logger.info("DutchFlagPartition({}, 5): {}", initialVec, inputVec1);
            
            logger.info("MaxN({}, 5): {}", initialVec, Sort.maxN(initialVec, 5));
        } catch (IllegalArgumentException | NullPointerException e) {
            logger.error("Error in sort operations: {}", e.getMessage(), e);
            throw e;
        }
    }
    
    public static void main(String[] args) {
        logger.info("Application starting - Java Sample Project");
        try {
            single();
            double_();
            vector();
            primes();
            sort();
            logger.info("Application completed successfully");
        } catch (Exception e) {
            logger.error("Application error: {}", e.getMessage(), e);
            logger.error("The application encountered an error and will terminate");
            System.exit(1);
        }
    }
}
```

#### 5.2 control.Single

**Purpose**: Single-loop algorithm utility methods

**Logging Strategy**:
- DEBUG: Method entry with parameters
- DEBUG: Calculation results
- ERROR: Validation failures

**Example Implementation**:

```java
package control;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public final class Single {
    private static final Logger logger = LoggerFactory.getLogger(Single.class);
    
    private Single() {
        throw new UnsupportedOperationException("Utility class");
    }
    
    public static int sumRange(int n) {
        logger.debug("sumRange called with n={}", n);
        
        if (n < 0) {
            logger.error("sumRange validation failed: n must be non-negative, got: {}", n);
            throw new IllegalArgumentException("n must be non-negative, got: " + n);
        }
        
        int result = n * (n - 1) / 2;
        logger.debug("sumRange result: {} for n={}", result, n);
        return result;
    }
    
    public static int maxArray(int[] arr) {
        logger.debug("maxArray called with array length={}", arr == null ? "null" : arr.length);
        
        if (arr == null) {
            logger.error("maxArray validation failed: array is null");
            throw new NullPointerException("Array cannot be null");
        }
        if (arr.length == 0) {
            logger.error("maxArray validation failed: array is empty");
            throw new IllegalArgumentException("Array cannot be empty");
        }
        
        int max = arr[0];
        for (int i : arr) {
            if (i > max) {
                max = i;
            }
        }
        
        logger.debug("maxArray result: {} for array length={}", max, arr.length);
        return max;
    }
    
    public static int sumModulus(int n, int m) {
        logger.debug("sumModulus called with n={}, m={}", n, m);
        
        if (m <= 0) {
            logger.error("sumModulus validation failed: modulus must be positive, got: {}", m);
            throw new IllegalArgumentException("Modulus must be positive, got: " + m);
        }
        
        int k = (n - 1) / m;
        int result = m * k * (k + 1) / 2;
        logger.debug("sumModulus result: {} for n={}, m={}", result, n, m);
        return result;
    }
}
```

#### 5.3 control.Double

**Purpose**: Double-loop algorithm utility methods

**Logging Strategy**:
- DEBUG: Method entry with parameters
- DEBUG: Intermediate results (for complex algorithms)
- ERROR: Validation failures

**Example Implementation**:

```java
package control;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.util.HashMap;

public final class Double {
    private static final Logger logger = LoggerFactory.getLogger(Double.class);
    
    private Double() {
        throw new UnsupportedOperationException("Utility class");
    }
    
    public static int sumSquare(int n) {
        logger.debug("sumSquare called with n={}", n);
        int result = (n - 1) * n * (2 * n - 1) / 6;
        logger.debug("sumSquare result: {} for n={}", result, n);
        return result;
    }
    
    public static int countPairs(int[] arr) {
        logger.debug("countPairs called with array length={}", arr == null ? "null" : arr.length);
        
        if (arr == null) {
            logger.error("countPairs validation failed: array is null");
            throw new NullPointerException("Array cannot be null");
        }
        
        HashMap<Integer, Integer> frequencyMap = new HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            frequencyMap.put(arr[i], frequencyMap.getOrDefault(arr[i], 0) + 1);
        }
        
        int count = 0;
        for (int freq : frequencyMap.values()) {
            if (freq == 2) {
                count++;
            }
        }
        
        logger.debug("countPairs result: {} pairs found in array length={}", count, arr.length);
        return count;
    }
    
    public static int countDuplicates(int[] arr0, int[] arr1) {
        logger.debug("countDuplicates called with array lengths=[{}, {}]", 
            arr0 == null ? "null" : arr0.length, arr1 == null ? "null" : arr1.length);
        
        if (arr0 == null) {
            logger.error("countDuplicates validation failed: first array is null");
            throw new NullPointerException("First array cannot be null");
        }
        if (arr1 == null) {
            logger.error("countDuplicates validation failed: second array is null");
            throw new NullPointerException("Second array cannot be null");
        }
        if (arr0.length != arr1.length) {
            logger.error("countDuplicates validation failed: arrays have different lengths: {} and {}", 
                arr0.length, arr1.length);
            throw new IllegalArgumentException(
                "Arrays must have equal length, got: " + arr0.length + " and " + arr1.length);
        }
        
        int count = 0;
        for (int i = 0; i < arr0.length; i++) {
            if (arr0[i] == arr1[i]) {
                count++;
            }
        }
        
        logger.debug("countDuplicates result: {} matches found", count);
        return count;
    }
    
    public static int sumMatrix(int[][] arr) {
        logger.debug("sumMatrix called with matrix dimension={}", arr == null ? "null" : arr.length);
        
        if (arr == null) {
            logger.error("sumMatrix validation failed: matrix is null");
            throw new NullPointerException("Matrix cannot be null");
        }
        
        int sum = 0;
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            if (arr[i] == null) {
                logger.error("sumMatrix validation failed: row {} is null", i);
                throw new NullPointerException("Matrix row cannot be null");
            }
            if (arr[i].length != n) {
                logger.error("sumMatrix validation failed: matrix not square, row {} has {} columns (expected {})", 
                    i, arr[i].length, n);
                throw new IllegalArgumentException(
                    "Matrix must be square, expected " + n + " columns but row " + i + " has " + arr[i].length);
            }
            for (int j = 0; j < n; j++) {
                sum += arr[i][j];
            }
        }
        
        logger.debug("sumMatrix result: {} for {}x{} matrix", sum, n, n);
        return sum;
    }
}
```

#### 5.4 algorithms.Primes

**Purpose**: Prime number algorithms using Sieve of Eratosthenes

**Logging Strategy**:
- DEBUG: Method entry with parameters
- DEBUG: Algorithm execution steps
- WARN: Large sieve generation (memory concerns)
- ERROR: Validation failures

**Example Implementation**:

```java
package algorithms;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.util.ArrayList;

public final class Primes {
    private static final Logger logger = LoggerFactory.getLogger(Primes.class);
    
    // Threshold for memory warning (10 MB)
    private static final int LARGE_SIEVE_THRESHOLD = 10_000_000;
    
    private Primes() {
        throw new UnsupportedOperationException("Utility class");
    }
    
    public static boolean[] generateSieve(int limit) {
        logger.debug("generateSieve called with limit={}", limit);
        
        if (limit < 0) {
            logger.error("generateSieve validation failed: limit is negative: {}", limit);
            throw new IllegalArgumentException("Limit cannot be negative: " + limit);
        }
        
        if (limit > LARGE_SIEVE_THRESHOLD) {
            long estimatedMemoryMB = limit / 1_000_000;
            logger.warn("Generating large sieve for limit={}, estimated memory: ~{} MB", 
                limit, estimatedMemoryMB);
        }
        
        if (limit < 2) {
            logger.debug("generateSieve returning empty sieve for limit={}", limit);
            return new boolean[limit + 1];
        }
        
        boolean[] isPrime = new boolean[limit + 1];
        
        // Initialize all numbers as potentially prime
        for (int i = 2; i <= limit; i++) {
            isPrime[i] = true;
        }
        
        logger.debug("Starting Sieve of Eratosthenes for limit={}", limit);
        
        // Sieve of Eratosthenes algorithm
        for (int i = 2; i * i <= limit; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= limit; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        
        logger.debug("generateSieve completed for limit={}", limit);
        return isPrime;
    }
    
    public static boolean isPrime(int n) {
        logger.debug("isPrime called with n={}", n);
        
        if (n < 2) {
            logger.debug("isPrime result: false for n={} (less than 2)", n);
            return false;
        }
        
        boolean[] sieve = generateSieve(n);
        boolean result = sieve[n];
        logger.debug("isPrime result: {} for n={}", result, n);
        return result;
    }
    
    public static int sumPrimes(int n) {
        logger.debug("sumPrimes called with n={}", n);
        
        if (n < 0) {
            logger.error("sumPrimes validation failed: upper bound is negative: {}", n);
            throw new IllegalArgumentException("Upper bound cannot be negative: " + n);
        }
        if (n <= 2) {
            logger.debug("sumPrimes result: 0 for n={} (no primes less than 2)", n);
            return 0;
        }
        
        boolean[] sieve = generateSieve(n - 1);
        int sum = 0;
        
        for (int i = 2; i < n; i++) {
            if (sieve[i]) {
                sum += i;
            }
        }
        
        logger.debug("sumPrimes result: {} for n={}", sum, n);
        return sum;
    }
    
    public static ArrayList<Integer> primeFactors(int n) {
        logger.debug("primeFactors called with n={}", n);
        
        if (n <= 0) {
            logger.error("primeFactors validation failed: number must be positive: {}", n);
            throw new IllegalArgumentException("Number must be positive: " + n);
        }
        
        ArrayList<Integer> factors = new ArrayList<>();
        
        for (int i = 2; i * i <= n; i++) {
            while (n % i == 0) {
                factors.add(i);
                n /= i;
            }
        }
        if (n > 1) {
            factors.add(n);
        }
        
        logger.debug("primeFactors result: {} factors found", factors.size());
        return factors;
    }
    
    public static ArrayList<Integer> getAllPrimesUpTo(int n) {
        logger.debug("getAllPrimesUpTo called with n={}", n);
        
        if (n < 0) {
            logger.error("getAllPrimesUpTo validation failed: upper bound is negative: {}", n);
            throw new IllegalArgumentException("Upper bound cannot be negative: " + n);
        }
        
        ArrayList<Integer> primes = new ArrayList<>();
        
        if (n < 2) {
            logger.debug("getAllPrimesUpTo result: empty list for n={}", n);
            return primes;
        }
        
        boolean[] sieve = generateSieve(n);
        
        for (int i = 2; i <= n; i++) {
            if (sieve[i]) {
                primes.add(i);
            }
        }
        
        logger.debug("getAllPrimesUpTo result: {} primes found for n={}", primes.size(), n);
        return primes;
    }
}
```

#### 5.5 algorithms.Sort

**Purpose**: Sorting and partitioning algorithms

**Logging Strategy**:
- DEBUG: Method entry with parameters
- DEBUG: Algorithm steps (partition progress)
- ERROR: Validation failures

**Example Implementation**:

```java
package algorithms;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.util.ArrayList;
import java.util.Collections;
import java.util.PriorityQueue;

public final class Sort {
    private static final Logger logger = LoggerFactory.getLogger(Sort.class);
    
    private Sort() {
        throw new UnsupportedOperationException("Utility class");
    }
    
    public static void sortVector(ArrayList<Integer> v) {
        logger.debug("sortVector called with list size={}", v == null ? "null" : v.size());
        
        if (v == null) {
            logger.error("sortVector validation failed: ArrayList is null");
            throw new NullPointerException("ArrayList cannot be null");
        }
        
        Collections.sort(v);
        logger.debug("sortVector completed for list size={}", v.size());
    }
    
    public static void dutchFlagPartition(ArrayList<Integer> v, int pivot_value) {
        logger.debug("dutchFlagPartition called with list size={}, pivot={}", 
            v == null ? "null" : v.size(), pivot_value);
        
        if (v == null) {
            logger.error("dutchFlagPartition validation failed: ArrayList is null");
            throw new NullPointerException("ArrayList cannot be null");
        }
        
        int next_value = 0;
        
        // First pass: move elements < pivot to front
        for (int i = 0; i < v.size(); i++) {
            if (v.get(i) < pivot_value) {
                Collections.swap(v, i, next_value);
                next_value++;
            }
        }
        
        logger.debug("dutchFlagPartition: first pass complete, next_value={}", next_value);
        
        // Second pass: move elements == pivot after the smaller elements
        for (int i = next_value; i < v.size(); i++) {
            if (v.get(i) == pivot_value) {
                Collections.swap(v, i, next_value);
                next_value++;
            }
        }
        
        logger.debug("dutchFlagPartition completed, partitions: [0-{})<pivot, [{})<pivot, [{})<greater", 
            next_value, next_value, v.size());
    }
    
    public static ArrayList<Integer> maxN(ArrayList<Integer> v, int n) {
        logger.debug("maxN called with list size={}, n={}", v == null ? "null" : v.size(), n);
        
        if (v == null) {
            logger.error("maxN validation failed: ArrayList is null");
            throw new NullPointerException("ArrayList cannot be null");
        }
        if (n < 0) {
            logger.error("maxN validation failed: n is negative: {}", n);
            throw new IllegalArgumentException("n cannot be negative: " + n);
        }
        if (n == 0 || n > v.size()) {
            logger.error("maxN validation failed: n={} out of valid range [1, {}]", n, v.size());
            throw new IllegalArgumentException("n must be between 1 and vector size (" + v.size() + "), got: " + n);
        }
        
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for (int i = 0; i < n; ++i) {
            minHeap.offer(v.get(i));
        }
        
        for (int i = n; i < v.size(); ++i) {
            if (v.get(i) > minHeap.peek()) {
                minHeap.poll();
                minHeap.offer(v.get(i));
            }
        }
        
        ArrayList<Integer> ret = new ArrayList<>(minHeap);
        Collections.sort(ret, Collections.reverseOrder());
        
        logger.debug("maxN result: returned {} elements", ret.size());
        return ret;
    }
}
```

#### 5.6 datastructures.DsVector

**Purpose**: Vector/ArrayList manipulation utilities

**Logging Strategy**:
- DEBUG: Method entry with parameters
- DEBUG: Operation results
- ERROR: Validation failures

**Example Implementation**:

```java
package datastructures;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.util.ArrayList;
import java.util.Collections;

public final class DsVector {
    private static final Logger logger = LoggerFactory.getLogger(DsVector.class);
    
    private DsVector() {
        throw new UnsupportedOperationException("Utility class");
    }
    
    public static ArrayList<Integer> modifyVector(ArrayList<Integer> v) {
        logger.debug("modifyVector called with list size={}", v == null ? "null" : v.size());
        
        if (v == null) {
            logger.error("modifyVector validation failed: ArrayList is null");
            throw new NullPointerException("ArrayList cannot be null");
        }
        
        for (int i = 0; i < v.size(); i++) {
            v.set(i, v.get(i) + 1);
        }
        
        logger.debug("modifyVector completed: incremented {} elements", v.size());
        return v;
    }
    
    public static ArrayList<Integer> searchVector(ArrayList<Integer> v, int n) {
        logger.debug("searchVector called with list size={}, search value={}", 
            v == null ? "null" : v.size(), n);
        
        if (v == null) {
            logger.error("searchVector validation failed: ArrayList is null");
            throw new NullPointerException("ArrayList cannot be null");
        }
        
        ArrayList<Integer> indices = new ArrayList<>();
        for (int i = 0; i < v.size(); i++) {
            if (v.get(i) == n) {
                indices.add(i);
            }
        }
        
        logger.debug("searchVector result: found {} occurrences of {}", indices.size(), n);
        return indices;
    }
    
    public static ArrayList<Integer> rotateVector(ArrayList<Integer> v, int n) {
        logger.debug("rotateVector called with list size={}, rotation={}", 
            v == null ? "null" : v.size(), n);
        
        if (v == null) {
            logger.error("rotateVector validation failed: ArrayList is null");
            throw new NullPointerException("ArrayList cannot be null");
        }
        if (n < 0) {
            logger.error("rotateVector validation failed: rotation amount is negative: {}", n);
            throw new IllegalArgumentException("Rotation amount cannot be negative, got: " + n);
        }
        if (v.size() > 0 && n >= v.size()) {
            logger.error("rotateVector validation failed: rotation {} >= size {}", n, v.size());
            throw new IllegalArgumentException(
                "Rotation amount must be less than size, got: " + n + " for size: " + v.size());
        }
        
        ArrayList<Integer> ret = new ArrayList<>();
        for (int i = n; i < v.size(); i++) {
            ret.add(v.get(i));
        }
        for (int i = 0; i < n; i++) {
            ret.add(v.get(i));
        }
        
        logger.debug("rotateVector completed");
        return ret;
    }
    
    public static ArrayList<Integer> mergeVectors(ArrayList<Integer> v1, ArrayList<Integer> v2) {
        logger.debug("mergeVectors called with list sizes=[{}, {}]", 
            v1 == null ? "null" : v1.size(), v2 == null ? "null" : v2.size());
        
        if (v1 == null) {
            logger.error("mergeVectors validation failed: first ArrayList is null");
            throw new NullPointerException("First ArrayList cannot be null");
        }
        if (v2 == null) {
            logger.error("mergeVectors validation failed: second ArrayList is null");
            throw new NullPointerException("Second ArrayList cannot be null");
        }
        
        ArrayList<Integer> ret = new ArrayList<>();
        for (int i = 0; i < v1.size(); i++) {
            ret.add(v1.get(i));
        }
        for (int i = 0; i < v2.size(); i++) {
            ret.add(v2.get(i));
        }
        
        logger.debug("mergeVectors result: merged to size {}", ret.size());
        return ret;
    }
}
```

#### 5.7 generator.GenVector

**Purpose**: Random vector generation

**Logging Strategy**:
- DEBUG: Method entry with parameters
- DEBUG: Generation results
- ERROR: Validation failures

**Example Implementation**:

```java
package generator;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.util.ArrayList;
import java.util.concurrent.ThreadLocalRandom;

public final class GenVector {
    private static final Logger logger = LoggerFactory.getLogger(GenVector.class);
    
    private GenVector() {
        throw new UnsupportedOperationException("Utility class");
    }
    
    public static ArrayList<Integer> generateVector(int n, int m) {
        logger.debug("generateVector called with n={}, m={}", n, m);
        
        if (n < 0) {
            logger.error("generateVector validation failed: length is negative: {}", n);
            throw new IllegalArgumentException("Length n cannot be negative: " + n);
        }
        if (m <= 0) {
            logger.error("generateVector validation failed: maximum value is non-positive: {}", m);
            throw new IllegalArgumentException("Maximum value m must be positive: " + m);
        }
        
        ArrayList<Integer> ret = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            ret.add(ThreadLocalRandom.current().nextInt(m));
        }
        
        logger.debug("generateVector completed: generated {} elements with max value {}", n, m);
        return ret;
    }
}
```

### Performance Logging

For operations that may be expensive, consider adding performance metrics:

```java
public static boolean[] generateSieve(int limit) {
    long startTime = System.nanoTime();
    logger.debug("generateSieve started for limit={}", limit);
    
    // ... algorithm implementation ...
    
    long duration = System.nanoTime() - startTime;
    logger.debug("generateSieve completed in {} ms for limit={}", duration / 1_000_000, limit);
    
    return isPrime;
}
```

---

## 6. Configuration Guidance

### 6.1 Logback Configuration File

Create `app/src/main/resources/logback.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    
    <!-- Property definitions for reusability -->
    <property name="LOG_PATTERN" 
              value="%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n"/>
    <property name="LOG_FILE_PATH" value="logs/app.log"/>
    
    <!-- Console Appender for Development -->
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>${LOG_PATTERN}</pattern>
        </encoder>
        <!-- Optional: Use colored output for console -->
        <withJansi>true</withJansi>
    </appender>
    
    <!-- File Appender for Production-like Scenarios -->
    <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>${LOG_FILE_PATH}</file>
        
        <!-- Rolling policy: daily rotation with size limit -->
        <rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
            <!-- Daily rollover -->
            <fileNamePattern>logs/app-%d{yyyy-MM-dd}.%i.log</fileNamePattern>
            
            <!-- Each file should be at most 10MB -->
            <maxFileSize>10MB</maxFileSize>
            
            <!-- Keep 30 days worth of history -->
            <maxHistory>30</maxHistory>
            
            <!-- Total size of all archive files -->
            <totalSizeCap>1GB</totalSizeCap>
        </rollingPolicy>
        
        <encoder>
            <pattern>${LOG_PATTERN}</pattern>
        </encoder>
    </appender>
    
    <!-- Async Appender for Performance (Optional) -->
    <appender name="ASYNC_FILE" class="ch.qos.logback.classic.AsyncAppender">
        <appender-ref ref="FILE"/>
        <queueSize>512</queueSize>
        <discardingThreshold>0</discardingThreshold>
    </appender>
    
    <!-- Logger Configuration for Application Packages -->
    
    <!-- Control package: detailed debugging -->
    <logger name="control" level="DEBUG" additivity="false">
        <appender-ref ref="CONSOLE"/>
        <appender-ref ref="FILE"/>
    </logger>
    
    <!-- Algorithms package: detailed debugging -->
    <logger name="algorithms" level="DEBUG" additivity="false">
        <appender-ref ref="CONSOLE"/>
        <appender-ref ref="FILE"/>
    </logger>
    
    <!-- Data structures package: detailed debugging -->
    <logger name="datastructures" level="DEBUG" additivity="false">
        <appender-ref ref="CONSOLE"/>
        <appender-ref ref="FILE"/>
    </logger>
    
    <!-- Generator package: info level (less verbose) -->
    <logger name="generator" level="INFO" additivity="false">
        <appender-ref ref="CONSOLE"/>
        <appender-ref ref="FILE"/>
    </logger>
    
    <!-- Application runner: info level -->
    <logger name="run.java" level="INFO" additivity="false">
        <appender-ref ref="CONSOLE"/>
        <appender-ref ref="FILE"/>
    </logger>
    
    <!-- Root logger configuration -->
    <root level="INFO">
        <appender-ref ref="CONSOLE"/>
        <appender-ref ref="FILE"/>
    </root>
    
</configuration>
```

### 6.2 Configuration Profiles

For different environments, you can create profile-specific configurations:

#### Development Profile: `logback-dev.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <property name="LOG_PATTERN" 
              value="%d{HH:mm:ss.SSS} [%thread] %highlight(%-5level) %cyan(%logger{36}) - %msg%n"/>
    
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>${LOG_PATTERN}</pattern>
        </encoder>
    </appender>
    
    <!-- All loggers at DEBUG for development -->
    <root level="DEBUG">
        <appender-ref ref="CONSOLE"/>
    </root>
</configuration>
```

#### Production Profile: `logback-prod.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <property name="LOG_PATTERN" 
              value="%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n"/>
    <property name="LOG_FILE_PATH" value="/var/log/sample-java-app/app.log"/>
    
    <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>${LOG_FILE_PATH}</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
            <fileNamePattern>/var/log/sample-java-app/app-%d{yyyy-MM-dd}.%i.log</fileNamePattern>
            <maxFileSize>50MB</maxFileSize>
            <maxHistory>90</maxHistory>
            <totalSizeCap>5GB</totalSizeCap>
        </rollingPolicy>
        <encoder>
            <pattern>${LOG_PATTERN}</pattern>
        </encoder>
    </appender>
    
    <!-- Production: INFO level, file only -->
    <root level="INFO">
        <appender-ref ref="FILE"/>
    </root>
</configuration>
```

### 6.3 Log Pattern Components

The recommended pattern: `%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n`

| Component | Description | Example |
|-----------|-------------|---------|
| `%d{yyyy-MM-dd HH:mm:ss.SSS}` | Timestamp with milliseconds | `2024-01-15 14:23:45.123` |
| `[%thread]` | Thread name in brackets | `[main]` |
| `%-5level` | Log level, left-justified, 5 chars | `INFO ` |
| `%logger{36}` | Logger name, max 36 chars | `control.Single` |
| `-` | Separator | `-` |
| `%msg` | The log message | `sumRange called with n=10` |
| `%n` | New line | Line break |

**Optional Components**:
- `%class` - Class name
- `%method` - Method name
- `%line` - Line number
- `%exception` - Exception stack trace
- `%mdc` - MDC values

### 6.4 Configuration File Placement

Standard location: `app/src/main/resources/logback.xml`

Directory structure:
```
app/
├── build.gradle.kts
└── src/
    └── main/
        ├── java/
        │   └── ... (source files)
        └── resources/
            ├── logback.xml          (default configuration)
            ├── logback-dev.xml      (development profile)
            └── logback-prod.xml     (production profile)
```

To use a specific profile, set the system property:
```bash
java -Dlogback.configurationFile=logback-dev.xml -jar app.jar
```

### 6.5 Log File Rotation Policies

#### Time-Based Rotation

```xml
<rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
    <!-- Daily rollover -->
    <fileNamePattern>logs/app-%d{yyyy-MM-dd}.log</fileNamePattern>
    <!-- Keep 30 days -->
    <maxHistory>30</maxHistory>
</rollingPolicy>
```

#### Size-Based Rotation

```xml
<rollingPolicy class="ch.qos.logback.core.rolling.FixedWindowRollingPolicy">
    <fileNamePattern>logs/app.%i.log</fileNamePattern>
    <minIndex>1</minIndex>
    <maxIndex>10</maxIndex>
</rollingPolicy>
<triggeringPolicy class="ch.qos.logback.core.rolling.SizeBasedTriggeringPolicy">
    <maxFileSize>10MB</maxFileSize>
</triggeringPolicy>
```

#### Combined (Recommended)

```xml
<rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
    <fileNamePattern>logs/app-%d{yyyy-MM-dd}.%i.log</fileNamePattern>
    <maxFileSize>10MB</maxFileSize>
    <maxHistory>30</maxHistory>
    <totalSizeCap>1GB</totalSizeCap>
</rollingPolicy>
```

---

## 7. Structured Logging Best Practices

### 7.1 Parameterized Messages

**DO: Use Parameterized Messages**

```java
// ✅ GOOD: Efficient, no string concatenation if DEBUG is disabled
logger.debug("Processing vector with size={}, pivot={}", vector.size(), pivotValue);
```

**DON'T: Use String Concatenation**

```java
// ❌ BAD: Always creates string, even if DEBUG is disabled
logger.debug("Processing vector with size=" + vector.size() + ", pivot=" + pivotValue);
```

**Why?**
- Parameterized messages are only formatted if the log level is enabled
- Avoids unnecessary string concatenation and memory allocation
- Better performance, especially for DEBUG/TRACE logs that are often disabled

### 7.2 Logging Collections and Objects

**Logging Collections**:

```java
// ✅ GOOD: Uses collection's toString()
logger.debug("Vector contents: {}", vector);

// ✅ GOOD: Log size first for large collections
logger.debug("Vector size={}, contents={}", vector.size(), vector);

// ⚠️ CAUTION: For very large collections, log size only
if (vector.size() > 100) {
    logger.debug("Large vector size={}", vector.size());
} else {
    logger.debug("Vector size={}, contents={}", vector.size(), vector);
}
```

**Logging Custom Objects**:

```java
// Ensure your objects have meaningful toString() implementations
// Or use specific fields:
logger.debug("Processing user: id={}, name={}", user.getId(), user.getName());
```

### 7.3 Exception Logging

**DO: Include Exception Object**

```java
// ✅ GOOD: Includes full stack trace
try {
    // ... operation
} catch (IllegalArgumentException e) {
    logger.error("Validation failed for input: {}", input, e);
    throw e;
}
```

**DON'T: Log Only Message**

```java
// ❌ BAD: Loses stack trace
catch (IllegalArgumentException e) {
    logger.error("Validation failed: " + e.getMessage());
    throw e;
}
```

**Exception-Only Logging** (when message is redundant):

```java
// If exception message is sufficient
catch (IllegalArgumentException e) {
    logger.error("Operation failed", e);
    throw e;
}
```

### 7.4 Conditional Logging

For expensive operations:

```java
// ✅ GOOD: Check log level before expensive computation
if (logger.isDebugEnabled()) {
    String expensiveDebugInfo = computeExpensiveDebugInfo();
    logger.debug("Debug info: {}", expensiveDebugInfo);
}
```

However, parameterized messages usually eliminate the need for this:

```java
// ✅ BETTER: Let SLF4J handle it with parameterized messages
logger.debug("Debug info: {}", this::computeExpensiveDebugInfo);
```

### 7.5 MDC (Mapped Diagnostic Context)

MDC allows adding contextual information to all log messages in a thread.

**Use Case**: Multi-threaded applications, request tracking

**Example**:

```java
import org.slf4j.MDC;

public class App {
    public static void main(String[] args) {
        // Add context for this execution
        MDC.put("executionId", UUID.randomUUID().toString());
        MDC.put("user", "demo");
        
        try {
            logger.info("Application starting");
            // All logs in this thread will include MDC values
            single();
            double_();
        } finally {
            // Always clear MDC to prevent memory leaks
            MDC.clear();
        }
    }
}
```

**Configuration** (add to log pattern):

```xml
<pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} [%X{executionId}] - %msg%n</pattern>
```

**Output**:
```
2024-01-15 14:23:45.123 [main] INFO  run.java.App [a1b2c3d4-...] - Application starting
```

**For This Project**: MDC is optional. Consider it if you add multi-threading or want to track different execution runs.

### 7.6 Performance Data Logging

For algorithm performance metrics:

```java
public static int sumPrimes(int n) {
    long startTime = System.nanoTime();
    logger.debug("sumPrimes started for n={}", n);
    
    // ... algorithm implementation ...
    
    long durationNs = System.nanoTime() - startTime;
    long durationMs = durationNs / 1_000_000;
    
    if (durationMs > 100) {
        logger.warn("sumPrimes took {} ms for n={} (slower than expected)", durationMs, n);
    } else {
        logger.debug("sumPrimes completed in {} ms for n={}", durationMs, n);
    }
    
    return sum;
}
```

### 7.7 Logging Anti-Patterns

**Anti-Pattern 1: Over-logging**

```java
// ❌ BAD: Too verbose, clutters logs
logger.debug("Entering method");
logger.debug("Variable x = {}", x);
logger.debug("Variable y = {}", y);
logger.debug("Calling helper method");
logger.debug("Helper method returned");
logger.debug("Exiting method");
```

```java
// ✅ GOOD: Meaningful debug points
logger.debug("Processing data: x={}, y={}", x, y);
// ... logic ...
logger.debug("Processing complete: result={}", result);
```

**Anti-Pattern 2: Logging Sensitive Data**

```java
// ❌ BAD: Logs passwords, credit cards, etc.
logger.debug("User credentials: username={}, password={}", username, password);
```

```java
// ✅ GOOD: Redact or omit sensitive data
logger.debug("User authentication attempt: username={}", username);
```

**Anti-Pattern 3: Swallowing Exceptions**

```java
// ❌ BAD: Exception lost
try {
    riskyOperation();
} catch (Exception e) {
    // Silent failure
}
```

```java
// ✅ GOOD: Log the exception
try {
    riskyOperation();
} catch (Exception e) {
    logger.error("Risky operation failed", e);
    throw e; // or handle appropriately
}
```

**Anti-Pattern 4: Logging in Loops**

```java
// ❌ BAD: Creates thousands of log entries
for (int i = 0; i < 10000; i++) {
    logger.debug("Processing item {}", i);
    processItem(i);
}
```

```java
// ✅ GOOD: Log summary or batch progress
logger.debug("Processing {} items", items.size());
for (int i = 0; i < items.size(); i++) {
    processItem(i);
    if (i % 1000 == 0) {
        logger.debug("Progress: {}/{} items processed", i, items.size());
    }
}
logger.debug("Processing complete: {} items processed", items.size());
```

---

## 8. Migration Strategy

### 8.1 Systematic Approach

Follow this order for migrating from `System.out`/`System.err` to logging:

1. **Setup Phase** (Task 1)
   - Add dependencies to build files
   - Create `logback.xml` configuration
   - Verify build and dependencies

2. **Error Logging Phase** (Task 2) - PRIORITIZE
   - Replace `System.err.println` with `logger.error()`
   - Add logging to exception handlers
   - Add validation failure logging

3. **Info Logging Phase** (Task 3)
   - Replace main output in `App.java` with `logger.info()`
   - Keep user-facing output similar

4. **Debug Logging Phase** (Task 4)
   - Add detailed logging to utility classes
   - Add algorithm step logging
   - Add performance metrics

5. **Refinement Phase** (Task 5)
   - Adjust log levels based on testing
   - Optimize log messages
   - Fine-tune configuration

### 8.2 Step-by-Step Migration Plan

#### Phase 1: Setup (15 minutes)

**Step 1.1**: Update `gradle/libs.versions.toml`
```toml
[versions]
slf4j = "2.0.9"
logback = "1.4.14"

[libraries]
slf4j-api = { module = "org.slf4j:slf4j-api", version.ref = "slf4j" }
logback-classic = { module = "ch.qos.logback:logback-classic", version.ref = "logback" }
```

**Step 1.2**: Update `app/build.gradle.kts`
```kotlin
dependencies {
    // ... existing dependencies ...
    implementation(libs.slf4j.api)
    implementation(libs.logback.classic)
}
```

**Step 1.3**: Create `app/src/main/resources/logback.xml`
- Use the configuration from Section 6.1

**Step 1.4**: Verify build
```bash
./gradlew clean build
```

#### Phase 2: Error Logging (30 minutes)

**Priority**: Start with error scenarios to ensure failures are properly logged.

**Step 2.1**: Update `App.java` error handlers

Before:
```java
} catch (IllegalArgumentException | NullPointerException e) {
    System.err.println("Error in single loop operations: " + e.getMessage());
    throw e;
}
```

After:
```java
private static final Logger logger = LoggerFactory.getLogger(App.class);

// ...

} catch (IllegalArgumentException | NullPointerException e) {
    logger.error("Error in single loop operations: {}", e.getMessage(), e);
    throw e;
}
```

**Step 2.2**: Update all utility class validation failures

For each validation that throws an exception, add error logging before the throw:

Before:
```java
if (n < 0) {
    throw new IllegalArgumentException("n must be non-negative, got: " + n);
}
```

After:
```java
private static final Logger logger = LoggerFactory.getLogger(Single.class);

// ...

if (n < 0) {
    logger.error("Validation failed: n must be non-negative, got: {}", n);
    throw new IllegalArgumentException("n must be non-negative, got: " + n);
}
```

**Files to update**:
- `App.java` - All catch blocks (5 locations)
- `Single.java` - All validation failures (3 methods)
- `Double.java` - All validation failures (4 methods)
- `Primes.java` - All validation failures (5 methods)
- `Sort.java` - All validation failures (3 methods)
- `DsVector.java` - All validation failures (6 methods)
- `GenVector.java` - All validation failures (1 method)

#### Phase 3: Info Logging (45 minutes)

**Step 3.1**: Update `App.java` main method

Before:
```java
public static void main(String[] args) {
    try {
        single();
        // ...
    } catch (Exception e) {
        System.err.println("Application error: " + e.getMessage());
        System.exit(1);
    }
}
```

After:
```java
public static void main(String[] args) {
    logger.info("Application starting - Java Sample Project");
    try {
        single();
        double_();
        vector();
        primes();
        sort();
        logger.info("Application completed successfully");
    } catch (Exception e) {
        logger.error("Application error: {}", e.getMessage(), e);
        logger.error("The application encountered an error and will terminate");
        System.exit(1);
    }
}
```

**Step 3.2**: Update demonstration methods

Before:
```java
public static void single() {
    System.out.println("SingleForLoop");
    System.out.println("-------------");
    System.out.println(String.format("SumRange(10): %s", Single.sumRange(10)));
    // ...
}
```

After:
```java
public static void single() {
    try {
        logger.info("=== SingleForLoop Operations ===");
        logger.info("SumRange(10): {}", Single.sumRange(10));
        logger.info("MaxArray([1, 2, 3, 4, 5]): {}", 
            Single.maxArray(new int[] { 1, 2, 3, 4, 5 }));
        logger.info("SumModulus(100, 3): {}", Single.sumModulus(100, 3));
    } catch (IllegalArgumentException | NullPointerException e) {
        logger.error("Error in single loop operations: {}", e.getMessage(), e);
        throw e;
    }
}
```

**Apply to all demonstration methods**:
- `single()`
- `double_()`
- `vector()`
- `primes()`
- `sort()`

**Notes**:
- Remove `System.out.println()` for separators (`"-------------"`)
- Remove `System.out.println()` for empty lines
- Use `===` in section headers for visual distinction
- Use parameterized messages (`{}`) instead of `String.format()`

#### Phase 4: Debug Logging (60 minutes)

**Step 4.1**: Add method entry/exit logging

Add to each public method in utility classes:

```java
public static int sumRange(int n) {
    logger.debug("sumRange called with n={}", n);
    
    // ... validation ...
    
    int result = n * (n - 1) / 2;
    logger.debug("sumRange result: {} for n={}", result, n);
    return result;
}
```

**Step 4.2**: Add algorithm step logging

For complex algorithms like `Primes.generateSieve()`:

```java
public static boolean[] generateSieve(int limit) {
    logger.debug("generateSieve called with limit={}", limit);
    
    if (limit > 10_000_000) {
        logger.warn("Generating large sieve for limit={}, estimated memory: ~{} MB", 
            limit, limit / 1_000_000);
    }
    
    // ... algorithm ...
    
    logger.debug("generateSieve completed for limit={}", limit);
    return isPrime;
}
```

**Step 4.3**: Add performance logging (optional)

For expensive operations:

```java
long startTime = System.nanoTime();
logger.debug("Operation started");

// ... operation ...

long durationMs = (System.nanoTime() - startTime) / 1_000_000;
logger.debug("Operation completed in {} ms", durationMs);
```

**Files to update**:
- All utility classes in `control/`, `algorithms/`, `datastructures/`, `generator/`

#### Phase 5: Testing and Refinement (30 minutes)

**Step 5.1**: Run the application

```bash
./gradlew run
```

**Step 5.2**: Verify log output

Check that:
- Application starts and completes messages appear
- Section headers are visible
- Operation results are logged
- No `System.out.println` output remains (except intentional)

**Step 5.3**: Adjust log levels

If logs are too verbose:
- Change package log levels in `logback.xml`
- Consider setting generator package to INFO instead of DEBUG

If logs are too quiet:
- Ensure DEBUG logging is enabled for development

**Step 5.4**: Test error scenarios

Run tests to ensure error logging works:

```bash
./gradlew test
```

Check that exceptions are properly logged with stack traces.

### 8.3 Backward Compatibility Considerations

**Maintaining Output Format**:

If the application output is used by other tools/scripts:

**Option 1**: Keep similar output format
```java
// Instead of removing System.out entirely, you could keep both:
logger.info("SumRange(10): {}", result);
System.out.println("SumRange(10): " + result); // For backward compatibility
```

**Option 2**: Add output mode flag
```java
private static final boolean CONSOLE_OUTPUT = 
    Boolean.parseBoolean(System.getProperty("console.output", "true"));

public static void single() {
    int result = Single.sumRange(10);
    logger.info("SumRange(10): {}", result);
    if (CONSOLE_OUTPUT) {
        System.out.println("SumRange(10): " + result);
    }
}
```

**For this project**: Since it's a learning/demonstration project, full migration is recommended without backward compatibility concerns.

### 8.4 Testing Strategy

**Before Migration**:
```bash
# Capture current output
./gradlew run > before-output.txt 2> before-errors.txt
```

**After Migration**:
```bash
# Capture new output
./gradlew run > after-output.txt 2> after-errors.txt

# Compare logs directory
ls -la logs/
cat logs/app.log
```

**Validation Checklist**:
- [ ] Application starts successfully
- [ ] All operations execute without errors
- [ ] Log files are created in `logs/` directory
- [ ] Log levels are appropriate (INFO for results, ERROR for failures)
- [ ] No `System.out.println` calls remain (use grep to verify)
- [ ] Exception stack traces appear in logs
- [ ] Performance is acceptable (logging overhead is minimal)

### 8.5 Migration Checklist

- [ ] **Setup**
  - [ ] Dependencies added to `libs.versions.toml`
  - [ ] Dependencies added to `build.gradle.kts`
  - [ ] `logback.xml` created in `src/main/resources`
  - [ ] Build successful with `./gradlew clean build`

- [ ] **Error Logging**
  - [ ] App.java exception handlers updated (5 locations)
  - [ ] Single.java validation failures logged (3 methods)
  - [ ] Double.java validation failures logged (4 methods)
  - [ ] Primes.java validation failures logged (5 methods)
  - [ ] Sort.java validation failures logged (3 methods)
  - [ ] DsVector.java validation failures logged (6 methods)
  - [ ] GenVector.java validation failures logged (1 method)

- [ ] **Info Logging**
  - [ ] App.main() startup/shutdown messages
  - [ ] App.single() demonstration output
  - [ ] App.double_() demonstration output
  - [ ] App.vector() demonstration output
  - [ ] App.primes() demonstration output
  - [ ] App.sort() demonstration output
  - [ ] All `System.out.println` replaced with `logger.info()`

- [ ] **Debug Logging**
  - [ ] control.Single methods (3 methods)
  - [ ] control.Double methods (5 methods)
  - [ ] algorithms.Primes methods (5 methods)
  - [ ] algorithms.Sort methods (3 methods)
  - [ ] datastructures.DsVector methods (6 methods)
  - [ ] generator.GenVector methods (1 method)
  - [ ] Performance logging added (optional)

- [ ] **Testing**
  - [ ] Application runs successfully
  - [ ] Log files created correctly
  - [ ] Log rotation works
  - [ ] Error scenarios log properly
  - [ ] Unit tests still pass

- [ ] **Documentation**
  - [ ] README updated with logging information
  - [ ] Configuration documented
  - [ ] Log file locations documented

---

## 9. Summary and Best Practices

### 9.1 Quick Reference

**Logger Declaration**:
```java
private static final Logger logger = LoggerFactory.getLogger(MyClass.class);
```

**Log Levels**:
- `ERROR`: Validation failures, exceptions
- `WARN`: Performance concerns, large operations
- `INFO`: Operation results, application lifecycle
- `DEBUG`: Method parameters, algorithm steps, detailed flow

**Parameterized Messages**:
```java
logger.info("Operation result: {}", result);
logger.debug("Processing: param1={}, param2={}", param1, param2);
logger.error("Operation failed: {}", message, exception);
```

### 9.2 Key Recommendations

1. **Use SLF4J 2.0.9 + Logback 1.4.14** for Java 17 compatibility
2. **Always use parameterized messages** for performance
3. **Log validation failures** before throwing exceptions
4. **Include exception objects** when logging errors
5. **Use DEBUG for detailed flow**, INFO for results, ERROR for failures
6. **Configure logback.xml** with appropriate appenders and patterns
7. **Test error scenarios** to ensure proper logging
8. **Monitor log file size** and configure rotation policies

### 9.3 Additional Resources

**Official Documentation**:
- SLF4J: https://www.slf4j.org/manual.html
- Logback: https://logback.qos.ch/manual/index.html
- Logback Configuration: https://logback.qos.ch/manual/configuration.html

**Best Practices**:
- Google Java Style Guide (Logging): https://google.github.io/styleguide/javaguide.html
- Baeldung SLF4J Guide: https://www.baeldung.com/slf4j-with-log4j2-logback

**Performance**:
- Logback Performance: https://logback.qos.ch/performance.html
- Async Logging: https://logback.qos.ch/manual/appenders.html#AsyncAppender

---

## 10. Appendix

### 10.1 Complete Example: Single.java with Logging

```java
package control;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public final class Single {
    private static final Logger logger = LoggerFactory.getLogger(Single.class);
    
    private Single() {
        throw new UnsupportedOperationException("Utility class");
    }
    
    /**
     * This method is used to calculate the sum of the first n natural numbers.
     * n exclusive
     *
     * @param n The number of natural numbers to sum.
     * @return The sum of the first n natural numbers.
     * @throws IllegalArgumentException if n is negative
     */
    public static int sumRange(int n) {
        logger.debug("sumRange called with n={}", n);
        
        if (n < 0) {
            logger.error("sumRange validation failed: n must be non-negative, got: {}", n);
            throw new IllegalArgumentException("n must be non-negative, got: " + n);
        }
        
        int result = n * (n - 1) / 2;
        logger.debug("sumRange result: {} for n={}", result, n);
        return result;
    }
    
    /**
     * This method calculates the maximum value in an array of integers.
     *
     * @param arr The array of integers.
     * @return The maximum value in the array.
     * @throws NullPointerException if arr is null
     * @throws IllegalArgumentException if arr is empty
     */
    public static int maxArray(int[] arr) {
        logger.debug("maxArray called with array length={}", arr == null ? "null" : arr.length);
        
        if (arr == null) {
            logger.error("maxArray validation failed: array is null");
            throw new NullPointerException("Array cannot be null");
        }
        if (arr.length == 0) {
            logger.error("maxArray validation failed: array is empty");
            throw new IllegalArgumentException("Array cannot be empty");
        }
        
        int max = arr[0];
        for (int i : arr) {
            if (i > max) {
                max = i;
            }
        }
        
        logger.debug("maxArray result: {} for array length={}", max, arr.length);
        return max;
    }
    
    /**
     * This method calculates the sum of the first n natural numbers, modulo m.
     *
     * @param n The number of natural numbers to sum.
     * @param m The modulus.
     * @return The sum of the first n natural numbers, modulo m.
     * @throws IllegalArgumentException if m is zero or negative
     */
    public static int sumModulus(int n, int m) {
        logger.debug("sumModulus called with n={}, m={}", n, m);
        
        if (m <= 0) {
            logger.error("sumModulus validation failed: modulus must be positive, got: {}", m);
            throw new IllegalArgumentException("Modulus must be positive, got: " + m);
        }
        
        int k = (n - 1) / m;
        int result = m * k * (k + 1) / 2;
        logger.debug("sumModulus result: {} for n={}, m={}", result, n, m);
        return result;
    }
}
```

### 10.2 Complete Logback Configuration with Comments

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    
    <!-- 
        Property Definitions
        Define reusable properties for patterns and file paths
    -->
    <property name="LOG_PATTERN" 
              value="%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n"/>
    <property name="CONSOLE_PATTERN" 
              value="%d{HH:mm:ss.SSS} %highlight(%-5level) %cyan(%logger{36}) - %msg%n"/>
    <property name="LOG_FILE_PATH" value="logs/app.log"/>
    
    <!-- 
        Console Appender
        Outputs to System.out with optional colored output
        Best for development
    -->
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>${CONSOLE_PATTERN}</pattern>
        </encoder>
    </appender>
    
    <!-- 
        Rolling File Appender
        Writes to rotating log files with size and time-based rolling
        Best for production
    -->
    <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <!-- Current log file -->
        <file>${LOG_FILE_PATH}</file>
        
        <!-- Rolling policy: combines time-based and size-based rolling -->
        <rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
            <!-- Archive file naming pattern -->
            <fileNamePattern>logs/app-%d{yyyy-MM-dd}.%i.log</fileNamePattern>
            
            <!-- Maximum size per file before rolling -->
            <maxFileSize>10MB</maxFileSize>
            
            <!-- Keep log files for 30 days -->
            <maxHistory>30</maxHistory>
            
            <!-- Maximum total size of all archived files -->
            <totalSizeCap>1GB</totalSizeCap>
            
            <!-- Clean up on startup if size limits exceeded -->
            <cleanHistoryOnStart>true</cleanHistoryOnStart>
        </rollingPolicy>
        
        <!-- Log message formatting -->
        <encoder>
            <pattern>${LOG_PATTERN}</pattern>
        </encoder>
    </appender>
    
    <!-- 
        Async File Appender (Optional)
        Wraps FILE appender for better performance
        Use if file I/O impacts application performance
    -->
    <appender name="ASYNC_FILE" class="ch.qos.logback.classic.AsyncAppender">
        <appender-ref ref="FILE"/>
        <!-- Queue size for buffering log events -->
        <queueSize>512</queueSize>
        <!-- Don't discard any events (set to 0) -->
        <discardingThreshold>0</discardingThreshold>
        <!-- Include caller data (performance impact) -->
        <includeCallerData>false</includeCallerData>
    </appender>
    
    <!-- 
        Package-specific Loggers
        Configure log levels per package for fine-grained control
    -->
    
    <!-- Control package: single and double loop algorithms -->
    <logger name="control" level="DEBUG" additivity="false">
        <appender-ref ref="CONSOLE"/>
        <appender-ref ref="FILE"/>
    </logger>
    
    <!-- Algorithms package: primes, sorting -->
    <logger name="algorithms" level="DEBUG" additivity="false">
        <appender-ref ref="CONSOLE"/>
        <appender-ref ref="FILE"/>
    </logger>
    
    <!-- Data structures package: vector operations -->
    <logger name="datastructures" level="DEBUG" additivity="false">
        <appender-ref ref="CONSOLE"/>
        <appender-ref ref="FILE"/>
    </logger>
    
    <!-- Generator package: random data generation (less verbose) -->
    <logger name="generator" level="INFO" additivity="false">
        <appender-ref ref="CONSOLE"/>
        <appender-ref ref="FILE"/>
    </logger>
    
    <!-- Application runner: main application lifecycle -->
    <logger name="run.java" level="INFO" additivity="false">
        <appender-ref ref="CONSOLE"/>
        <appender-ref ref="FILE"/>
    </logger>
    
    <!-- 
        Root Logger
        Fallback for any classes not covered by package-specific loggers
    -->
    <root level="INFO">
        <appender-ref ref="CONSOLE"/>
        <appender-ref ref="FILE"/>
    </root>
    
    <!-- 
        Configuration Notes:
        - Adjust log levels per environment (DEBUG for dev, INFO for prod)
        - Use ASYNC_FILE instead of FILE for high-throughput applications
        - Consider separate appenders for ERROR level (e.g., error.log)
        - Add email appender for critical errors in production
        - Enable JMX for runtime configuration changes
    -->
    
</configuration>
```

### 10.3 Gradle Build File Complete Example

```kotlin
plugins {
    application
}

repositories {
    mavenCentral()
}

dependencies {
    // Testing
    testImplementation(libs.junit.jupiter)
    testRuntimeOnly("org.junit.platform:junit-platform-launcher")
    
    // Application dependencies
    implementation(libs.guava)
    
    // Logging framework
    implementation(libs.slf4j.api)
    implementation(libs.logback.classic)
    // Note: logback-core is transitively included by logback-classic
}

java {
    toolchain {
        languageVersion.set(JavaLanguageVersion.of(17))
    }
}

application {
    mainClass.set("run.java.App")
}

tasks.named<Test>("test") {
    useJUnitPlatform()
}

// Optional: Configure run task to use specific logback configuration
tasks.named<JavaExec>("run") {
    // Use development logback configuration
    systemProperty("logback.configurationFile", "src/main/resources/logback-dev.xml")
}
```

### 10.4 Version Catalog Complete Example

```toml
# gradle/libs.versions.toml

[versions]
guava = "32.1.2-jre"
junit-jupiter = "5.10.0"
slf4j = "2.0.9"
logback = "1.4.14"

[libraries]
guava = { module = "com.google.guava:guava", version.ref = "guava" }
junit-jupiter = { module = "org.junit.jupiter:junit-jupiter", version.ref = "junit-jupiter" }
slf4j-api = { module = "org.slf4j:slf4j-api", version.ref = "slf4j" }
logback-classic = { module = "ch.qos.logback:logback-classic", version.ref = "logback" }

[bundles]
logging = ["slf4j-api", "logback-classic"]
```

Usage with bundles:
```kotlin
dependencies {
    implementation(libs.bundles.logging)
}
```

---

**End of Logging Framework Recommendations**
