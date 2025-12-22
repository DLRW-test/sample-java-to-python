package strings;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class StropsTest {
  private Strops strops;

  @BeforeEach
  public void setUp() {
    strops = new Strops();
  }

  // ===== Tests for reverse() method =====

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

  // ===== Tests for isPalindrome() method =====

  @Test
  public void testIsPalindromeEmptyString() {
    // This test SHOULD FAIL - exposes the critical bug
    // Empty string should be considered a palindrome, but the implementation returns false
    assertTrue(strops.isPalindrome(""));
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
}
