"""Vector (list) manipulation operations.

This module provides utility functions for vector (list) operations including
modification, searching, sorting, reversing, rotation, and merging. All
functions work with lists of integers.
"""


def modify_vector(vector: list[int]) -> list[int]:
    """Add 1 to each element of the list.

    This function increments each element of the input list by 1. The list is
    modified in place and also returned for convenience.

    Args:
        vector: The list of integers to be incremented.

    Returns:
        The modified list (same object as input).

    Raises:
        TypeError: If vector is None.

    Note:
        Time complexity: O(n), Space complexity: O(1) where n is the length of the list.

    Examples:
        >>> modify_vector([1, 2, 3])
        [2, 3, 4]
        >>> modify_vector([])
        []
    """
    if vector is None:
        raise TypeError("ArrayList cannot be null")
    for i in range(len(vector)):
        vector[i] = vector[i] + 1
    return vector


def search_vector(vector: list[int], value: int) -> list[int]:
    """Search the list for all instances of a value.

    This function finds all indices where the specified value appears in the
    list and returns them as a new list.

    Args:
        vector: The list of integers to be searched.
        value: The value to search for.

    Returns:
        A list of all indices where the value was found. Returns an empty list
        if the value is not found.

    Raises:
        TypeError: If vector is None.

    Note:
        Time complexity: O(n), Space complexity: O(k) where n is the length
            of the list and k is the number of matches.

    Examples:
        >>> search_vector([1, 2, 3, 2, 4], 2)
        [1, 3]
        >>> search_vector([1, 2, 3], 5)
        []
    """
    if vector is None:
        raise TypeError("ArrayList cannot be null")
    indices: list[int] = []
    for i in range(len(vector)):
        if vector[i] == value:
            indices.append(i)
    return indices


def sort_vector(vector: list[int]) -> list[int]:
    """Sort the list in ascending order.

    This function creates and returns a new list containing the elements of the
    input list sorted in ascending order. The original list is not modified.

    Args:
        vector: The list of integers to be sorted.

    Returns:
        A new list containing the sorted elements.

    Raises:
        TypeError: If vector is None.

    Note:
        Time complexity: O(n log n), Space complexity: O(n) where n is
            the length of the list.

    Examples:
        >>> sort_vector([3, 1, 4, 1, 5])
        [1, 1, 3, 4, 5]
        >>> sort_vector([])
        []
    """
    if vector is None:
        raise TypeError("ArrayList cannot be null")
    return sorted(vector)


def reverse_vector(vector: list[int]) -> list[int]:
    """Reverse the list.

    This function creates and returns a new list containing the elements of the
    input list in reverse order. The original list is not modified.

    Args:
        vector: The list of integers to be reversed.

    Returns:
        A new list containing the reversed elements.

    Raises:
        TypeError: If vector is None.

    Note:
        Time complexity: O(n), Space complexity: O(n) where n is the
            length of the list.

    Examples:
        >>> reverse_vector([1, 2, 3, 4, 5])
        [5, 4, 3, 2, 1]
        >>> reverse_vector([])
        []
    """
    if vector is None:
        raise TypeError("ArrayList cannot be null")
    result: list[int] = []
    for i in range(len(vector) - 1, -1, -1):
        result.append(vector[i])
    return result


def rotate_vector(vector: list[int], positions: int) -> list[int]:
    """Rotate the list left by a specified number of positions.

    This function creates and returns a new list where elements have been
    rotated left (towards the beginning) by the specified number of positions.
    The original list is not modified.

    Args:
        vector: The list of integers to be rotated.
        positions: The number of positions to rotate. Must be non-negative and
            less than the size of the list (if list is non-empty).

    Returns:
        A new list containing the rotated elements.

    Raises:
        TypeError: If vector is None.
        ValueError: If positions is negative or if positions >= size of the
            list (when list is non-empty).

    Note:
        Time complexity: O(n), Space complexity: O(n) where n is the length of the list.

    Examples:
        >>> rotate_vector([1, 2, 3, 4, 5], 2)
        [3, 4, 5, 1, 2]
        >>> rotate_vector([1, 2, 3], 0)
        [1, 2, 3]
        >>> rotate_vector([], 0)
        []
    """
    if vector is None:
        raise TypeError("ArrayList cannot be null")
    if positions < 0:
        raise ValueError(f"Rotation amount cannot be negative, got: {positions}")
    if len(vector) > 0 and positions >= len(vector):
        raise ValueError(
            f"Rotation amount must be less than size, "
            f"got: {positions} for size: {len(vector)}"
        )
    
    result: list[int] = []
    for i in range(positions, len(vector)):
        result.append(vector[i])
    for i in range(positions):
        result.append(vector[i])
    return result


def merge_vectors(vector1: list[int], vector2: list[int]) -> list[int]:
    """Merge two lists.

    This function creates and returns a new list containing all elements from
    the first list followed by all elements from the second list. The original
    lists are not modified.

    Args:
        vector1: The first list of integers to be merged.
        vector2: The second list of integers to be merged.

    Returns:
        A new list containing all elements from both input lists.

    Raises:
        TypeError: If vector1 or vector2 is None.

    Note:
        Time complexity: O(n + m), Space complexity: O(n + m) where n and
            m are the lengths of the two lists.

    Examples:
        >>> merge_vectors([1, 2, 3], [4, 5, 6])
        [1, 2, 3, 4, 5, 6]
        >>> merge_vectors([], [1, 2])
        [1, 2]
        >>> merge_vectors([1, 2], [])
        [1, 2]
    """
    if vector1 is None:
        raise TypeError("First ArrayList cannot be null")
    if vector2 is None:
        raise TypeError("Second ArrayList cannot be null")
    
    result: list[int] = []
    for i in range(len(vector1)):
        result.append(vector1[i])
    for i in range(len(vector2)):
        result.append(vector2[i])
    return result
