"""Sorting utilities and algorithms.

This module provides sorting utilities including basic sorting, the Dutch flag
partition algorithm for three-way partitioning, and heap-based selection of
the N largest elements from a list.
"""

import heapq


def sort_vector(data: list[int]) -> list[int]:
    """Sort a list of integers in ascending order.

    Creates and returns a new sorted list without modifying the original.
    Uses Python's built-in Timsort algorithm for efficient sorting.

    Args:
        data: The list of integers to be sorted.

    Returns:
        A new list containing all elements from data in ascending order.

    Raises:
        TypeError: If data is None.

    Note:
        Time complexity: O(n log n) where n is the length of the list.
        Space complexity: O(n) for the new sorted list.

    Example:
        >>> sort_vector([3, 1, 4, 1, 5, 9, 2, 6])
        [1, 1, 2, 3, 4, 5, 6, 9]
        >>> sort_vector([5, 2, 8, 1])
        [1, 2, 5, 8]
        >>> sort_vector([])
        []
    """
    if data is None:
        raise TypeError("List cannot be None")
    return sorted(data)


def dutch_flag_partition(arr: list[int], pivot: int) -> list[int]:
    """Partition a list around a pivot value using the Dutch flag algorithm.

    Implements the Dutch national flag problem solution, partitioning the
    list into three sections: elements less than pivot, elements equal to
    pivot, and elements greater than pivot. Returns a new partitioned list
    without modifying the original.

    The algorithm performs two passes:
    1. Move all elements < pivot to the front
    2. Move all elements == pivot after the < pivot section

    Args:
        arr: The list of integers to be partitioned.
        pivot: The pivot value for partitioning.

    Returns:
        A new list with elements partitioned into three sections:
        [elements < pivot][elements == pivot][elements > pivot]

    Raises:
        TypeError: If arr is None.

    Note:
        Time complexity: O(n) where n is the length of the list (two passes).
        Space complexity: O(n) for the new partitioned list.

    Example:
        >>> dutch_flag_partition([3, 5, 2, 6, 8, 1, 0, 5, 5], 5)
        [3, 2, 1, 0, 5, 5, 5, 6, 8]
        >>> dutch_flag_partition([1, 0, 2, 1, 0, 2, 1], 1)
        [0, 0, 1, 1, 1, 2, 2]
        >>> dutch_flag_partition([4, 4, 4], 4)
        [4, 4, 4]
    """
    if arr is None:
        raise TypeError("List cannot be None")

    # Create a copy to avoid modifying the original
    result = arr.copy()
    next_value = 0

    # First pass: move all elements < pivot to the front
    for i in range(len(result)):
        if result[i] < pivot:
            result[i], result[next_value] = result[next_value], result[i]
            next_value += 1

    # Second pass: move all elements == pivot after the < pivot section
    for i in range(next_value, len(result)):
        if result[i] == pivot:
            result[i], result[next_value] = result[next_value], result[i]
            next_value += 1

    return result


def max_n(data: list[int], n: int) -> list[int]:
    """Return the N largest elements from a list.

    Uses a min-heap of size N to efficiently find the largest N elements.
    The result is sorted in descending order (largest first).

    Args:
        data: The list of integers to search.
        n: The number of largest elements to return.

    Returns:
        A list of the N largest elements in descending order.

    Raises:
        TypeError: If data is None.
        ValueError: If n is negative, zero, or greater than the size of data.

    Note:
        Time complexity: O(n log k) where n is the list size and k is the
            number of elements to return.
        Space complexity: O(k) for the heap.

    Example:
        >>> max_n([3, 1, 4, 1, 5, 9, 2, 6], 3)
        [9, 6, 5]
        >>> max_n([10, 20, 30, 40, 50], 2)
        [50, 40]
        >>> max_n([7], 1)
        [7]
    """
    if data is None:
        raise TypeError("List cannot be None")
    if n < 0:
        raise ValueError(f"n cannot be negative: {n}")
    if n == 0 or n > len(data):
        raise ValueError(
            f"n must be between 1 and list size ({len(data)}), got: {n}"
        )

    # Build a min-heap with the first n elements
    min_heap = data[:n].copy()
    heapq.heapify(min_heap)

    # Process remaining elements
    for i in range(n, len(data)):
        if data[i] > min_heap[0]:
            heapq.heapreplace(min_heap, data[i])

    # Sort in descending order and return
    result = sorted(min_heap, reverse=True)
    return result
