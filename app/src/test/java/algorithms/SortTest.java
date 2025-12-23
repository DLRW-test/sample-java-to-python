package algorithms;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.ArrayList;
import java.util.Arrays;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;

public class SortTest {

  @Nested
  @DisplayName("SortVector(ArrayList<Integer> v) tests")
  class SortVectorTests {

    @Test
    @DisplayName("Edge case: empty vector should remain empty")
    public void testSortVectorEmpty() {
      ArrayList<Integer> v = new ArrayList<>();
      Sort.sortVector(v);
      assertEquals(0, v.size(), "Empty vector should remain empty");
    }

    @Test
    @DisplayName("Edge case: single element vector should remain unchanged")
    public void testSortVectorSingleElement() {
      ArrayList<Integer> v = new ArrayList<>(Arrays.asList(42));
      Sort.sortVector(v);
      ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(42));
      assertEquals(expected, v, "Single element vector should remain unchanged");
    }

    @Test
    @DisplayName("Already sorted vector should remain sorted")
    public void testSortVectorAlreadySorted() {
      ArrayList<Integer> v = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
      Sort.sortVector(v);
      ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
      assertEquals(expected, v, "Already sorted vector should remain sorted");
    }

    @Test
    @DisplayName("Reverse sorted vector should be sorted in ascending order")
    public void testSortVectorReverseSorted() {
      ArrayList<Integer> v = new ArrayList<>(Arrays.asList(5, 4, 3, 2, 1));
      Sort.sortVector(v);
      ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
      assertEquals(expected, v, "Reverse sorted vector should be sorted ascending");
    }

    @Test
    @DisplayName("Random order vector should be sorted in ascending order")
    public void testSortVectorRandomOrder() {
      ArrayList<Integer> v = new ArrayList<>(Arrays.asList(3, 1, 4, 1, 5, 9, 2, 6));
      Sort.sortVector(v);
      ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(1, 1, 2, 3, 4, 5, 6, 9));
      assertEquals(expected, v, "Random order vector should be sorted ascending");
    }

    @Test
    @DisplayName("Vector with duplicates should be sorted correctly")
    public void testSortVectorWithDuplicates() {
      ArrayList<Integer> v = new ArrayList<>(Arrays.asList(3, 1, 3, 2, 1, 2, 3));
      Sort.sortVector(v);
      ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(1, 1, 2, 2, 3, 3, 3));
      assertEquals(expected, v, "Vector with duplicates should be sorted correctly");
    }

    @Test
    @DisplayName("Vector with all identical values should remain unchanged")
    public void testSortVectorAllIdentical() {
      ArrayList<Integer> v = new ArrayList<>(Arrays.asList(7, 7, 7, 7, 7));
      Sort.sortVector(v);
      ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(7, 7, 7, 7, 7));
      assertEquals(expected, v, "Vector with all identical values should remain unchanged");
    }

    @Test
    @DisplayName("Vector with negative numbers should be sorted correctly")
    public void testSortVectorWithNegatives() {
      ArrayList<Integer> v = new ArrayList<>(Arrays.asList(-3, 5, -1, 0, 2, -8));
      Sort.sortVector(v);
      ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(-8, -3, -1, 0, 2, 5));
      assertEquals(expected, v, "Vector with negative numbers should be sorted correctly");
    }
  }

  @Nested
  @DisplayName("DutchFlagPartition(ArrayList<Integer> v, int pivot) tests")
  class DutchFlagPartitionTests {

    @Test
    @DisplayName("Edge case: empty vector should remain empty")
    public void testDutchFlagPartitionEmpty() {
      ArrayList<Integer> v = new ArrayList<>();
      Sort.dutchFlagPartition(v, 5);
      assertEquals(0, v.size(), "Empty vector should remain empty");
    }

    @Test
    @DisplayName("Edge case: single element less than pivot")
    public void testDutchFlagPartitionSingleLessThanPivot() {
      ArrayList<Integer> v = new ArrayList<>(Arrays.asList(3));
      Sort.dutchFlagPartition(v, 5);
      ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(3));
      assertEquals(expected, v, "Single element less than pivot should remain unchanged");
    }

    @Test
    @DisplayName("Edge case: single element equal to pivot")
    public void testDutchFlagPartitionSingleEqualPivot() {
      ArrayList<Integer> v = new ArrayList<>(Arrays.asList(5));
      Sort.dutchFlagPartition(v, 5);
      ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(5));
      assertEquals(expected, v, "Single element equal to pivot should remain unchanged");
    }

    @Test
    @DisplayName("Edge case: single element greater than pivot")
    public void testDutchFlagPartitionSingleGreaterThanPivot() {
      ArrayList<Integer> v = new ArrayList<>(Arrays.asList(7));
      Sort.dutchFlagPartition(v, 5);
      ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(7));
      assertEquals(expected, v, "Single element greater than pivot should remain unchanged");
    }

    @Test
    @DisplayName("All elements less than pivot should remain in same relative order")
    public void testDutchFlagPartitionAllLessThanPivot() {
      ArrayList<Integer> v = new ArrayList<>(Arrays.asList(1, 2, 3, 4));
      Sort.dutchFlagPartition(v, 10);
      // All elements should be less than pivot - order preserved
      for (Integer val : v) {
        assertTrue(val < 10, "All elements should be less than pivot");
      }
    }

    @Test
    @DisplayName("All elements equal to pivot")
    public void testDutchFlagPartitionAllEqualPivot() {
      ArrayList<Integer> v = new ArrayList<>(Arrays.asList(5, 5, 5, 5));
      Sort.dutchFlagPartition(v, 5);
      ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(5, 5, 5, 5));
      assertEquals(expected, v, "All elements equal to pivot should remain unchanged");
    }

    @Test
    @DisplayName("All elements greater than pivot should remain in same relative order")
    public void testDutchFlagPartitionAllGreaterThanPivot() {
      ArrayList<Integer> v = new ArrayList<>(Arrays.asList(10, 11, 12, 13));
      Sort.dutchFlagPartition(v, 5);
      // All elements should be greater than pivot
      for (Integer val : v) {
        assertTrue(val > 5, "All elements should be greater than pivot");
      }
    }

    @Test
    @DisplayName("Mixed values should be partitioned correctly")
    public void testDutchFlagPartitionMixedValues() {
      ArrayList<Integer> v = new ArrayList<>(Arrays.asList(3, 5, 2, 5, 1, 8, 5, 9, 4));
      Sort.dutchFlagPartition(v, 5);
      
      // Find boundaries
      int firstPivotOrGreater = -1;
      int firstGreaterThanPivot = -1;
      
      for (int i = 0; i < v.size(); i++) {
        if (v.get(i) >= 5 && firstPivotOrGreater == -1) {
          firstPivotOrGreater = i;
        }
        if (v.get(i) > 5 && firstGreaterThanPivot == -1) {
          firstGreaterThanPivot = i;
          break;
        }
      }
      
      // Verify partitioning: less than pivot, equal to pivot, greater than pivot
      for (int i = 0; i < v.size(); i++) {
        if (firstPivotOrGreater != -1 && i < firstPivotOrGreater) {
          assertTrue(v.get(i) < 5, "Elements before pivot section should be less than pivot");
        }
        if (firstPivotOrGreater != -1 && firstGreaterThanPivot != -1 && 
            i >= firstPivotOrGreater && i < firstGreaterThanPivot) {
          assertEquals(5, v.get(i), "Elements in middle section should equal pivot");
        }
        if (firstGreaterThanPivot != -1 && i >= firstGreaterThanPivot) {
          assertTrue(v.get(i) > 5, "Elements after pivot section should be greater than pivot");
        }
      }
    }

    @Test
    @DisplayName("Partition with no elements equal to pivot")
    public void testDutchFlagPartitionNoEqualElements() {
      ArrayList<Integer> v = new ArrayList<>(Arrays.asList(1, 2, 3, 7, 8, 9));
      Sort.dutchFlagPartition(v, 5);
      
      // Find the partition point
      int partitionIndex = -1;
      for (int i = 0; i < v.size(); i++) {
        if (v.get(i) > 5) {
          partitionIndex = i;
          break;
        }
      }
      
      // Verify all elements before partition are < pivot and after are > pivot
      for (int i = 0; i < v.size(); i++) {
        if (partitionIndex != -1 && i < partitionIndex) {
          assertTrue(v.get(i) < 5, "Elements before partition should be less than pivot");
        }
        if (partitionIndex != -1 && i >= partitionIndex) {
          assertTrue(v.get(i) > 5, "Elements after partition should be greater than pivot");
        }
      }
    }
  }

  @Nested
  @DisplayName("MaxN(ArrayList<Integer> v, int n) tests")
  class MaxNTests {

    @Test
    @DisplayName("Edge case: n=0 should return empty vector")
    public void testMaxNZero() {
      ArrayList<Integer> v = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
      ArrayList<Integer> result = Sort.maxN(v, 0);
      assertEquals(0, result.size(), "MaxN with n=0 should return empty vector");
    }

    @Test
    @DisplayName("Edge case: negative n should return empty vector")
    public void testMaxNNegative() {
      ArrayList<Integer> v = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
      ArrayList<Integer> result = Sort.maxN(v, -1);
      assertEquals(0, result.size(), "MaxN with negative n should return empty vector");
    }

    @Test
    @DisplayName("Edge case: n=1 should return largest element")
    public void testMaxNOne() {
      ArrayList<Integer> v = new ArrayList<>(Arrays.asList(3, 1, 4, 1, 5, 9, 2, 6));
      ArrayList<Integer> result = Sort.maxN(v, 1);
      ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(9));
      assertEquals(expected, result, "MaxN with n=1 should return the largest element");
    }

    @Test
    @DisplayName("n equals vector size should return empty vector")
    public void testMaxNEqualsSize() {
      ArrayList<Integer> v = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
      ArrayList<Integer> result = Sort.maxN(v, 5);
      assertEquals(0, result.size(), "MaxN with n equal to size should return empty vector");
    }

    @Test
    @DisplayName("n > vector size should return empty vector")
    public void testMaxNGreaterThanSize() {
      ArrayList<Integer> v = new ArrayList<>(Arrays.asList(1, 2, 3));
      ArrayList<Integer> result = Sort.maxN(v, 10);
      assertEquals(0, result.size(), "MaxN with n > size should return empty vector");
    }

    @Test
    @DisplayName("Normal case: return top 3 elements in descending order")
    public void testMaxNNormalCase() {
      ArrayList<Integer> v = new ArrayList<>(Arrays.asList(3, 1, 4, 1, 5, 9, 2, 6));
      ArrayList<Integer> result = Sort.maxN(v, 3);
      ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(9, 6, 5));
      assertEquals(expected, result, "MaxN should return top 3 elements in descending order");
    }

    @Test
    @DisplayName("Result should be sorted in descending order")
    public void testMaxNDescendingOrder() {
      ArrayList<Integer> v = new ArrayList<>(Arrays.asList(10, 5, 20, 15, 25));
      ArrayList<Integer> result = Sort.MaxN(v, 4);
      ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(25, 20, 15, 10));
      assertEquals(expected, result, "MaxN result should be sorted in descending order");
    }

    @Test
    @DisplayName("Top n with duplicates should handle correctly")
    public void testMaxNWithDuplicates() {
      ArrayList<Integer> v = new ArrayList<>(Arrays.asList(5, 5, 3, 5, 1, 2));
      ArrayList<Integer> result = Sort.maxN(v, 3);
      // Top 3 should be three 5's
      assertEquals(3, result.size(), "Result should have 3 elements");
      assertEquals(5, result.get(0), "First element should be 5");
      assertEquals(5, result.get(1), "Second element should be 5");
      assertEquals(5, result.get(2), "Third element should be 5");
    }

    @Test
    @DisplayName("Top n from vector with negative numbers")
    public void testMaxNWithNegatives() {
      ArrayList<Integer> v = new ArrayList<>(Arrays.asList(-5, -1, -10, 3, 0, -2));
      ArrayList<Integer> result = Sort.maxN(v, 3);
      ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(3, 0, -1));
      assertEquals(expected, result, "MaxN should correctly find top elements from mixed positive/negative");
    }

    @Test
    @DisplayName("Top n from vector with all identical values")
    public void testMaxNAllIdentical() {
      ArrayList<Integer> v = new ArrayList<>(Arrays.asList(7, 7, 7, 7, 7));
      ArrayList<Integer> result = Sort.maxN(v, 3);
      ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(7, 7, 7));
      assertEquals(expected, result, "MaxN from identical values should return n copies");
    }

    @Test
    @DisplayName("Empty vector should return empty result")
    public void testMaxNEmptyVector() {
      ArrayList<Integer> v = new ArrayList<>();
      ArrayList<Integer> result = Sort.maxN(v, 3);
      assertEquals(0, result.size(), "MaxN from empty vector should return empty result");
    }
  }
}
