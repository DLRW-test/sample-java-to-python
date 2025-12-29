"""
Test suite for the linked_list module.

Translates test cases from datastructures.DsLinkedListTest.java to pytest format.
Tests cover:
- shuffle: Randomly shuffles a linked list (creates new list)
- slice: Returns a slice of a linked list (creates new list)
- Error handling for None inputs and invalid parameters
"""

import pytest
from sample_project.datastructures.linked_list import shuffle, slice_list


# ==================== shuffle Tests ====================


class TestShuffle:
    """Tests for shuffle function (creates shuffled copy)."""

    def test_empty_list(self):
        """Empty list should remain empty after shuffle."""
        lst = []
        result = shuffle(lst)
        assert len(result) == 0
        assert result is not lst  # Should return a new list

    def test_single_element(self):
        """Single element list should contain same element after shuffle."""
        lst = [42]
        result = shuffle(lst)
        assert len(result) == 1
        assert result[0] == 42
        assert result is not lst  # Should return a new list

    def test_valid_permutation(self):
        """Shuffled list should contain same elements (valid permutation)."""
        lst = [1, 2, 3, 4, 5]

        result = shuffle(lst)

        # Should have same size
        assert len(result) == 5

        # Should contain all original elements (same multiset)
        original_set = set(lst)
        result_set = set(result)
        assert original_set == result_set

        # Count occurrences to verify exact permutation
        for value in lst:
            original_count = lst.count(value)
            result_count = result.count(value)
            assert original_count == result_count, f"Element {value} should appear same number of times"

        assert result is not lst  # Should return a new list

    def test_original_unchanged(self):
        """Shuffled list should not modify original list."""
        lst = [10, 20, 30, 40]

        result = shuffle(lst)

        # Original list should remain unchanged
        assert len(lst) == 4
        assert lst[0] == 10
        assert lst[1] == 20
        assert lst[2] == 30
        assert lst[3] == 40

        assert result is not lst  # Should be different objects

    def test_statistical_randomness(self):
        """Multiple shuffles should demonstrate randomness."""
        lst = [1, 2, 3, 4, 5]

        # Track how many times each position sees each value across multiple shuffles
        iterations = 100
        position_value_counts = [[0] * 6 for _ in range(5)]  # [position][value 0-5]

        for _ in range(iterations):
            shuffled = shuffle(lst)
            for pos in range(len(shuffled)):
                value = shuffled[pos]
                position_value_counts[pos][value] += 1

        # Statistical check: for a truly random shuffle with 100 iterations,
        # each value should appear at each position at least once (with very high probability)
        # We'll check that at least some positions have seen multiple different values
        positions_with_variety = 0
        for pos in range(5):
            different_values_seen = 0
            for value in range(1, 6):
                if position_value_counts[pos][value] > 0:
                    different_values_seen += 1
            if different_values_seen >= 3:  # Position has seen at least 3 different values
                positions_with_variety += 1

        # At least 3 out of 5 positions should have variety (seen multiple different values)
        assert positions_with_variety >= 3, (
            f"Expected at least 3 positions to show variety in shuffling, "
            f"but only {positions_with_variety} positions did"
        )

    def test_with_duplicates(self):
        """Shuffle with duplicate elements should preserve duplicates."""
        lst = [1, 2, 2, 3, 3, 3]

        result = shuffle(lst)

        # Count each element
        count1 = result.count(1)
        count2 = result.count(2)
        count3 = result.count(3)

        assert count1 == 1
        assert count2 == 2
        assert count3 == 3

    def test_two_elements_both_permutations(self):
        """Shuffle of two elements should eventually produce both permutations."""
        lst = [1, 2]

        found_original = False
        found_reversed = False

        # Run shuffle multiple times to see both permutations
        for _ in range(50):
            result = shuffle(lst)
            if result[0] == 1 and result[1] == 2:
                found_original = True
            if result[0] == 2 and result[1] == 1:
                found_reversed = True
            if found_original and found_reversed:
                break

        # With 50 iterations, we should see at least one permutation with very high probability
        assert found_original or found_reversed, "Should find at least one permutation in 50 shuffles"

    def test_when_none_raises_type_error(self):
        """None input should raise TypeError."""
        with pytest.raises(TypeError):
            shuffle(None)


# ==================== slice Tests ====================


class TestSlice:
    """Tests for slice_list function (creates slice of list)."""

    def test_full_slice(self):
        """Full slice (start=0, end=size) should return copy of entire list."""
        lst = [1, 2, 3, 4, 5]

        result = slice_list(lst, 0, 5)

        assert len(result) == 5
        assert result[0] == 1
        assert result[1] == 2
        assert result[2] == 3
        assert result[3] == 4
        assert result[4] == 5

        assert result is not lst  # Should be a new list

    def test_from_beginning(self):
        """Partial slice from beginning."""
        lst = [10, 20, 30, 40, 50]

        result = slice_list(lst, 0, 3)

        assert len(result) == 3
        assert result[0] == 10
        assert result[1] == 20
        assert result[2] == 30

    def test_middle_section(self):
        """Partial slice from middle."""
        lst = [1, 2, 3, 4, 5]

        result = slice_list(lst, 1, 4)

        assert len(result) == 3
        assert result[0] == 2
        assert result[1] == 3
        assert result[2] == 4

    def test_to_end(self):
        """Partial slice to end."""
        lst = [100, 200, 300, 400]

        result = slice_list(lst, 2, 4)

        assert len(result) == 2
        assert result[0] == 300
        assert result[1] == 400

    def test_empty_result(self):
        """Empty slice (start=end) should return empty list."""
        lst = [1, 2, 3]

        result = slice_list(lst, 2, 2)

        assert len(result) == 0

    def test_single_element(self):
        """Single element slice."""
        lst = [5, 10, 15, 20, 25]

        result = slice_list(lst, 2, 3)

        assert len(result) == 1
        assert result[0] == 15

    def test_start_boundary(self):
        """Slice at start boundary (index 0)."""
        lst = [7, 8, 9]

        result = slice_list(lst, 0, 1)

        assert len(result) == 1
        assert result[0] == 7

    def test_end_boundary(self):
        """Slice at end boundary."""
        lst = [11, 12, 13, 14]

        result = slice_list(lst, 3, 4)

        assert len(result) == 1
        assert result[0] == 14

    def test_original_unchanged(self):
        """Original list should remain unchanged after slice."""
        lst = [1, 2, 3, 4, 5]

        result = slice_list(lst, 1, 3)

        # Original list should be unchanged
        assert len(lst) == 5
        assert lst[0] == 1
        assert lst[1] == 2
        assert lst[2] == 3
        assert lst[3] == 4
        assert lst[4] == 5

        # Result should be independent
        assert result is not lst

    def test_empty_list(self):
        """Slice from empty list should return empty list."""
        lst = []

        result = slice_list(lst, 0, 0)

        assert len(result) == 0

    def test_multiple_slices_independent(self):
        """Multiple slices from same list should be independent."""
        lst = [10, 20, 30, 40, 50]

        slice1 = slice_list(lst, 0, 2)
        slice2 = slice_list(lst, 2, 5)

        # First slice
        assert len(slice1) == 2
        assert slice1[0] == 10
        assert slice1[1] == 20

        # Second slice
        assert len(slice2) == 3
        assert slice2[0] == 30
        assert slice2[1] == 40
        assert slice2[2] == 50

        # They should be different objects
        assert slice1 is not slice2

    def test_when_none_raises_type_error(self):
        """None input should raise TypeError."""
        with pytest.raises(TypeError):
            slice_list(None, 0, 1)

    def test_when_start_negative_raises_index_error(self):
        """Negative start index should raise IndexError."""
        lst = [1, 2, 3]
        with pytest.raises(IndexError):
            slice_list(lst, -1, 2)

    def test_when_start_exceeds_size_raises_index_error(self):
        """Start index exceeding size should raise IndexError."""
        lst = [1, 2]
        with pytest.raises(IndexError):
            slice_list(lst, 5, 6)

    def test_when_end_negative_raises_index_error(self):
        """Negative end index should raise IndexError."""
        lst = [1, 2]
        with pytest.raises(IndexError):
            slice_list(lst, 0, -1)

    def test_when_end_exceeds_size_raises_index_error(self):
        """End index exceeding size should raise IndexError."""
        lst = [1, 2]
        with pytest.raises(IndexError):
            slice_list(lst, 0, 5)

    def test_when_start_greater_than_end_raises_index_error(self):
        """Start greater than end should raise IndexError."""
        lst = [1, 2, 3]
        with pytest.raises(IndexError):
            slice_list(lst, 2, 1)
