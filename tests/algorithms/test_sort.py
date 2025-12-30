"""
Comprehensive test suite for the algorithms.sort module.
Translated from algorithms.SortTest.java (JUnit 5 to pytest).
"""

import pytest
from sample_project.algorithms.sort import (
    sort_vector,
    dutch_flag_partition,
    max_n,
)


# ============================================================================
# SortVector(list[int] v) tests
# ============================================================================

class TestSortVector:
    """Tests for the sort_vector function."""

    def test_sort_vector_null(self):
        """Exception: None list should raise TypeError"""
        with pytest.raises(TypeError) as exc_info:
            sort_vector(None)
        error_msg = str(exc_info.value).lower()
        assert "none" in error_msg or "null" in error_msg

    def test_sort_vector_empty(self):
        """Edge case: empty list should remain empty"""
        v = []
        sort_vector(v)
        assert len(v) == 0, "Empty list should remain empty"

    def test_sort_vector_single_element(self):
        """Edge case: single element list should remain unchanged"""
        v = [42]
        sort_vector(v)
        expected = [42]
        assert v == expected, "Single element list should remain unchanged"

    def test_sort_vector_already_sorted(self):
        """Already sorted list should remain sorted"""
        v = [1, 2, 3, 4, 5]
        sort_vector(v)
        expected = [1, 2, 3, 4, 5]
        assert v == expected, "Already sorted list should remain sorted"

    def test_sort_vector_reverse_sorted(self):
        """Reverse sorted list should be sorted in ascending order"""
        v = [5, 4, 3, 2, 1]
        sort_vector(v)
        expected = [1, 2, 3, 4, 5]
        assert v == expected, "Reverse sorted list should be sorted ascending"

    def test_sort_vector_random_order(self):
        """Random order list should be sorted in ascending order"""
        v = [3, 1, 4, 1, 5, 9, 2, 6]
        sort_vector(v)
        expected = [1, 1, 2, 3, 4, 5, 6, 9]
        assert v == expected, "Random order list should be sorted ascending"

    def test_sort_vector_with_duplicates(self):
        """List with duplicates should be sorted correctly"""
        v = [3, 1, 3, 2, 1, 2, 3]
        sort_vector(v)
        expected = [1, 1, 2, 2, 3, 3, 3]
        assert v == expected, "List with duplicates should be sorted correctly"

    def test_sort_vector_all_identical(self):
        """List with all identical values should remain unchanged"""
        v = [7, 7, 7, 7, 7]
        sort_vector(v)
        expected = [7, 7, 7, 7, 7]
        assert v == expected, "List with all identical values should remain unchanged"

    def test_sort_vector_with_negatives(self):
        """List with negative numbers should be sorted correctly"""
        v = [-3, 5, -1, 0, 2, -8]
        sort_vector(v)
        expected = [-8, -3, -1, 0, 2, 5]
        assert v == expected, "List with negative numbers should be sorted correctly"


# ============================================================================
# DutchFlagPartition(list[int] v, int pivot) tests
# ============================================================================

class TestDutchFlagPartition:
    """Tests for the dutch_flag_partition function."""

    def test_dutch_flag_partition_null(self):
        """Exception: None list should raise TypeError"""
        with pytest.raises(TypeError) as exc_info:
            dutch_flag_partition(None, 5)
        error_msg = str(exc_info.value).lower()
        assert "none" in error_msg or "null" in error_msg

    def test_dutch_flag_partition_empty(self):
        """Edge case: empty list should remain empty"""
        v = []
        dutch_flag_partition(v, 5)
        assert len(v) == 0, "Empty list should remain empty"

    def test_dutch_flag_partition_single_less_than_pivot(self):
        """Edge case: single element less than pivot"""
        v = [3]
        dutch_flag_partition(v, 5)
        expected = [3]
        assert v == expected, "Single element less than pivot should remain unchanged"

    def test_dutch_flag_partition_single_equal_pivot(self):
        """Edge case: single element equal to pivot"""
        v = [5]
        dutch_flag_partition(v, 5)
        expected = [5]
        assert v == expected, "Single element equal to pivot should remain unchanged"

    def test_dutch_flag_partition_single_greater_than_pivot(self):
        """Edge case: single element greater than pivot"""
        v = [7]
        dutch_flag_partition(v, 5)
        expected = [7]
        msg = "Single element greater than pivot should remain unchanged"
        assert v == expected, msg

    def test_dutch_flag_partition_all_less_than_pivot(self):
        """All elements less than pivot should remain in same relative order"""
        v = [1, 2, 3, 4]
        dutch_flag_partition(v, 10)
        # All elements should be less than pivot
        for val in v:
            assert val < 10, "All elements should be less than pivot"

    def test_dutch_flag_partition_all_equal_pivot(self):
        """All elements equal to pivot"""
        v = [5, 5, 5, 5]
        dutch_flag_partition(v, 5)
        expected = [5, 5, 5, 5]
        assert v == expected, "All elements equal to pivot should remain unchanged"

    def test_dutch_flag_partition_all_greater_than_pivot(self):
        """All elements greater than pivot should remain in same relative order"""
        v = [10, 11, 12, 13]
        dutch_flag_partition(v, 5)
        # All elements should be greater than pivot
        for val in v:
            assert val > 5, "All elements should be greater than pivot"

    def test_dutch_flag_partition_mixed_values(self):
        """Mixed values should be partitioned correctly"""
        v = [3, 5, 2, 5, 1, 8, 5, 9, 4]
        dutch_flag_partition(v, 5)

        # Find boundaries
        first_pivot_or_greater = -1
        first_greater_than_pivot = -1

        for i in range(len(v)):
            if v[i] >= 5 and first_pivot_or_greater == -1:
                first_pivot_or_greater = i
            if v[i] > 5 and first_greater_than_pivot == -1:
                first_greater_than_pivot = i
                break

        # Verify partitioning: less than pivot, equal to pivot, greater than pivot
        for i in range(len(v)):
            if first_pivot_or_greater != -1 and i < first_pivot_or_greater:
                msg = "Elements before pivot section should be less than pivot"
                assert v[i] < 5, msg
            if (
                first_pivot_or_greater != -1
                and first_greater_than_pivot != -1
                and i >= first_pivot_or_greater
                and i < first_greater_than_pivot
            ):
                assert v[i] == 5, "Elements in middle section should equal pivot"
            if first_greater_than_pivot != -1 and i >= first_greater_than_pivot:
                msg = "Elements after pivot section should be greater than pivot"
                assert v[i] > 5, msg

    def test_dutch_flag_partition_no_equal_elements(self):
        """Partition with no elements equal to pivot"""
        v = [1, 2, 3, 7, 8, 9]
        dutch_flag_partition(v, 5)

        # Find the partition point
        partition_index = -1
        for i in range(len(v)):
            if v[i] > 5:
                partition_index = i
                break

        # Verify all elements before partition are < pivot and after are > pivot
        for i in range(len(v)):
            if partition_index != -1 and i < partition_index:
                msg = "Elements before partition should be less than pivot"
                assert v[i] < 5, msg
            if partition_index != -1 and i >= partition_index:
                msg = "Elements after partition should be greater than pivot"
                assert v[i] > 5, msg


# ============================================================================
# MaxN(list[int] v, int n) tests
# ============================================================================

class TestMaxN:
    """Tests for the max_n function."""

    def test_max_n_null(self):
        """Exception: None list should raise TypeError"""
        with pytest.raises(TypeError) as exc_info:
            max_n(None, 3)
        error_msg = str(exc_info.value).lower()
        assert "none" in error_msg or "null" in error_msg

    def test_max_n_negative(self):
        """Exception: negative n should raise ValueError"""
        v = [1, 2, 3, 4, 5]
        with pytest.raises(ValueError) as exc_info:
            max_n(v, -1)
        assert "negative" in str(exc_info.value).lower()

    def test_max_n_zero(self):
        """Exception: n=0 should raise ValueError"""
        v = [1, 2, 3, 4, 5]
        with pytest.raises(ValueError) as exc_info:
            max_n(v, 0)
        assert "between 1" in str(exc_info.value).lower()

    def test_max_n_one(self):
        """Edge case: n=1 should return largest element"""
        v = [3, 1, 4, 1, 5, 9, 2, 6]
        result = max_n(v, 1)
        expected = [9]
        assert result == expected, "max_n with n=1 should return the largest element"

    def test_max_n_equals_size(self):
        """Exception: n equals list size should raise ValueError"""
        v = [1, 2, 3, 4, 5]
        with pytest.raises(ValueError) as exc_info:
            max_n(v, 5)
        assert "between 1" in str(exc_info.value).lower()

    def test_max_n_greater_than_size(self):
        """Exception: n > list size should raise ValueError"""
        v = [1, 2, 3]
        with pytest.raises(ValueError) as exc_info:
            max_n(v, 10)
        assert "between 1" in str(exc_info.value).lower()

    def test_max_n_empty_list(self):
        """Exception: empty list should raise ValueError"""
        v = []
        with pytest.raises(ValueError) as exc_info:
            max_n(v, 3)
        assert "between 1" in str(exc_info.value).lower()

    def test_max_n_normal_case(self):
        """Normal case: return top 3 elements in descending order"""
        v = [3, 1, 4, 1, 5, 9, 2, 6]
        result = max_n(v, 3)
        expected = [9, 6, 5]
        msg = "max_n should return top 3 elements in descending order"
        assert result == expected, msg

    def test_max_n_descending_order(self):
        """Result should be sorted in descending order"""
        v = [10, 5, 20, 15, 25]
        result = max_n(v, 4)
        expected = [25, 20, 15, 10]
        msg = "max_n result should be sorted in descending order"
        assert result == expected, msg

    def test_max_n_with_duplicates(self):
        """Top n with duplicates should handle correctly"""
        v = [5, 5, 3, 5, 1, 2]
        result = max_n(v, 3)
        # Top 3 should be three 5's
        assert len(result) == 3, "Result should have 3 elements"
        assert result[0] == 5, "First element should be 5"
        assert result[1] == 5, "Second element should be 5"
        assert result[2] == 5, "Third element should be 5"

    def test_max_n_with_negatives(self):
        """Top n from list with negative numbers"""
        v = [-5, -1, -10, 3, 0, -2]
        result = max_n(v, 3)
        expected = [3, 0, -1]
        msg = "max_n should correctly find top elements from mixed positive/negative"
        assert result == expected, msg

    def test_max_n_all_identical(self):
        """Top n from list with all identical values"""
        v = [7, 7, 7, 7, 7]
        result = max_n(v, 3)
        expected = [7, 7, 7]
        assert result == expected, "max_n from identical values should return n copies"
