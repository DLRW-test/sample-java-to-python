"""Random vector generation module.

This module provides functionality for generating vectors (lists) of random integers
within a specified range.
"""

import random


def generate_vector(size: int, min_val: int, max_val: int) -> list[int]:
    """Generate a vector of random integers within a specified range.

    Creates a list of random integers where each element is independently
    generated within the inclusive range [min_val, max_val].

    Args:
        size: The number of elements in the generated vector. Must be non-negative.
        min_val: The minimum value (inclusive) for generated integers.
        max_val: The maximum value (inclusive) for generated integers.

    Returns:
        A list of random integers with the specified size, where each element
        is in the range [min_val, max_val].

    Raises:
        TypeError: If any of the input parameters is None.
        ValueError: If size is negative (size < 0).
        ValueError: If min_val is greater than max_val.

    Complexity:
        O(n) where n is the size parameter, as we generate n random integers.

    Example:
        >>> vec = generate_vector(5, 0, 10)
        >>> len(vec)
        5
        >>> all(0 <= x <= 10 for x in vec)
        True
    """
    # Check for None inputs
    if size is None or min_val is None or max_val is None:
        raise TypeError("All parameters must be non-None values")

    # Validate size
    if size < 0:
        raise ValueError(f"Size cannot be negative: {size}")

    # Validate range
    if min_val > max_val:
        raise ValueError(
            f"min_val ({min_val}) cannot be greater than max_val ({max_val})"
        )

    # Generate vector with random integers
    return [random.randint(min_val, max_val) for _ in range(size)]
