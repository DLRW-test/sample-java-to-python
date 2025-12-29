"""Double-loop control flow operations.

This module provides utility functions that implement double-loop operations
for various computational tasks including sums of squares, triangular numbers,
pair counting, and matrix operations.
"""


def sum_square(n: int) -> int:
    """Calculate the sum of squares from 0 to n-1.

    Computes the sum: 0² + 1² + 2² + ... + (n-1)²
    Uses the formula: (n-1) * n * (2*n-1) / 6

    Args:
        n: The upper bound (exclusive) for the sum of squares.

    Returns:
        The sum of squares from 0 to n-1.

    Raises:
        TypeError: If n is None.
        ValueError: If n is negative.

    Note:
        Time complexity: O(1) - uses closed-form formula.
        Though conceptually represents O(n²) nested loop computation.
    """
    if n is None:
        raise TypeError("n cannot be None")
    if n < 0:
        raise ValueError(f"n must be non-negative, got: {n}")
    return (n - 1) * n * (2 * n - 1) // 6


def sum_triangle(n: int) -> int:
    """Calculate the sum of triangular numbers from T(0) to T(n).

    Computes the sum of triangular numbers: T(0) + T(1) + ... + T(n)
    Uses the formula: (n-1) * n * (n+1) / 6

    Args:
        n: The number of triangular numbers to sum.

    Returns:
        The sum of the first n triangular numbers.

    Raises:
        TypeError: If n is None.
        ValueError: If n is negative.

    Note:
        Time complexity: O(1) - uses closed-form formula.
        Though conceptually represents O(n²) nested loop computation.
    """
    if n is None:
        raise TypeError("n cannot be None")
    if n < 0:
        raise ValueError(f"n must be non-negative, got: {n}")
    return (n - 1) * n * (n + 1) // 6


def count_pairs(arr: list[int]) -> int:
    """Count the number of pairs in an array.

    A pair is any value that appears exactly twice in the array.
    Uses a dictionary to track frequencies in a single pass.

    Args:
        arr: The array of integers to analyze.

    Returns:
        The number of values that appear exactly twice in the array.

    Raises:
        TypeError: If arr is None.

    Note:
        Time complexity: O(n) - single pass with hash map.
        Optimized from O(n²) nested loop approach.
    """
    if arr is None:
        raise TypeError("Array cannot be None")

    # Track frequency of each value
    frequency_map: dict[int, int] = {}

    # Single pass to count frequencies
    for value in arr:
        frequency_map[value] = frequency_map.get(value, 0) + 1

    # Count elements that appear exactly twice
    count = 0
    for freq in frequency_map.values():
        if freq == 2:
            count += 1

    return count


def count_duplicates(arr0: list[int], arr1: list[int]) -> int:
    """Count instances where values at the same index are equal.

    Compares two arrays element-by-element and counts how many positions
    have matching values.

    Args:
        arr0: The first array of integers.
        arr1: The second array of integers.

    Returns:
        The number of positions where arr0[i] == arr1[i].

    Raises:
        TypeError: If arr0 or arr1 is None.
        ValueError: If arrays have different lengths.

    Note:
        Time complexity: O(n) - single pass comparison.
    """
    if arr0 is None:
        raise TypeError("First array cannot be None")
    if arr1 is None:
        raise TypeError("Second array cannot be None")
    if len(arr0) != len(arr1):
        raise ValueError(
            f"Arrays must have equal length, got: {len(arr0)} and {len(arr1)}"
        )

    # Single-pass comparison
    count = 0
    for i in range(len(arr0)):
        if arr0[i] == arr1[i]:
            count += 1

    return count


def sum_matrix(matrix: list[list[int]]) -> int:
    """Sum all values in a square 2D matrix.

    Iterates through all rows and columns of a square matrix to compute
    the total sum of all elements.

    Args:
        matrix: A square 2D array of integers (n x n).

    Returns:
        The sum of all values in the matrix.

    Raises:
        TypeError: If matrix is None or any row is None.
        ValueError: If matrix is not square (rows != columns).

    Note:
        Time complexity: O(n²) - nested loop over all matrix elements.
    """
    if matrix is None:
        raise TypeError("Matrix cannot be None")

    total = 0
    n = len(matrix)

    for i in range(n):
        if matrix[i] is None:
            raise TypeError("Matrix row cannot be None")
        if len(matrix[i]) != n:
            raise ValueError(
                f"Matrix must be square, expected {n} columns but row {i} has {len(matrix[i])}"
            )
        for j in range(n):
            total += matrix[i][j]

    return total
