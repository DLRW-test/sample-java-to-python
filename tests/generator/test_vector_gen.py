"""
Comprehensive unit tests for generate_vector() function.

Translated from GenVectorTest.java. The generate_vector() function has been
optimized to use Python's random module for better performance.
"""

import pytest
from sample_project.generator.vector_gen import generate_vector


# ==================== Boundary Condition Tests ====================


def test_generate_vector_empty_vector() -> None:
    """Test with n=0 should return an empty vector."""
    result = generate_vector(0, 10)
    assert len(result) == 0, "Vector with n=0 should be empty"


def test_generate_vector_single_element() -> None:
    """Test with n=1 should return a vector with exactly one element."""
    result = generate_vector(1, 10)
    assert len(result) == 1, "Vector with n=1 should have size 1"
    assert 0 <= result[0] < 10, "Single element should be in valid range [0, 10)"


def test_generate_vector_large_n() -> None:
    """Test with large n (100+ elements) to verify scalability."""
    n = 150
    m = 50
    result = generate_vector(n, m)
    assert len(result) == n, f"Vector should have exactly {n} elements"
    
    # Verify all elements are in valid range
    for i, value in enumerate(result):
        assert 0 <= value < m, (
            f"Element at index {i} ({value}) should be in range [0, {m})"
        )


# ==================== Length Verification Tests ====================


def test_generate_vector_length_verification_various_n() -> None:
    """Test that returned vector length always equals n parameter."""
    test_sizes = [0, 1, 5, 10, 25, 50, 100, 200]
    
    for n in test_sizes:
        result = generate_vector(n, 100)
        assert len(result) == n, f"Vector length should match parameter n={n}"


# ==================== Range Verification Tests ====================


def test_generate_vector_range_verification_small_m() -> None:
    """Test with small m value (m=10)."""
    n = 50
    m = 10
    result = generate_vector(n, m)
    
    for i, value in enumerate(result):
        assert value >= 0, "Element should be non-negative"
        assert value < m, f"Element should be less than m={m}"


def test_generate_vector_range_verification_medium_m() -> None:
    """Test with medium m value (m=100)."""
    n = 50
    m = 100
    result = generate_vector(n, m)
    
    for i, value in enumerate(result):
        assert value >= 0, "Element should be non-negative"
        assert value < m, f"Element should be less than m={m}"


def test_generate_vector_range_verification_large_m() -> None:
    """Test with large m value (m=1000)."""
    n = 50
    m = 1000
    result = generate_vector(n, m)
    
    for i, value in enumerate(result):
        assert value >= 0, "Element should be non-negative"
        assert value < m, f"Element should be less than m={m}"


def test_generate_vector_range_verification_very_large_m() -> None:
    """Test with very large m value."""
    n = 30
    m = 10000
    result = generate_vector(n, m)
    
    for i, value in enumerate(result):
        assert value >= 0, "Element should be non-negative"
        assert value < m, f"Element should be less than m={m}"


# ==================== Edge Cases ====================


def test_generate_vector_edge_case_m_equals_one() -> None:
    """When m=1, all elements should be 0 (only valid value in [0, 1))."""
    n = 20
    m = 1
    result = generate_vector(n, m)
    
    assert len(result) == n, "Vector should have correct size"
    for i, value in enumerate(result):
        assert value == 0, (
            f"When m=1, all elements must be 0 (only value in range [0, 1))"
        )


def test_generate_vector_edge_case_empty_vector_various_m() -> None:
    """Empty vector should work regardless of m value."""
    m_values = [1, 10, 100, 1000]
    
    for m in m_values:
        result = generate_vector(0, m)
        assert len(result) == 0, f"Empty vector (n=0) should work with m={m}"


# ==================== Randomness Verification Tests ====================


def test_generate_vector_randomness_check_elements_vary() -> None:
    """
    Generate multiple vectors and verify elements are not all identical.
    
    This tests that randomness is working (elements should vary).
    """
    n = 20
    m = 10
    
    result1 = generate_vector(n, m)
    result2 = generate_vector(n, m)
    result3 = generate_vector(n, m)
    
    # Check that at least one of the vectors differs from the others
    # It's extremely unlikely (but theoretically possible) that all three
    # random vectors would be identical
    result1_equals_result2 = result1 == result2
    result2_equals_result3 = result2 == result3
    result1_equals_result3 = result1 == result3
    
    all_equal = (
        result1_equals_result2
        and result2_equals_result3
        and result1_equals_result3
    )
    msg = "Multiple random vectors should not all be identical (randomness check)"
    assert not all_equal, msg


def test_generate_vector_randomness_check_not_all_same_value() -> None:
    """
    For a reasonably sized vector with sufficient range,
    not all elements should be the same value.
    """
    n = 50
    m = 20
    
    result = generate_vector(n, m)
    
    # Collect unique values
    unique_values = set(result)
    
    # With 50 elements and range [0, 20), we should have multiple distinct values
    # (probability of all being the same is astronomically low)
    assert len(unique_values) > 1, (
        f"A vector of {n} elements with range [0, {m}) should contain "
        f"multiple distinct values (not all identical)"
    )


def test_generate_vector_randomness_check_distribution_coverage() -> None:
    """
    Generate a large vector and verify we get reasonable coverage of the range.
    
    This is a soft randomness test - with enough elements, we should see
    multiple different values from the range.
    """
    n = 200
    m = 10
    
    result = generate_vector(n, m)
    
    # Count unique values
    unique_values = set(result)
    
    # With 200 elements over range [0, 10), we should see at least
    # several distinct values (typically would see most or all 10 values)
    assert len(unique_values) >= 5, (
        f"With {n} elements over range [0, {m}), should see reasonable "
        f"variety of values (got {len(unique_values)} distinct values)"
    )


# ==================== Exception Tests ====================


def test_generate_vector_negative_n() -> None:
    """Test that negative n raises ValueError."""
    with pytest.raises(ValueError, match="n.*negative|n.*must be.*non-negative"):
        generate_vector(-1, 10)


def test_generate_vector_negative_m() -> None:
    """Test that negative m raises ValueError."""
    with pytest.raises(ValueError, match="m.*negative|m.*must be.*positive"):
        generate_vector(10, -1)


def test_generate_vector_zero_m() -> None:
    """Test that m=0 raises ValueError."""
    with pytest.raises(ValueError, match="m.*zero|m.*must be.*positive"):
        generate_vector(10, 0)


def test_generate_vector_both_negative() -> None:
    """Test that both negative parameters raises ValueError."""
    with pytest.raises(ValueError):
        generate_vector(-5, -10)
