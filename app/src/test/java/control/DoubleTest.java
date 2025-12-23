package control;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;

public class DoubleTest {
  @Test
  public void testSumSquare() {
    assertEquals(0, Double.sumSquare(1));
    assertEquals(1, Double.sumSquare(2));
    assertEquals(5, Double.sumSquare(3));
    assertEquals(285, Double.sumSquare(10));
  }

  @Test
  public void testSumTriangle() {
    assertEquals(0, Double.sumTriangle(1));
    assertEquals(1, Double.sumTriangle(2));
    assertEquals(4, Double.sumTriangle(3));
    assertEquals(165, Double.sumTriangle(10));
  }

  @Test
  public void testCountPairs() {
    assertEquals(0, Double.countPairs(new int[] { 0 }));
    assertEquals(0, Double.countPairs(new int[] { 1, 2, 3 }));
    assertEquals(0, Double.countPairs(new int[] { 1, 1, 1 }));
    assertEquals(1, Double.countPairs(new int[] { 1, 1, 2 }));
    assertEquals(2, Double.countPairs(new int[] { 1, 1, 2, 2 }));
    assertEquals(3, Double.countPairs(new int[] { 0, 0, 1, 1, 2, 2 }));
    assertEquals(3, Double.countPairs(new int[] { 0, 0, 1, 1, 2, 2, 3 }));
  }

  @Test
  public void testCountDuplicates() {
    assertEquals(1, Double.countDuplicates(new int[] { 0 }, new int[] { 0 }));
    assertEquals(
        0, Double.countDuplicates(new int[] { 1, 2, 3 }, new int[] { 2, 3, 1 }));
    assertEquals(
        1, Double.countDuplicates(new int[] { 1, 1, 1 }, new int[] { 1, 2, 3 }));
    assertEquals(
        2, Double.countDuplicates(new int[] { 1, 1, 2 }, new int[] { 1, 2, 2 }));
    assertEquals(4, Double.countDuplicates(new int[] { 1, 1, 2, 2 },
        new int[] { 1, 1, 2, 2 }));
  }

  @Test
  public void testSumMatrix() {
    assertEquals(0, Double.sumMatrix(new int[][] { { 0 } }));
    assertEquals(6, Double.sumMatrix(new int[][] { { 0, 1 }, { 2, 3 } }));
    assertEquals(
        36, Double.sumMatrix(new int[][] { { 0, 1, 2 }, { 3, 4, 5 }, { 6, 7, 8 } }));
  }

  // ==================== Error Handling Tests ====================

  @Test
  public void testCountPairs_whenNull_throwsNullPointerException() {
    assertThrows(NullPointerException.class, () -> {
      Double.countPairs(null);
    });
  }

  @Test
  public void testCountDuplicates_whenFirstArrayNull_throwsNullPointerException() {
    assertThrows(NullPointerException.class, () -> {
      Double.countDuplicates(null, new int[] {1, 2, 3});
    });
  }

  @Test
  public void testCountDuplicates_whenSecondArrayNull_throwsNullPointerException() {
    assertThrows(NullPointerException.class, () -> {
      Double.countDuplicates(new int[] {1, 2, 3}, null);
    });
  }

  @Test
  public void testCountDuplicates_whenLengthMismatch_throwsIllegalArgumentException() {
    assertThrows(IllegalArgumentException.class, () -> {
      Double.countDuplicates(new int[] {1, 2}, new int[] {1, 2, 3});
    });
  }

  @Test
  public void testSumMatrix_whenNull_throwsNullPointerException() {
    assertThrows(NullPointerException.class, () -> {
      Double.sumMatrix(null);
    });
  }

  @Test
  public void testSumMatrix_whenRowNull_throwsNullPointerException() {
    assertThrows(NullPointerException.class, () -> {
      Double.sumMatrix(new int[][] { {1, 2}, null });
    });
  }

  @Test
  public void testSumMatrix_whenNotSquare_throwsIllegalArgumentException() {
    assertThrows(IllegalArgumentException.class, () -> {
      Double.sumMatrix(new int[][] { {1, 2, 3}, {4, 5} });
    });
  }
}
