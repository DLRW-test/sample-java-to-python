package datastructures;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotSame;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.Set;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;

public class DsLinkedListTest {

  // ==================== shuffle Tests ====================

  @Nested
  @DisplayName("shuffle(LinkedList<Integer> l) tests")
  class ShuffleTests {

    @Test
    @DisplayName("Empty list should remain empty after shuffle")
    public void testShuffle_EmptyList() {
      LinkedList<Integer> list = new LinkedList<>();
      LinkedList<Integer> result = DsLinkedList.shuffle(list);
      assertEquals(0, result.size());
      assertNotSame(list, result); // Should return a new list
    }

    @Test
    @DisplayName("Single element list should contain same element after shuffle")
    public void testShuffle_SingleElement() {
      LinkedList<Integer> list = new LinkedList<>();
      list.add(42);
      LinkedList<Integer> result = DsLinkedList.shuffle(list);
      assertEquals(1, result.size());
      assertEquals(42, result.get(0));
      assertNotSame(list, result); // Should return a new list
    }

    @Test
    @DisplayName("Shuffled list should contain same elements (valid permutation)")
    public void testShuffle_ValidPermutation() {
      LinkedList<Integer> list = new LinkedList<>();
      list.add(1);
      list.add(2);
      list.add(3);
      list.add(4);
      list.add(5);
      
      LinkedList<Integer> result = DsLinkedList.shuffle(list);
      
      // Should have same size
      assertEquals(5, result.size());
      
      // Should contain all original elements (same multiset)
      Set<Integer> originalSet = new HashSet<>(list);
      Set<Integer> resultSet = new HashSet<>(result);
      assertEquals(originalSet, resultSet);
      
      // Count occurrences to verify exact permutation
      for (Integer value : list) {
        int originalCount = 0;
        int resultCount = 0;
        for (Integer item : list) {
          if (item.equals(value)) originalCount++;
        }
        for (Integer item : result) {
          if (item.equals(value)) resultCount++;
        }
        assertEquals(originalCount, resultCount, "Element " + value + " should appear same number of times");
      }
      
      assertNotSame(list, result); // Should return a new list
    }

    @Test
    @DisplayName("Shuffled list should not modify original list")
    public void testShuffle_OriginalUnchanged() {
      LinkedList<Integer> list = new LinkedList<>();
      list.add(10);
      list.add(20);
      list.add(30);
      list.add(40);
      
      LinkedList<Integer> result = DsLinkedList.shuffle(list);
      
      // Original list should remain unchanged
      assertEquals(4, list.size());
      assertEquals(10, list.get(0));
      assertEquals(20, list.get(1));
      assertEquals(30, list.get(2));
      assertEquals(40, list.get(3));
      
      assertNotSame(list, result); // Should be different objects
    }

    @Test
    @DisplayName("Multiple shuffles should demonstrate randomness")
    public void testShuffle_StatisticalRandomness() {
      LinkedList<Integer> list = new LinkedList<>();
      list.add(1);
      list.add(2);
      list.add(3);
      list.add(4);
      list.add(5);
      
      // Track how many times each position sees each value across multiple shuffles
      int iterations = 100;
      int[][] positionValueCounts = new int[5][6]; // [position][value 0-5]
      
      for (int i = 0; i < iterations; i++) {
        LinkedList<Integer> shuffled = DsLinkedList.shuffle(list);
        for (int pos = 0; pos < shuffled.size(); pos++) {
          int value = shuffled.get(pos);
          positionValueCounts[pos][value]++;
        }
      }
      
      // Statistical check: for a truly random shuffle with 100 iterations,
      // each value should appear at each position at least once (with very high probability)
      // We'll check that at least some positions have seen multiple different values
      int positionsWithVariety = 0;
      for (int pos = 0; pos < 5; pos++) {
        int differentValuesSeen = 0;
        for (int value = 1; value <= 5; value++) {
          if (positionValueCounts[pos][value] > 0) {
            differentValuesSeen++;
          }
        }
        if (differentValuesSeen >= 3) { // Position has seen at least 3 different values
          positionsWithVariety++;
        }
      }
      
      // At least 3 out of 5 positions should have variety (seen multiple different values)
      assertTrue(positionsWithVariety >= 3, 
          "Expected at least 3 positions to show variety in shuffling, but only " 
          + positionsWithVariety + " positions did");
    }

    @Test
    @DisplayName("Shuffle with duplicate elements should preserve duplicates")
    public void testShuffle_WithDuplicates() {
      LinkedList<Integer> list = new LinkedList<>();
      list.add(1);
      list.add(2);
      list.add(2);
      list.add(3);
      list.add(3);
      list.add(3);
      
      LinkedList<Integer> result = DsLinkedList.shuffle(list);
      
      // Count each element
      int count1 = 0, count2 = 0, count3 = 0;
      for (Integer val : result) {
        if (val == 1) count1++;
        else if (val == 2) count2++;
        else if (val == 3) count3++;
      }
      
      assertEquals(1, count1);
      assertEquals(2, count2);
      assertEquals(3, count3);
    }

    @Test
    @DisplayName("Shuffle of two elements should eventually produce both permutations")
    public void testShuffle_TwoElements_BothPermutations() {
      LinkedList<Integer> list = new LinkedList<>();
      list.add(1);
      list.add(2);
      
      boolean foundOriginal = false;
      boolean foundReversed = false;
      
      // Run shuffle multiple times to see both permutations
      for (int i = 0; i < 50; i++) {
        LinkedList<Integer> result = DsLinkedList.shuffle(list);
        if (result.get(0) == 1 && result.get(1) == 2) {
          foundOriginal = true;
        }
        if (result.get(0) == 2 && result.get(1) == 1) {
          foundReversed = true;
        }
        if (foundOriginal && foundReversed) {
          break;
        }
      }
      
      // With 50 iterations, we should see both permutations with very high probability
      assertTrue(foundOriginal || foundReversed, 
          "Should find at least one permutation in 50 shuffles");
    }
  }

  // ==================== slice Tests ====================

  @Nested
  @DisplayName("slice(LinkedList<Integer> l, int start, int end) tests")
  class SliceTests {

    @Test
    @DisplayName("Full slice (start=0, end=size) should return copy of entire list")
    public void testSlice_FullSlice() {
      LinkedList<Integer> list = new LinkedList<>();
      list.add(1);
      list.add(2);
      list.add(3);
      list.add(4);
      list.add(5);
      
      LinkedList<Integer> result = DsLinkedList.slice(list, 0, 5);
      
      assertEquals(5, result.size());
      assertEquals(1, result.get(0));
      assertEquals(2, result.get(1));
      assertEquals(3, result.get(2));
      assertEquals(4, result.get(3));
      assertEquals(5, result.get(4));
      
      assertNotSame(list, result); // Should be a new list
    }

    @Test
    @DisplayName("Partial slice from beginning")
    public void testSlice_FromBeginning() {
      LinkedList<Integer> list = new LinkedList<>();
      list.add(10);
      list.add(20);
      list.add(30);
      list.add(40);
      list.add(50);
      
      LinkedList<Integer> result = DsLinkedList.slice(list, 0, 3);
      
      assertEquals(3, result.size());
      assertEquals(10, result.get(0));
      assertEquals(20, result.get(1));
      assertEquals(30, result.get(2));
    }

    @Test
    @DisplayName("Partial slice from middle")
    public void testSlice_MiddleSection() {
      LinkedList<Integer> list = new LinkedList<>();
      list.add(1);
      list.add(2);
      list.add(3);
      list.add(4);
      list.add(5);
      
      LinkedList<Integer> result = DsLinkedList.slice(list, 1, 4);
      
      assertEquals(3, result.size());
      assertEquals(2, result.get(0));
      assertEquals(3, result.get(1));
      assertEquals(4, result.get(2));
    }

    @Test
    @DisplayName("Partial slice to end")
    public void testSlice_ToEnd() {
      LinkedList<Integer> list = new LinkedList<>();
      list.add(100);
      list.add(200);
      list.add(300);
      list.add(400);
      
      LinkedList<Integer> result = DsLinkedList.slice(list, 2, 4);
      
      assertEquals(2, result.size());
      assertEquals(300, result.get(0));
      assertEquals(400, result.get(1));
    }

    @Test
    @DisplayName("Empty slice (start=end) should return empty list")
    public void testSlice_EmptyResult() {
      LinkedList<Integer> list = new LinkedList<>();
      list.add(1);
      list.add(2);
      list.add(3);
      
      LinkedList<Integer> result = DsLinkedList.slice(list, 2, 2);
      
      assertEquals(0, result.size());
    }

    @Test
    @DisplayName("Single element slice")
    public void testSlice_SingleElement() {
      LinkedList<Integer> list = new LinkedList<>();
      list.add(5);
      list.add(10);
      list.add(15);
      list.add(20);
      list.add(25);
      
      LinkedList<Integer> result = DsLinkedList.slice(list, 2, 3);
      
      assertEquals(1, result.size());
      assertEquals(15, result.get(0));
    }

    @Test
    @DisplayName("Slice at start boundary (index 0)")
    public void testSlice_StartBoundary() {
      LinkedList<Integer> list = new LinkedList<>();
      list.add(7);
      list.add(8);
      list.add(9);
      
      LinkedList<Integer> result = DsLinkedList.slice(list, 0, 1);
      
      assertEquals(1, result.size());
      assertEquals(7, result.get(0));
    }

    @Test
    @DisplayName("Slice at end boundary")
    public void testSlice_EndBoundary() {
      LinkedList<Integer> list = new LinkedList<>();
      list.add(11);
      list.add(12);
      list.add(13);
      list.add(14);
      
      LinkedList<Integer> result = DsLinkedList.slice(list, 3, 4);
      
      assertEquals(1, result.size());
      assertEquals(14, result.get(0));
    }

    @Test
    @DisplayName("Original list should remain unchanged after slice")
    public void testSlice_OriginalUnchanged() {
      LinkedList<Integer> list = new LinkedList<>();
      list.add(1);
      list.add(2);
      list.add(3);
      list.add(4);
      list.add(5);
      
      LinkedList<Integer> result = DsLinkedList.slice(list, 1, 3);
      
      // Original list should be unchanged
      assertEquals(5, list.size());
      assertEquals(1, list.get(0));
      assertEquals(2, list.get(1));
      assertEquals(3, list.get(2));
      assertEquals(4, list.get(3));
      assertEquals(5, list.get(4));
      
      // Result should be independent
      assertNotSame(list, result);
    }

    @Test
    @DisplayName("Slice from empty list should return empty list")
    public void testSlice_EmptyList() {
      LinkedList<Integer> list = new LinkedList<>();
      
      LinkedList<Integer> result = DsLinkedList.slice(list, 0, 0);
      
      assertEquals(0, result.size());
    }

    @Test
    @DisplayName("Multiple slices from same list should be independent")
    public void testSlice_MultipleSlicesIndependent() {
      LinkedList<Integer> list = new LinkedList<>();
      list.add(10);
      list.add(20);
      list.add(30);
      list.add(40);
      list.add(50);
      
      LinkedList<Integer> slice1 = DsLinkedList.slice(list, 0, 2);
      LinkedList<Integer> slice2 = DsLinkedList.slice(list, 2, 5);
      
      // First slice
      assertEquals(2, slice1.size());
      assertEquals(10, slice1.get(0));
      assertEquals(20, slice1.get(1));
      
      // Second slice
      assertEquals(3, slice2.size());
      assertEquals(30, slice2.get(0));
      assertEquals(40, slice2.get(1));
      assertEquals(50, slice2.get(2));
      
      // They should be different objects
      assertNotSame(slice1, slice2);
    }
  }

  // ==================== Error Handling Tests ====================

  @Nested
  @DisplayName("Error Handling Tests")
  class ErrorHandlingTests {

    @Test
    public void testShuffle_whenNull_throwsNullPointerException() {
      assertThrows(NullPointerException.class, () -> {
        DsLinkedList.shuffle(null);
      });
    }

    @Test
    public void testSlice_whenNull_throwsNullPointerException() {
      assertThrows(NullPointerException.class, () -> {
        DsLinkedList.slice(null, 0, 1);
      });
    }

    @Test
    public void testSlice_whenStartNegative_throwsIndexOutOfBoundsException() {
      LinkedList<Integer> list = new LinkedList<>();
      list.add(1);
      list.add(2);
      list.add(3);
      assertThrows(IndexOutOfBoundsException.class, () -> {
        DsLinkedList.slice(list, -1, 2);
      });
    }

    @Test
    public void testSlice_whenStartExceedsSize_throwsIndexOutOfBoundsException() {
      LinkedList<Integer> list = new LinkedList<>();
      list.add(1);
      list.add(2);
      assertThrows(IndexOutOfBoundsException.class, () -> {
        DsLinkedList.slice(list, 5, 6);
      });
    }

    @Test
    public void testSlice_whenEndNegative_throwsIndexOutOfBoundsException() {
      LinkedList<Integer> list = new LinkedList<>();
      list.add(1);
      list.add(2);
      assertThrows(IndexOutOfBoundsException.class, () -> {
        DsLinkedList.slice(list, 0, -1);
      });
    }

    @Test
    public void testSlice_whenEndExceedsSize_throwsIndexOutOfBoundsException() {
      LinkedList<Integer> list = new LinkedList<>();
      list.add(1);
      list.add(2);
      assertThrows(IndexOutOfBoundsException.class, () -> {
        DsLinkedList.slice(list, 0, 5);
      });
    }

    @Test
    public void testSlice_whenStartGreaterThanEnd_throwsIndexOutOfBoundsException() {
      LinkedList<Integer> list = new LinkedList<>();
      list.add(1);
      list.add(2);
      list.add(3);
      assertThrows(IndexOutOfBoundsException.class, () -> {
        DsLinkedList.slice(list, 2, 1);
      });
    }
  }
}
