package control;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SingleTest {
  @Test
  public void testSumRange() {
    assertEquals(0, Single.sumRange(0));
    assertEquals(0, Single.sumRange(1));
    assertEquals(1, Single.sumRange(2));
    assertEquals(3, Single.sumRange(3));
    assertEquals(6, Single.sumRange(4));
    assertEquals(45, Single.sumRange(10));
  }

  @Test
  public void testMaxArray() {
    assertEquals(0, Single.maxArray(new int[] { 0 }));
    assertEquals(5, Single.maxArray(new int[] { 1, 2, 3, 4, 5 }));
    assertEquals(1, Single.maxArray(new int[] { 1, 1, 1, 1, 0 }));
    assertEquals(0, Single.maxArray(new int[] { -1, -1, -1, -1, 0 }));
    // Edge case: All-negative array
    assertEquals(-3, Single.maxArray(new int[] { -5, -3, -10 }));
    // Edge case: Mixed positive/negative array
    assertEquals(7, Single.maxArray(new int[] { -5, 3, -10, 7, -2 }));
    // Edge case: Single negative element
    assertEquals(-42, Single.maxArray(new int[] { -42 }));
    // Edge case: All zeros
    assertEquals(0, Single.maxArray(new int[] { 0, 0, 0 }));
  }

  @Test
  public void testSumModulus() {
    assertEquals(0, Single.sumModulus(0, 1));
    assertEquals(0, Single.sumModulus(1, 2));
    assertEquals(0, Single.sumModulus(2, 2));
    assertEquals(2, Single.sumModulus(3, 2));
    assertEquals(2, Single.sumModulus(4, 2));
    assertEquals(20, Single.sumModulus(10, 2));
    assertEquals(18, Single.sumModulus(10, 3));
    assertEquals(12, Single.sumModulus(10, 4));
  }
}