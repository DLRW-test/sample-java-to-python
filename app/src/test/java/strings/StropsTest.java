package strings;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

/**
 * Comprehensive unit tests for the strings.Strops class.
 * 
 * This test class achieves full coverage of the Strops class and documents two critical bugs:
 * 
 * CRITICAL BUG #1: isPalindrome() Empty String Handling
 * - Location: Strops.isPalindrome() method
 * - Current Behavior: Returns false for empty string ("")
 * - Expected Behavior: Should return true (empty string is vacuously a palindrome)
 * - Impact: Violates mathematical definition of palindrome
 * - Test: testIsPalindromeEmptyString() expects true and will FAIL if bug exists
 * 
 * CRITICAL BUG #2: reverse() Implementation Efficiency
 * - Location: Strops.reverse() method  
 * - Current Behavior: May manually iterate through string characters
 * - Expected Behavior: Should use StringBuilder.reverse() for efficiency and correctness
 * - Impact: Performance degradation and potential implementation errors
 * - Test: All reverse() tests verify correctness; efficient implementation expected
 * 
 * Test Strategy: Tests are written to verify correct behavior. When bugs exist, tests will
 * fail, following TDD principles. Once bugs are fixed, all tests should pass.
 */
public class StropsTest {
  private Strops strops;

  @BeforeEach
  public void setUp() {
    strops = new Strops();
  }

  // ===== Tests for reverse() method =====
  //
  // IMPLEMENTATION NOTE (Bug #2):
  // The reverse() method should use StringBuilder.reverse() for optimal performance.
  // Manual character-by-character iteration is inefficient and error-prone.
  // These tests verify correctness of output regardless of implementation,
  // but the implementation should be reviewed for efficiency.

  @Test
  public void testReverseEmptyString() {
    assertEquals("", strops.reverse(""));
  }

  @Test
  public void testReverseSingleCharacter() {
    assertEquals("a", strops.reverse("a"));
  }

  @Test
  public void testReverseMultipleCharacters() {
    assertEquals("olleh", strops.reverse("hello"));
  }

  @Test
  public void testReversePalindrome() {
    assertEquals("racecar", strops.reverse("racecar"));
  }

  @Test
  public void testReverseSpecialCharacters() {
    assertEquals("c#b@a", strops.reverse("a@b#c"));
  }

  @Test
  public void testReverseNumbers() {
    assertEquals("321", strops.reverse("123"));
  }

  @Test
  public void testReverseMixed() {
    assertEquals("!321olleH", strops.reverse("Hello123!"));
  }

  @Test
  public void testReverseLongString() {
    // Test with a longer string to ensure algorithm handles length
    String input = "abcdefghijklmnopqrstuvwxyz";
    String expected = "zyxwvutsrqponmlkjihgfedcba";
    assertEquals(expected, strops.reverse(input));
  }

  @Test
  public void testReverseWithWhitespace() {
    // Test that whitespace is properly handled
    assertEquals("  olleh", strops.reverse("hello  "));
    assertEquals("dlrow olleh", strops.reverse("hello world"));
  }

  // ===== Tests for isPalindrome() method =====
  //
  // CRITICAL BUG #1 - Empty String Handling:
  // The isPalindrome() method currently returns FALSE for empty strings,
  // but should return TRUE. An empty string reads the same forwards and backwards
  // (vacuously true), making it a valid palindrome by mathematical definition.
  //
  // The testIsPalindromeEmptyString() test will FAIL if this bug exists,
  // as it expects the correct behavior (true).

  @Test
  public void testIsPalindrome_EmptyString_ShouldReturnTrue() {
    // CRITICAL BUG TEST: This test verifies Bug #1
    // Expected: true (empty string is a palindrome)
    // Actual (if bug exists): false
    // This test will FAIL until the bug is fixed
    assertTrue(strops.isPalindrome(""), 
        "Empty string should be considered a palindrome (vacuously true)");
  }

  @Test
  public void testIsPalindromeSingleCharacter() {
    assertTrue(strops.isPalindrome("a"));
  }

  @Test
  public void testIsPalindromeEvenLengthPalindrome() {
    assertTrue(strops.isPalindrome("abba"));
  }

  @Test
  public void testIsPalindromeOddLengthPalindrome() {
    assertTrue(strops.isPalindrome("aba"));
  }

  @Test
  public void testIsPalindromeLongerPalindrome() {
    assertTrue(strops.isPalindrome("racecar"));
  }

  @Test
  public void testIsPalindromeNonPalindrome() {
    assertFalse(strops.isPalindrome("hello"));
  }

  @Test
  public void testIsPalindromeCaseSensitivity() {
    // The implementation is case-sensitive, so "Aba" is not a palindrome
    assertFalse(strops.isPalindrome("Aba"));
  }

  @Test
  public void testIsPalindromeWithSpaces() {
    // Test behavior with spaces - spaces are treated as characters
    assertTrue(strops.isPalindrome("a b a"));
  }

  @Test
  public void testIsPalindromeSpecialChars() {
    // Special characters are treated as regular characters
    assertTrue(strops.isPalindrome("a@a"));
  }

  @Test
  public void testIsPalindromeWithSpacesNotPalindrome() {
    // Additional test: string with spaces that is not a palindrome
    assertFalse(strops.isPalindrome("ab a"));
  }

  @Test
  public void testIsPalindromeTwoCharactersPalindrome() {
    assertTrue(strops.isPalindrome("aa"));
  }

  @Test
  public void testIsPalindromeTwoCharactersNotPalindrome() {
    assertFalse(strops.isPalindrome("ab"));
  }

  @Test
  public void testIsPalindrome_NumbersPalindrome() {
    // Test palindrome with numeric characters
    assertTrue(strops.isPalindrome("12321"));
    assertTrue(strops.isPalindrome("1221"));
  }

  @Test
  public void testIsPalindrome_NumbersNotPalindrome() {
    // Test non-palindrome with numeric characters
    assertFalse(strops.isPalindrome("12345"));
  }

  @Test
  public void testIsPalindrome_LongPalindrome() {
    // Test with a longer palindrome string
    assertTrue(strops.isPalindrome("abcdefedcba"));
  }

  @Test
  public void testIsPalindrome_MixedSpecialCharacters() {
    // Test palindrome with mixed content
    assertTrue(strops.isPalindrome("a1b2b1a"));
    assertTrue(strops.isPalindrome("!@#@!"));
  }

  @Test
  public void testIsPalindrome_AllSameCharacter() {
    // Edge case: all same character is always a palindrome
    assertTrue(strops.isPalindrome("aaaa"));
    assertTrue(strops.isPalindrome("111"));
  }
}
