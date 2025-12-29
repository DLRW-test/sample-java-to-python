"""Single-loop control flow operations.

This module provides utility functions for single-loop control operations,
including range summation, array maximum finding, and modular arithmetic
summation.
"""


def sum_range(n: int) -> int:
    """Calculate sum of integers from 1 to n (exclusive).

    This method calculates the sum of integers from 1 to n-1 using the
    formula n * (n - 1) / 2.

    Args:
        n: Upper bound of range (exclusive).

    Returns:
        Sum of integers from 1 to n-1.

    Raises:
        ValueError: If n is negative.

    Complexity:
        O(n) time, O(1) space
    """
    if n < 0:
        raise ValueError(f"n must be non-negative, got: {n}")
    return n * (n - 1) // 2


def max_array(array: list[int]) -> int:
    """Calculate the maximum value in an array of integers.

    This method iterates through the array to find and return the maximum
    value.

    Args:
        array: The list of integers to search.

    Returns:
        The maximum value in the array.

    Raises:
        TypeError: If array is None.
        ValueError: If array is empty.

    Complexity:
        O(n) time, O(1) space
    """
    if array is None:
        raise TypeError("Array cannot be None")
    if len(array) == 0:
        raise ValueError("Array cannot be empty")
    max_val = array[0]
    for i in array:
        if i > max_val:
            max_val = i
    return max_val


def sum_modulus(n: int, m: int) -> int:
    """Calculate the sum of the first n natural numbers, modulo m.

    This method calculates the sum of multiples of m that are less than n,
    using the formula m * k * (k + 1) / 2 where k = (n - 1) / m.

    Args:
        n: The number of natural numbers to consider.
        m: The modulus.

    Returns:
        The sum of the first n natural numbers, modulo m.

    Raises:
        ValueError: If n is negative or m is zero or negative.

    Complexity:
        O(n²) time, O(1) space
    """
    if n < 0:
        raise ValueError(f"n must be non-negative, got: {n}")
    if m <= 0:
        raise ValueError(f"Modulus must be positive, got: {m}")
    k = (n - 1) // m
    return m * k * (k + 1) // 2
