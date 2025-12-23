package datastructures;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertSame;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Vector;
import org.junit.jupiter.api.Test;

public class DsVectorTest {

  // ==================== modifyVector Tests ====================

  @Test
  public void testModifyVector_EmptyVector() {
    Vector<Integer> v = new Vector<>();
    Vector<Integer> result = DsVector.modifyVector(v);
    assertEquals(0, result.size());
    assertSame(v, result); // Verify same reference (in-place modification)
  }

  @Test
  public void testModifyVector_SingleElement() {
    Vector<Integer> v = new Vector<>();
    v.add(5);
    Vector<Integer> result = DsVector.modifyVector(v);
    assertEquals(1, result.size());
    assertEquals(6, result.get(0)); // 5 + 1 = 6
    assertSame(v, result);
  }

  @Test
  public void testModifyVector_MultipleElements() {
    Vector<Integer> v = new Vector<>();
    v.add(1);
    v.add(2);
    v.add(3);
    v.add(4);
    Vector<Integer> result = DsVector.modifyVector(v);
    assertEquals(4, result.size());
    assertEquals(2, result.get(0));
    assertEquals(3, result.get(1));
    assertEquals(4, result.get(2));
    assertEquals(5, result.get(3));
    assertSame(v, result);
  }

  @Test
  public void testModifyVector_WithNegativeNumbers() {
    Vector<Integer> v = new Vector<>();
    v.add(-5);
    v.add(0);
    v.add(10);
    Vector<Integer> result = DsVector.modifyVector(v);
    assertEquals(-4, result.get(0));
    assertEquals(1, result.get(1));
    assertEquals(11, result.get(2));
  }

  // ==================== searchVector Tests ====================

  @Test
  public void testSearchVector_EmptyVector() {
    Vector<Integer> v = new Vector<>();
    Vector<Integer> result = DsVector.searchVector(v, 5);
    assertEquals(0, result.size()); // No matches in empty vector
  }

  @Test
  public void testSearchVector_ElementNotFound() {
    Vector<Integer> v = new Vector<>();
    v.add(1);
    v.add(2);
    v.add(3);
    Vector<Integer> result = DsVector.searchVector(v, 5);
    assertEquals(0, result.size()); // No matches found
  }

  @Test
  public void testSearchVector_SingleMatchAtBeginning() {
    Vector<Integer> v = new Vector<>();
    v.add(10);
    v.add(20);
    v.add(30);
    Vector<Integer> result = DsVector.searchVector(v, 10);
    assertEquals(1, result.size());
    assertEquals(0, result.get(0));
  }

  @Test
  public void testSearchVector_SingleMatchInMiddle() {
    Vector<Integer> v = new Vector<>();
    v.add(10);
    v.add(20);
    v.add(30);
    Vector<Integer> result = DsVector.searchVector(v, 20);
    assertEquals(1, result.size());
    assertEquals(1, result.get(0));
  }

  @Test
  public void testSearchVector_SingleMatchAtEnd() {
    Vector<Integer> v = new Vector<>();
    v.add(10);
    v.add(20);
    v.add(30);
    Vector<Integer> result = DsVector.searchVector(v, 30);
    assertEquals(1, result.size());
    assertEquals(2, result.get(0));
  }

  @Test
  public void testSearchVector_MultipleMatches() {
    Vector<Integer> v = new Vector<>();
    v.add(5);
    v.add(10);
    v.add(5);
    v.add(20);
    v.add(5);
    Vector<Integer> result = DsVector.searchVector(v, 5);
    assertEquals(3, result.size());
    assertEquals(0, result.get(0)); // First match
    assertEquals(2, result.get(1)); // Second match
    assertEquals(4, result.get(2)); // Third match
  }

  // ==================== sortVector Tests ====================

  @Test
  public void testSortVector_EmptyVector() {
    Vector<Integer> v = new Vector<>();
    Vector<Integer> result = DsVector.sortVector(v);
    assertEquals(0, result.size());
  }

  @Test
  public void testSortVector_SingleElement() {
    Vector<Integer> v = new Vector<>();
    v.add(42);
    Vector<Integer> result = DsVector.sortVector(v);
    assertEquals(1, result.size());
    assertEquals(42, result.get(0));
  }

  @Test
  public void testSortVector_AlreadySorted() {
    Vector<Integer> v = new Vector<>();
    v.add(1);
    v.add(2);
    v.add(3);
    v.add(4);
    v.add(5);
    Vector<Integer> result = DsVector.sortVector(v);
    assertEquals(5, result.size());
    assertEquals(1, result.get(0));
    assertEquals(2, result.get(1));
    assertEquals(3, result.get(2));
    assertEquals(4, result.get(3));
    assertEquals(5, result.get(4));
  }

  @Test
  public void testSortVector_ReverseSorted() {
    Vector<Integer> v = new Vector<>();
    v.add(5);
    v.add(4);
    v.add(3);
    v.add(2);
    v.add(1);
    Vector<Integer> result = DsVector.sortVector(v);
    assertEquals(5, result.size());
    assertEquals(1, result.get(0));
    assertEquals(2, result.get(1));
    assertEquals(3, result.get(2));
    assertEquals(4, result.get(3));
    assertEquals(5, result.get(4));
  }

  @Test
  public void testSortVector_WithDuplicates() {
    Vector<Integer> v = new Vector<>();
    v.add(3);
    v.add(1);
    v.add(3);
    v.add(2);
    v.add(1);
    Vector<Integer> result = DsVector.sortVector(v);
    assertEquals(5, result.size());
    assertEquals(1, result.get(0));
    assertEquals(1, result.get(1));
    assertEquals(2, result.get(2));
    assertEquals(3, result.get(3));
    assertEquals(3, result.get(4));
  }

  @Test
  public void testSortVector_RandomOrder() {
    Vector<Integer> v = new Vector<>();
    v.add(9);
    v.add(2);
    v.add(7);
    v.add(1);
    v.add(5);
    Vector<Integer> result = DsVector.sortVector(v);
    assertEquals(5, result.size());
    assertEquals(1, result.get(0));
    assertEquals(2, result.get(1));
    assertEquals(5, result.get(2));
    assertEquals(7, result.get(3));
    assertEquals(9, result.get(4));
  }

  @Test
  public void testSortVector_CreatesNewVector() {
    Vector<Integer> v = new Vector<>();
    v.add(3);
    v.add(1);
    v.add(2);
    Vector<Integer> result = DsVector.sortVector(v);
    // Original should be unchanged
    assertEquals(3, v.get(0));
    assertEquals(1, v.get(1));
    assertEquals(2, v.get(2));
    // Result should be sorted
    assertEquals(1, result.get(0));
    assertEquals(2, result.get(1));
    assertEquals(3, result.get(2));
  }

  @Test
  public void testSortVector_WithNegativeNumbers() {
    Vector<Integer> v = new Vector<>();
    v.add(-5);
    v.add(3);
    v.add(-10);
    v.add(0);
    v.add(7);
    Vector<Integer> result = DsVector.sortVector(v);
    assertEquals(-10, result.get(0));
    assertEquals(-5, result.get(1));
    assertEquals(0, result.get(2));
    assertEquals(3, result.get(3));
    assertEquals(7, result.get(4));
  }

  // ==================== reverseVector Tests ====================

  @Test
  public void testReverseVector_EmptyVector() {
    Vector<Integer> v = new Vector<>();
    Vector<Integer> result = DsVector.reverseVector(v);
    assertEquals(0, result.size());
  }

  @Test
  public void testReverseVector_SingleElement() {
    Vector<Integer> v = new Vector<>();
    v.add(42);
    Vector<Integer> result = DsVector.reverseVector(v);
    assertEquals(1, result.size());
    assertEquals(42, result.get(0));
  }

  @Test
  public void testReverseVector_MultipleElements() {
    Vector<Integer> v = new Vector<>();
    v.add(1);
    v.add(2);
    v.add(3);
    v.add(4);
    v.add(5);
    Vector<Integer> result = DsVector.reverseVector(v);
    assertEquals(5, result.size());
    assertEquals(5, result.get(0));
    assertEquals(4, result.get(1));
    assertEquals(3, result.get(2));
    assertEquals(2, result.get(3));
    assertEquals(1, result.get(4));
  }

  @Test
  public void testReverseVector_CreatesNewVector() {
    Vector<Integer> v = new Vector<>();
    v.add(1);
    v.add(2);
    v.add(3);
    Vector<Integer> result = DsVector.reverseVector(v);
    // Original should be unchanged
    assertEquals(1, v.get(0));
    assertEquals(2, v.get(1));
    assertEquals(3, v.get(2));
    // Result should be reversed
    assertEquals(3, result.get(0));
    assertEquals(2, result.get(1));
    assertEquals(1, result.get(2));
  }

  @Test
  public void testReverseVector_EvenNumberOfElements() {
    Vector<Integer> v = new Vector<>();
    v.add(10);
    v.add(20);
    v.add(30);
    v.add(40);
    Vector<Integer> result = DsVector.reverseVector(v);
    assertEquals(40, result.get(0));
    assertEquals(30, result.get(1));
    assertEquals(20, result.get(2));
    assertEquals(10, result.get(3));
  }

  // ==================== rotateVector Tests ====================

  @Test
  public void testRotateVector_ZeroRotation() {
    Vector<Integer> v = new Vector<>();
    v.add(1);
    v.add(2);
    v.add(3);
    v.add(4);
    Vector<Integer> result = DsVector.rotateVector(v, 0);
    assertEquals(4, result.size());
    assertEquals(1, result.get(0));
    assertEquals(2, result.get(1));
    assertEquals(3, result.get(2));
    assertEquals(4, result.get(3));
  }

  @Test
  public void testRotateVector_FullRotation() {
    Vector<Integer> v = new Vector<>();
    v.add(1);
    v.add(2);
    v.add(3);
    v.add(4);
    Vector<Integer> result = DsVector.rotateVector(v, 4);
    assertEquals(4, result.size());
    assertEquals(1, result.get(0));
    assertEquals(2, result.get(1));
    assertEquals(3, result.get(2));
    assertEquals(4, result.get(3));
  }

  @Test
  public void testRotateVector_NormalRotation() {
    Vector<Integer> v = new Vector<>();
    v.add(1);
    v.add(2);
    v.add(3);
    v.add(4);
    v.add(5);
    Vector<Integer> result = DsVector.rotateVector(v, 2);
    assertEquals(5, result.size());
    assertEquals(3, result.get(0)); // Element at index 2
    assertEquals(4, result.get(1)); // Element at index 3
    assertEquals(5, result.get(2)); // Element at index 4
    assertEquals(1, result.get(3)); // Element at index 0
    assertEquals(2, result.get(4)); // Element at index 1
  }

  @Test
  public void testRotateVector_SingleElement() {
    Vector<Integer> v = new Vector<>();
    v.add(42);
    Vector<Integer> result = DsVector.rotateVector(v, 0);
    assertEquals(1, result.size());
    assertEquals(42, result.get(0));
  }

  @Test
  public void testRotateVector_SingleElementWithRotation() {
    Vector<Integer> v = new Vector<>();
    v.add(42);
    Vector<Integer> result = DsVector.rotateVector(v, 1);
    assertEquals(1, result.size());
    assertEquals(42, result.get(0));
  }

  @Test
  public void testRotateVector_EmptyVector() {
    Vector<Integer> v = new Vector<>();
    Vector<Integer> result = DsVector.rotateVector(v, 5);
    assertEquals(0, result.size());
  }

  @Test
  public void testRotateVector_RotateByOne() {
    Vector<Integer> v = new Vector<>();
    v.add(10);
    v.add(20);
    v.add(30);
    Vector<Integer> result = DsVector.rotateVector(v, 1);
    assertEquals(3, result.size());
    assertEquals(20, result.get(0));
    assertEquals(30, result.get(1));
    assertEquals(10, result.get(2));
  }

  @Test
  public void testRotateVector_CreatesNewVector() {
    Vector<Integer> v = new Vector<>();
    v.add(1);
    v.add(2);
    v.add(3);
    Vector<Integer> result = DsVector.rotateVector(v, 1);
    // Original should be unchanged
    assertEquals(1, v.get(0));
    assertEquals(2, v.get(1));
    assertEquals(3, v.get(2));
  }

  // ==================== mergeVectors Tests ====================

  @Test
  public void testMergeVectors_BothEmpty() {
    Vector<Integer> v1 = new Vector<>();
    Vector<Integer> v2 = new Vector<>();
    Vector<Integer> result = DsVector.mergeVectors(v1, v2);
    assertEquals(0, result.size());
  }

  @Test
  public void testMergeVectors_FirstEmptySecondNonEmpty() {
    Vector<Integer> v1 = new Vector<>();
    Vector<Integer> v2 = new Vector<>();
    v2.add(1);
    v2.add(2);
    v2.add(3);
    Vector<Integer> result = DsVector.mergeVectors(v1, v2);
    assertEquals(3, result.size());
    assertEquals(1, result.get(0));
    assertEquals(2, result.get(1));
    assertEquals(3, result.get(2));
  }

  @Test
  public void testMergeVectors_FirstNonEmptySecondEmpty() {
    Vector<Integer> v1 = new Vector<>();
    v1.add(10);
    v1.add(20);
    Vector<Integer> v2 = new Vector<>();
    Vector<Integer> result = DsVector.mergeVectors(v1, v2);
    assertEquals(2, result.size());
    assertEquals(10, result.get(0));
    assertEquals(20, result.get(1));
  }

  @Test
  public void testMergeVectors_BothNonEmpty() {
    Vector<Integer> v1 = new Vector<>();
    v1.add(1);
    v1.add(2);
    Vector<Integer> v2 = new Vector<>();
    v2.add(3);
    v2.add(4);
    v2.add(5);
    Vector<Integer> result = DsVector.mergeVectors(v1, v2);
    assertEquals(5, result.size());
    assertEquals(1, result.get(0));
    assertEquals(2, result.get(1));
    assertEquals(3, result.get(2));
    assertEquals(4, result.get(3));
    assertEquals(5, result.get(4));
  }

  @Test
  public void testMergeVectors_OrderPreservation() {
    Vector<Integer> v1 = new Vector<>();
    v1.add(100);
    v1.add(200);
    v1.add(300);
    Vector<Integer> v2 = new Vector<>();
    v2.add(10);
    v2.add(20);
    Vector<Integer> result = DsVector.mergeVectors(v1, v2);
    // v1 elements should come first
    assertEquals(100, result.get(0));
    assertEquals(200, result.get(1));
    assertEquals(300, result.get(2));
    // v2 elements should come after
    assertEquals(10, result.get(3));
    assertEquals(20, result.get(4));
  }

  @Test
  public void testMergeVectors_OriginalsUnchanged() {
    Vector<Integer> v1 = new Vector<>();
    v1.add(1);
    v1.add(2);
    Vector<Integer> v2 = new Vector<>();
    v2.add(3);
    v2.add(4);
    Vector<Integer> result = DsVector.mergeVectors(v1, v2);
    
    // Original vectors should be unchanged
    assertEquals(2, v1.size());
    assertEquals(1, v1.get(0));
    assertEquals(2, v1.get(1));
    assertEquals(2, v2.size());
    assertEquals(3, v2.get(0));
    assertEquals(4, v2.get(1));
    
    // Result should have all elements
    assertEquals(4, result.size());
  }

  @Test
  public void testMergeVectors_SingleElementEach() {
    Vector<Integer> v1 = new Vector<>();
    v1.add(42);
    Vector<Integer> v2 = new Vector<>();
    v2.add(99);
    Vector<Integer> result = DsVector.mergeVectors(v1, v2);
    assertEquals(2, result.size());
    assertEquals(42, result.get(0));
    assertEquals(99, result.get(1));
  }
}
