"""Test suite for double-loop control operations.

Translated from DoubleTest.java to pytest.
"""

import pytest
from sample_project.control.double import (
    sum_square,
    sum_triangle,
    count_pairs,
    count_duplicates,
    sum_matrix,
)


# ==================== Basic Functionality Tests ====================


def test_sum_square():
    """Test sum_square with various input values."""
    assert sum_square(1) == 0
    assert sum_square(2) == 1
    assert sum_square(3) == 5
    assert sum_square(10) == 285


def test_sum_triangle():
    """Test sum_triangle with various input values."""
    assert sum_triangle(1) == 0
    assert sum_triangle(2) == 1
    assert sum_triangle(3) == 4
    assert sum_triangle(10) == 165


def test_count_pairs():
    """Test count_pairs with various arrays.
    
    A pair is any value that is repeated exactly twice in the array.
    """
    assert count_pairs([0]) == 0
    assert count_pairs([1, 2, 3]) == 0
    assert count_pairs([1, 1, 1]) == 0
    assert count_pairs([1, 1, 2]) == 1
    assert count_pairs([1, 1, 2, 2]) == 2
    assert count_pairs([0, 0, 1, 1, 2, 2]) == 3
    assert count_pairs([0, 0, 1, 1, 2, 2, 3]) == 3


def test_count_duplicates():
    """Test count_duplicates with various array pairs.
    
    Counts instances where values at the same index are equal.
    """
    assert count_duplicates([0], [0]) == 1
    assert count_duplicates([1, 2, 3], [2, 3, 1]) == 0
    assert count_duplicates([1, 1, 1], [1, 2, 3]) == 1
    assert count_duplicates([1, 1, 2], [1, 2, 2]) == 2
    assert count_duplicates([1, 1, 2, 2], [1, 1, 2, 2]) == 4


def test_sum_matrix():
    """Test sum_matrix with various square matrices."""
    assert sum_matrix([[0]]) == 0
    assert sum_matrix([[0, 1], [2, 3]]) == 6
    assert sum_matrix([[0, 1, 2], [3, 4, 5], [6, 7, 8]]) == 36


# ==================== Error Handling Tests ====================


def test_count_pairs_when_null_throws_type_error():
    """Test that count_pairs raises TypeError when given None."""
    with pytest.raises(TypeError):
        count_pairs(None)


def test_count_duplicates_when_first_array_null_throws_type_error():
    """Test that count_duplicates raises TypeError when first array is None."""
    with pytest.raises(TypeError):
        count_duplicates(None, [1, 2, 3])


def test_count_duplicates_when_second_array_null_throws_type_error():
    """Test that count_duplicates raises TypeError when second array is None."""
    with pytest.raises(TypeError):
        count_duplicates([1, 2, 3], None)


def test_count_duplicates_when_length_mismatch_throws_value_error():
    """Test that count_duplicates raises ValueError when arrays have different lengths."""
    with pytest.raises(ValueError):
        count_duplicates([1, 2], [1, 2, 3])


def test_sum_matrix_when_null_throws_type_error():
    """Test that sum_matrix raises TypeError when given None."""
    with pytest.raises(TypeError):
        sum_matrix(None)


def test_sum_matrix_when_row_null_throws_type_error():
    """Test that sum_matrix raises TypeError when a row is None."""
    with pytest.raises(TypeError):
        sum_matrix([[1, 2], None])


def test_sum_matrix_when_not_square_throws_value_error():
    """Test that sum_matrix raises ValueError when matrix is not square."""
    with pytest.raises(ValueError):
        sum_matrix([[1, 2, 3], [4, 5]])
