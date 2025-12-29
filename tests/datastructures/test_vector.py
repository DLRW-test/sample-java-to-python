"""
Test suite for the vector module.

Translates test cases from datastructures.DsVectorTest.java to pytest format.
Tests cover:
- modifyVector: In-place modification of vector elements
- searchVector: Finding all indices of a target value
- sortVector: Creating sorted copies (immutability)
- reverseVector: Creating reversed copies (immutability)
- rotateVector: Creating rotated copies (immutability)
- mergeVectors: Merging two vectors (immutability)
- Error handling for None inputs and invalid parameters
"""

import pytest
from sample_project.datastructures.vector import (
    modify_vector,
    search_vector,
    sort_vector,
    reverse_vector,
    rotate_vector,
    merge_vectors,
)


# ==================== modifyVector Tests ====================


class TestModifyVector:
    """Tests for modify_vector function (in-place modification)."""

    def test_empty_vector(self):
        """Empty vector should remain empty after modification."""
        v = []
        result = modify_vector(v)
        assert len(result) == 0
        assert result is v  # Verify same reference (in-place modification)

    def test_single_element(self):
        """Single element should be incremented by 1."""
        v = [5]
        result = modify_vector(v)
        assert len(result) == 1
        assert result[0] == 6  # 5 + 1 = 6
        assert result is v

    def test_multiple_elements(self):
        """Multiple elements should each be incremented by 1."""
        v = [1, 2, 3, 4]
        result = modify_vector(v)
        assert len(result) == 4
        assert result[0] == 2
        assert result[1] == 3
        assert result[2] == 4
        assert result[3] == 5
        assert result is v

    def test_with_negative_numbers(self):
        """Negative numbers should also be incremented by 1."""
        v = [-5, 0, 10]
        result = modify_vector(v)
        assert result[0] == -4
        assert result[1] == 1
        assert result[2] == 11

    def test_when_none_raises_type_error(self):
        """None input should raise TypeError."""
        with pytest.raises(TypeError):
            modify_vector(None)


# ==================== searchVector Tests ====================


class TestSearchVector:
    """Tests for search_vector function."""

    def test_empty_vector(self):
        """Empty vector should return no matches."""
        v = []
        result = search_vector(v, 5)
        assert len(result) == 0  # No matches in empty vector

    def test_element_not_found(self):
        """Element not in vector should return no matches."""
        v = [1, 2, 3]
        result = search_vector(v, 5)
        assert len(result) == 0  # No matches found

    def test_single_match_at_beginning(self):
        """Single match at beginning should return index 0."""
        v = [10, 20, 30]
        result = search_vector(v, 10)
        assert len(result) == 1
        assert result[0] == 0

    def test_single_match_in_middle(self):
        """Single match in middle should return correct index."""
        v = [10, 20, 30]
        result = search_vector(v, 20)
        assert len(result) == 1
        assert result[0] == 1

    def test_single_match_at_end(self):
        """Single match at end should return last index."""
        v = [10, 20, 30]
        result = search_vector(v, 30)
        assert len(result) == 1
        assert result[0] == 2

    def test_multiple_matches(self):
        """Multiple matches should return all indices in order."""
        v = [5, 10, 5, 20, 5]
        result = search_vector(v, 5)
        assert len(result) == 3
        assert result[0] == 0  # First match
        assert result[1] == 2  # Second match
        assert result[2] == 4  # Third match

    def test_when_none_raises_type_error(self):
        """None input should raise TypeError."""
        with pytest.raises(TypeError):
            search_vector(None, 5)


# ==================== sortVector Tests ====================


class TestSortVector:
    """Tests for sort_vector function (creates new sorted vector)."""

    def test_empty_vector(self):
        """Empty vector should return empty sorted vector."""
        v = []
        result = sort_vector(v)
        assert len(result) == 0

    def test_single_element(self):
        """Single element should remain unchanged."""
        v = [42]
        result = sort_vector(v)
        assert len(result) == 1
        assert result[0] == 42

    def test_already_sorted(self):
        """Already sorted vector should remain sorted."""
        v = [1, 2, 3, 4, 5]
        result = sort_vector(v)
        assert len(result) == 5
        assert result[0] == 1
        assert result[1] == 2
        assert result[2] == 3
        assert result[3] == 4
        assert result[4] == 5

    def test_reverse_sorted(self):
        """Reverse sorted vector should be sorted correctly."""
        v = [5, 4, 3, 2, 1]
        result = sort_vector(v)
        assert len(result) == 5
        assert result[0] == 1
        assert result[1] == 2
        assert result[2] == 3
        assert result[3] == 4
        assert result[4] == 5

    def test_with_duplicates(self):
        """Vector with duplicates should sort with duplicates preserved."""
        v = [3, 1, 3, 2, 1]
        result = sort_vector(v)
        assert len(result) == 5
        assert result[0] == 1
        assert result[1] == 1
        assert result[2] == 2
        assert result[3] == 3
        assert result[4] == 3

    def test_random_order(self):
        """Randomly ordered vector should be sorted correctly."""
        v = [9, 2, 7, 1, 5]
        result = sort_vector(v)
        assert len(result) == 5
        assert result[0] == 1
        assert result[1] == 2
        assert result[2] == 5
        assert result[3] == 7
        assert result[4] == 9

    def test_creates_new_vector(self):
        """sort_vector should create a new vector and not modify original."""
        v = [3, 1, 2]
        result = sort_vector(v)
        # Original should be unchanged
        assert v[0] == 3
        assert v[1] == 1
        assert v[2] == 2
        # Result should be sorted
        assert result[0] == 1
        assert result[1] == 2
        assert result[2] == 3

    def test_with_negative_numbers(self):
        """Vector with negative numbers should sort correctly."""
        v = [-5, 3, -10, 0, 7]
        result = sort_vector(v)
        assert result[0] == -10
        assert result[1] == -5
        assert result[2] == 0
        assert result[3] == 3
        assert result[4] == 7

    def test_when_none_raises_type_error(self):
        """None input should raise TypeError."""
        with pytest.raises(TypeError):
            sort_vector(None)


# ==================== reverseVector Tests ====================


class TestReverseVector:
    """Tests for reverse_vector function (creates new reversed vector)."""

    def test_empty_vector(self):
        """Empty vector should return empty reversed vector."""
        v = []
        result = reverse_vector(v)
        assert len(result) == 0

    def test_single_element(self):
        """Single element should remain unchanged."""
        v = [42]
        result = reverse_vector(v)
        assert len(result) == 1
        assert result[0] == 42

    def test_multiple_elements(self):
        """Multiple elements should be reversed."""
        v = [1, 2, 3, 4, 5]
        result = reverse_vector(v)
        assert len(result) == 5
        assert result[0] == 5
        assert result[1] == 4
        assert result[2] == 3
        assert result[3] == 2
        assert result[4] == 1

    def test_creates_new_vector(self):
        """reverse_vector should create a new vector and not modify original."""
        v = [1, 2, 3]
        result = reverse_vector(v)
        # Original should be unchanged
        assert v[0] == 1
        assert v[1] == 2
        assert v[2] == 3
        # Result should be reversed
        assert result[0] == 3
        assert result[1] == 2
        assert result[2] == 1

    def test_even_number_of_elements(self):
        """Even number of elements should reverse correctly."""
        v = [10, 20, 30, 40]
        result = reverse_vector(v)
        assert result[0] == 40
        assert result[1] == 30
        assert result[2] == 20
        assert result[3] == 10

    def test_when_none_raises_type_error(self):
        """None input should raise TypeError."""
        with pytest.raises(TypeError):
            reverse_vector(None)


# ==================== rotateVector Tests ====================


class TestRotateVector:
    """Tests for rotate_vector function (creates new rotated vector)."""

    def test_zero_rotation(self):
        """Zero rotation should return copy of original vector."""
        v = [1, 2, 3, 4]
        result = rotate_vector(v, 0)
        assert len(result) == 4
        assert result[0] == 1
        assert result[1] == 2
        assert result[2] == 3
        assert result[3] == 4

    def test_full_rotation(self):
        """Full rotation (by size) should return to original order."""
        v = [1, 2, 3, 4]
        result = rotate_vector(v, 4)
        assert len(result) == 4
        assert result[0] == 1
        assert result[1] == 2
        assert result[2] == 3
        assert result[3] == 4

    def test_normal_rotation(self):
        """Normal rotation should shift elements correctly."""
        v = [1, 2, 3, 4, 5]
        result = rotate_vector(v, 2)
        assert len(result) == 5
        assert result[0] == 3  # Element at index 2
        assert result[1] == 4  # Element at index 3
        assert result[2] == 5  # Element at index 4
        assert result[3] == 1  # Element at index 0
        assert result[4] == 2  # Element at index 1

    def test_single_element(self):
        """Single element with zero rotation should remain unchanged."""
        v = [42]
        result = rotate_vector(v, 0)
        assert len(result) == 1
        assert result[0] == 42

    def test_single_element_with_rotation(self):
        """Single element with rotation should remain unchanged."""
        v = [42]
        result = rotate_vector(v, 1)
        assert len(result) == 1
        assert result[0] == 42

    def test_empty_vector(self):
        """Empty vector should return empty rotated vector."""
        v = []
        result = rotate_vector(v, 5)
        assert len(result) == 0

    def test_rotate_by_one(self):
        """Rotate by one should shift all elements left by one."""
        v = [10, 20, 30]
        result = rotate_vector(v, 1)
        assert len(result) == 3
        assert result[0] == 20
        assert result[1] == 30
        assert result[2] == 10

    def test_creates_new_vector(self):
        """rotate_vector should create a new vector and not modify original."""
        v = [1, 2, 3]
        result = rotate_vector(v, 1)
        # Original should be unchanged
        assert v[0] == 1
        assert v[1] == 2
        assert v[2] == 3

    def test_when_none_raises_type_error(self):
        """None input should raise TypeError."""
        with pytest.raises(TypeError):
            rotate_vector(None, 2)

    def test_when_negative_rotation_raises_value_error(self):
        """Negative rotation should raise ValueError."""
        v = [1, 2, 3]
        with pytest.raises(ValueError):
            rotate_vector(v, -1)

    def test_when_rotation_exceeds_size_raises_value_error(self):
        """Rotation exceeding size should raise ValueError."""
        v = [1, 2]
        with pytest.raises(ValueError):
            rotate_vector(v, 5)


# ==================== mergeVectors Tests ====================


class TestMergeVectors:
    """Tests for merge_vectors function (creates new merged vector)."""

    def test_both_empty(self):
        """Merging two empty vectors should return empty vector."""
        v1 = []
        v2 = []
        result = merge_vectors(v1, v2)
        assert len(result) == 0

    def test_first_empty_second_non_empty(self):
        """Merging empty with non-empty should return copy of non-empty."""
        v1 = []
        v2 = [1, 2, 3]
        result = merge_vectors(v1, v2)
        assert len(result) == 3
        assert result[0] == 1
        assert result[1] == 2
        assert result[2] == 3

    def test_first_non_empty_second_empty(self):
        """Merging non-empty with empty should return copy of non-empty."""
        v1 = [10, 20]
        v2 = []
        result = merge_vectors(v1, v2)
        assert len(result) == 2
        assert result[0] == 10
        assert result[1] == 20

    def test_both_non_empty(self):
        """Merging two non-empty vectors should concatenate them."""
        v1 = [1, 2]
        v2 = [3, 4, 5]
        result = merge_vectors(v1, v2)
        assert len(result) == 5
        assert result[0] == 1
        assert result[1] == 2
        assert result[2] == 3
        assert result[3] == 4
        assert result[4] == 5

    def test_order_preservation(self):
        """Merge should preserve order: v1 elements first, then v2 elements."""
        v1 = [100, 200, 300]
        v2 = [10, 20]
        result = merge_vectors(v1, v2)
        # v1 elements should come first
        assert result[0] == 100
        assert result[1] == 200
        assert result[2] == 300
        # v2 elements should come after
        assert result[3] == 10
        assert result[4] == 20

    def test_originals_unchanged(self):
        """merge_vectors should not modify original vectors."""
        v1 = [1, 2]
        v2 = [3, 4]
        result = merge_vectors(v1, v2)

        # Original vectors should be unchanged
        assert len(v1) == 2
        assert v1[0] == 1
        assert v1[1] == 2
        assert len(v2) == 2
        assert v2[0] == 3
        assert v2[1] == 4

        # Result should have all elements
        assert len(result) == 4

    def test_single_element_each(self):
        """Merging single-element vectors should work correctly."""
        v1 = [42]
        v2 = [99]
        result = merge_vectors(v1, v2)
        assert len(result) == 2
        assert result[0] == 42
        assert result[1] == 99

    def test_when_first_none_raises_type_error(self):
        """None as first argument should raise TypeError."""
        with pytest.raises(TypeError):
            merge_vectors(None, [])

    def test_when_second_none_raises_type_error(self):
        """None as second argument should raise TypeError."""
        with pytest.raises(TypeError):
            merge_vectors([], None)
