"""LinkedList operations module.

This module provides utility functions for linked list operations using
Python's `collections.deque[int]`. The deque data structure is chosen for
its O(1) append and pop operations at both ends, making it the most similar
to Java's LinkedList in terms of performance characteristics.

All functions return new deque instances, maintaining immutability of the
input data structures.
"""

import random
from collections import deque


def shuffle(linked_list: deque[int]) -> deque[int]:
    """Shuffle a linked list into a new deque with randomized element order.

    This function creates a new deque with the same elements as the input
    but in a random order. The original deque is not modified.

    Args:
        linked_list: The deque to be shuffled.

    Returns:
        A new deque with elements in random order.

    Raises:
        TypeError: If linked_list is None.

    Note:
        Time complexity: O(n), Space complexity: O(n)
    """
    if linked_list is None:
        raise TypeError("LinkedList cannot be None")
    # Convert to list for random.shuffle (similar to Java's ArrayList conversion)
    tmp = list(linked_list)
    random.shuffle(tmp)
    return deque(tmp)


def slice(linked_list: deque[int], start: int, end: int) -> deque[int]:
    """Return a slice of a linked list from start to end index.

    This function extracts a sublist from the input deque, from the start
    index (inclusive) to the end index (exclusive). The original deque is
    not modified.

    Args:
        linked_list: The deque to be sliced.
        start: The starting index of the slice (inclusive).
        end: The ending index of the slice (exclusive).

    Returns:
        A new deque containing elements from start to end-1.

    Raises:
        TypeError: If linked_list is None.
        IndexError: If start or end are out of bounds.
        ValueError: If start is greater than end.

    Note:
        Time complexity: O(n), Space complexity: O(k) where k is the slice size
    """
    if linked_list is None:
        raise TypeError("LinkedList cannot be None")
    
    size = len(linked_list)
    
    if start < 0 or start > size:
        raise IndexError(
            f"Start index out of bounds: {start} for size: {size}"
        )
    if end < 0 or end > size:
        raise IndexError(
            f"End index out of bounds: {end} for size: {size}"
        )
    if start > end:
        raise ValueError(
            f"Start index ({start}) cannot be greater than end index ({end})"
        )
    
    # Convert to list for slicing, then back to deque
    tmp = list(linked_list)
    return deque(tmp[start:end])
