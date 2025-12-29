"""Test suite for single-loop control operations.

Translated from SingleTest.java to pytest.
"""

import pytest
from sample_project.control.single import sum_range, max_array, sum_modulus


# ==================== Basic Functionality Tests ====================


def test_sum_range():
    """Test sum_range with various input values."""
    assert sum_range(0) == 0
    assert sum_range(1) == 0
    assert sum_range(2) == 1
    assert sum_range(3) == 3
    assert sum_range(4) == 6
    assert sum_range(10) == 45


def test_max_array():
    """Test max_array with various arrays including edge cases."""
    assert max_array([0]) == 0
    assert max_array([1, 2, 3, 4, 5]) == 5
    assert max_array([1, 1, 1, 1, 0]) == 1
    assert max_array([-1, -1, -1, -1, 0]) == 0
    # Edge case: All-negative array
    assert max_array([-5, -3, -10]) == -3
    # Edge case: Mixed positive/negative array
    assert max_array([-5, 3, -10, 7, -2]) == 7
    # Edge case: Single negative element
    assert max_array([-42]) == -42
    # Edge case: All zeros
    assert max_array([0, 0, 0]) == 0


def test_sum_modulus():
    """Test sum_modulus with various modulus values."""
    assert sum_modulus(0, 1) == 0
    assert sum_modulus(1, 2) == 0
    assert sum_modulus(2, 2) == 0
    assert sum_modulus(3, 2) == 2
    assert sum_modulus(4, 2) == 2
    assert sum_modulus(10, 2) == 20
    assert sum_modulus(10, 3) == 18
    assert sum_modulus(10, 4) == 12


# ==================== Error Handling Tests ====================


def test_max_array_when_null_throws_type_error():
    """Test that max_array raises TypeError when given None."""
    with pytest.raises(TypeError):
        max_array(None)


def test_max_array_when_empty_throws_value_error():
    """Test that max_array raises ValueError when given empty array."""
    with pytest.raises(ValueError):
        max_array([])


def test_sum_modulus_when_zero_divisor_throws_value_error():
    """Test that sum_modulus raises ValueError when divisor is zero."""
    with pytest.raises(ValueError):
        sum_modulus(10, 0)


def test_sum_modulus_when_negative_divisor_throws_value_error():
    """Test that sum_modulus raises ValueError when divisor is negative."""
    with pytest.raises(ValueError):
        sum_modulus(10, -1)


def test_sum_range_when_negative_throws_value_error():
    """Test that sum_range raises ValueError when input is negative."""
    with pytest.raises(ValueError):
        sum_range(-1)
