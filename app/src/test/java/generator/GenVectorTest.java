package generator;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertFalse;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;
import org.junit.jupiter.api.Test;

/**
 * Comprehensive unit tests for GenVector.generateVector() method.
 * 
 * The generateVector() method has been optimized to use ThreadLocalRandom
 * for better performance and thread-safety.
 */
public class GenVectorTest {

  // ==================== Boundary Condition Tests ====================

  @Test
  public void testGenerateVector_EmptyVector() {
    // Test with n=0 should return an empty vector
    ArrayList<Integer> result = GenVector.generateVector(0, 10);
    assertEquals(0, result.size(), "Vector with n=0 should be empty");
  }

  @Test
  public void testGenerateVector_SingleElement() {
    // Test with n=1 should return a vector with exactly one element
    ArrayList<Integer> result = GenVector.generateVector(1, 10);
    assertEquals(1, result.size(), "Vector with n=1 should have size 1");
    assertTrue(result.get(0) >= 0 && result.get(0) < 10, 
        "Single element should be in valid range [0, 10)");
  }

  @Test
  public void testGenerateVector_LargeN() {
    // Test with large n (100+ elements) to verify scalability
    int n = 150;
    int m = 50;
    ArrayList<Integer> result = GenVector.generateVector(n, m);
    assertEquals(n, result.size(), "Vector should have exactly " + n + " elements");
    
    // Verify all elements are in valid range
    for (int i = 0; i < result.size(); i++) {
      int value = result.get(i);
      assertTrue(value >= 0 && value < m, 
          "Element at index " + i + " (" + value + ") should be in range [0, " + m + ")");
    }
  }

  // ==================== Length Verification Tests ====================

  @Test
  public void testGenerateVector_LengthVerification_VariousN() {
    // Test that returned vector length always equals n parameter
    int[] testSizes = {0, 1, 5, 10, 25, 50, 100, 200};
    
    for (int n : testSizes) {
      ArrayList<Integer> result = GenVector.generateVector(n, 100);
      assertEquals(n, result.size(), 
          "Vector length should match parameter n=" + n);
    }
  }

  // ==================== Range Verification Tests ====================

  @Test
  public void testGenerateVector_RangeVerification_SmallM() {
    // Test with small m value (m=10)
    int n = 50;
    int m = 10;
    ArrayList<Integer> result = GenVector.generateVector(n, m);
    
    for (int i = 0; i < result.size(); i++) {
      int value = result.get(i);
      assertTrue(value >= 0, "Element should be non-negative");
      assertTrue(value < m, "Element should be less than m=" + m);
    }
  }

  @Test
  public void testGenerateVector_RangeVerification_MediumM() {
    // Test with medium m value (m=100)
    int n = 50;
    int m = 100;
    ArrayList<Integer> result = GenVector.generateVector(n, m);
    
    for (int i = 0; i < result.size(); i++) {
      int value = result.get(i);
      assertTrue(value >= 0, "Element should be non-negative");
      assertTrue(value < m, "Element should be less than m=" + m);
    }
  }

  @Test
  public void testGenerateVector_RangeVerification_LargeM() {
    // Test with large m value (m=1000)
    int n = 50;
    int m = 1000;
    ArrayList<Integer> result = GenVector.generateVector(n, m);
    
    for (int i = 0; i < result.size(); i++) {
      int value = result.get(i);
      assertTrue(value >= 0, "Element should be non-negative");
      assertTrue(value < m, "Element should be less than m=" + m);
    }
  }

  @Test
  public void testGenerateVector_RangeVerification_VeryLargeM() {
    // Test with very large m value
    int n = 30;
    int m = 10000;
    ArrayList<Integer> result = GenVector.generateVector(n, m);
    
    for (int i = 0; i < result.size(); i++) {
      int value = result.get(i);
      assertTrue(value >= 0, "Element should be non-negative");
      assertTrue(value < m, "Element should be less than m=" + m);
    }
  }

  // ==================== Edge Cases ====================

  @Test
  public void testGenerateVector_EdgeCase_MEqualsOne() {
    // When m=1, all elements should be 0 (only valid value in [0, 1))
    int n = 20;
    int m = 1;
    ArrayList<Integer> result = GenVector.generateVector(n, m);
    
    assertEquals(n, result.size(), "Vector should have correct size");
    for (int i = 0; i < result.size(); i++) {
      assertEquals(0, result.get(i), 
          "When m=1, all elements must be 0 (only value in range [0, 1))");
    }
  }

  @Test
  public void testGenerateVector_EdgeCase_EmptyVectorVariousM() {
    // Empty vector should work regardless of m value
    int[] mValues = {1, 10, 100, 1000};
    
    for (int m : mValues) {
      ArrayList<Integer> result = GenVector.generateVector(0, m);
      assertEquals(0, result.size(), 
          "Empty vector (n=0) should work with m=" + m);
    }
  }

  // ==================== Randomness Verification Tests ====================

  @Test
  public void testGenerateVector_RandomnessCheck_ElementsVary() {
    // Generate multiple vectors and verify elements are not all identical
    // This tests that randomness is working (elements should vary)
    int n = 20;
    int m = 10;
    
    ArrayList<Integer> result1 = GenVector.generateVector(n, m);
    ArrayList<Integer> result2 = GenVector.generateVector(n, m);
    ArrayList<Integer> result3 = GenVector.generateVector(n, m);
    
    // Check that at least one of the vectors differs from the others
    // It's extremely unlikely (but theoretically possible) that all three
    // random vectors would be identical
    boolean result1EqualsResult2 = vectorsEqual(result1, result2);
    boolean result2EqualsResult3 = vectorsEqual(result2, result3);
    boolean result1EqualsResult3 = vectorsEqual(result1, result3);
    
    assertFalse(result1EqualsResult2 && result2EqualsResult3 && result1EqualsResult3,
        "Multiple random vectors should not all be identical (randomness check)");
  }

  @Test
  public void testGenerateVector_RandomnessCheck_NotAllSameValue() {
    // For a reasonably sized vector with sufficient range,
    // not all elements should be the same value
    int n = 50;
    int m = 20;
    
    ArrayList<Integer> result = GenVector.generateVector(n, m);
    
    // Collect unique values
    Set<Integer> uniqueValues = new HashSet<>(result);
    
    // With 50 elements and range [0, 20), we should have multiple distinct values
    // (probability of all being the same is astronomically low)
    assertTrue(uniqueValues.size() > 1, 
        "A vector of " + n + " elements with range [0, " + m + ") should contain " +
        "multiple distinct values (not all identical)");
  }

  @Test
  public void testGenerateVector_RandomnessCheck_DistributionCoverage() {
    // Generate a large vector and verify we get reasonable coverage of the range
    // This is a soft randomness test - with enough elements, we should see
    // multiple different values from the range
    int n = 200;
    int m = 10;
    
    ArrayList<Integer> result = GenVector.generateVector(n, m);
    
    // Count unique values
    Set<Integer> uniqueValues = new HashSet<>(result);
    
    // With 200 elements over range [0, 10), we should see at least
    // several distinct values (typically would see most or all 10 values)
    assertTrue(uniqueValues.size() >= 5, 
        "With " + n + " elements over range [0, " + m + "), should see reasonable " +
        "variety of values (got " + uniqueValues.size() + " distinct values)");
  }

  // ==================== Exception Tests ====================

  @Test
  public void testGenerateVector_NegativeN() {
    // Test that negative n throws IllegalArgumentException
    assertThrows(IllegalArgumentException.class, () -> {
      GenVector.generateVector(-1, 10);
    }, "generateVector() should throw IllegalArgumentException for negative n");
  }

  @Test
  public void testGenerateVector_NegativeM() {
    // Test that negative m throws IllegalArgumentException
    assertThrows(IllegalArgumentException.class, () -> {
      GenVector.generateVector(10, -1);
    }, "generateVector() should throw IllegalArgumentException for negative m");
  }

  @Test
  public void testGenerateVector_ZeroM() {
    // Test that m=0 throws IllegalArgumentException
    assertThrows(IllegalArgumentException.class, () -> {
      GenVector.generateVector(10, 0);
    }, "generateVector() should throw IllegalArgumentException for m=0");
  }

  @Test
  public void testGenerateVector_BothNegative() {
    // Test that both negative parameters throws IllegalArgumentException
    assertThrows(IllegalArgumentException.class, () -> {
      GenVector.generateVector(-5, -10);
    }, "generateVector() should throw IllegalArgumentException when both n and m are negative");
  }

  // ==================== Helper Methods ====================

  /**
   * Helper method to check if two ArrayLists contain the same elements in the same order.
   */
  private boolean vectorsEqual(ArrayList<Integer> v1, ArrayList<Integer> v2) {
    if (v1.size() != v2.size()) {
      return false;
    }
    for (int i = 0; i < v1.size(); i++) {
      if (!v1.get(i).equals(v2.get(i))) {
        return false;
      }
    }
    return true;
  }
}
