"""
Comprehensive unit tests for the Strops class.

Translated from StropsTest.java. This test suite achieves full coverage of the
Strops class and documents two critical bugs:

CRITICAL BUG #1: isPalindrome() Empty String Handling
- Location: Strops.isPalindrome() method
- Current Behavior: Returns false for empty string ("")
- Expected Behavior: Should return true (empty string is vacuously a palindrome)
- Impact: Violates mathematical definition of palindrome
- Test: test_is_palindrome_empty_string_should_return_true() expects true and
  will FAIL if bug exists

CRITICAL BUG #2: reverse() Implementation Efficiency
- Location: Strops.reverse() method
- Current Behavior: May manually iterate through string characters
- Expected Behavior: Should use efficient string slicing or similar for performance
- Impact: Performance degradation and potential implementation errors
- Test: All reverse() tests verify correctness; efficient implementation expected

Test Strategy: Tests are written to verify correct behavior. When bugs exist,
tests will fail, following TDD principles. Once bugs are fixed, all tests should pass.
"""

import pytest
from sample_project.strings.operations import Strops


@pytest.fixture
def strops() -> Strops:
    """Create a new Strops instance for each test."""
    return Strops()


# ===== Tests for reverse() method =====
#
# IMPLEMENTATION NOTE (Bug #2):
# The reverse() method should use efficient string operations (like slicing)
# for optimal performance. Manual character-by-character iteration is
# inefficient and error-prone. These tests verify correctness of output
# regardless of implementation, but the implementation should be reviewed
# for efficiency.


def test_reverse_empty_string(strops: Strops) -> None:
    """Test reversing an empty string."""
    assert strops.reverse("") == ""


def test_reverse_single_character(strops: Strops) -> None:
    """Test reversing a single character."""
    assert strops.reverse("a") == "a"


def test_reverse_multiple_characters(strops: Strops) -> None:
    """Test reversing a string with multiple characters."""
    assert strops.reverse("hello") == "olleh"


def test_reverse_palindrome(strops: Strops) -> None:
    """Test reversing a palindrome (should return the same string)."""
    assert strops.reverse("racecar") == "racecar"


def test_reverse_special_characters(strops: Strops) -> None:
    """Test reversing a string with special characters."""
    assert strops.reverse("a@b#c") == "c#b@a"


def test_reverse_numbers(strops: Strops) -> None:
    """Test reversing a string with numeric characters."""
    assert strops.reverse("123") == "321"


def test_reverse_mixed(strops: Strops) -> None:
    """Test reversing a string with mixed content."""
    assert strops.reverse("Hello123!") == "!321olleH"


def test_reverse_long_string(strops: Strops) -> None:
    """Test with a longer string to ensure algorithm handles length."""
    input_str = "abcdefghijklmnopqrstuvwxyz"
    expected = "zyxwvutsrqponmlkjihgfedcba"
    assert strops.reverse(input_str) == expected


def test_reverse_with_whitespace(strops: Strops) -> None:
    """Test that whitespace is properly handled."""
    assert strops.reverse("hello  ") == "  olleh"
    assert strops.reverse("hello world") == "dlrow olleh"


def test_reverse_null_string(strops: Strops) -> None:
    """Test that null input raises TypeError."""
    with pytest.raises(TypeError):
        strops.reverse(None)  # type: ignore


# ===== Tests for isPalindrome() method =====
#
# CRITICAL BUG #1 - Empty String Handling:
# The isPalindrome() method currently returns FALSE for empty strings,
# but should return TRUE. An empty string reads the same forwards and backwards
# (vacuously true), making it a valid palindrome by mathematical definition.
#
# The test_is_palindrome_empty_string_should_return_true() test will FAIL if
# this bug exists, as it expects the correct behavior (true).


def test_is_palindrome_empty_string_should_return_true(strops: Strops) -> None:
    """
    CRITICAL BUG TEST: This test verifies Bug #1.
    
    Expected: true (empty string is a palindrome)
    Actual (if bug exists): false
    This test will FAIL until the bug is fixed
    """
    assert strops.is_palindrome(""), (
        "Empty string should be considered a palindrome (vacuously true)"
    )


def test_is_palindrome_single_character(strops: Strops) -> None:
    """Test that a single character is a palindrome."""
    assert strops.is_palindrome("a")


def test_is_palindrome_even_length_palindrome(strops: Strops) -> None:
    """Test even-length palindrome."""
    assert strops.is_palindrome("abba")


def test_is_palindrome_odd_length_palindrome(strops: Strops) -> None:
    """Test odd-length palindrome."""
    assert strops.is_palindrome("aba")


def test_is_palindrome_longer_palindrome(strops: Strops) -> None:
    """Test a longer palindrome."""
    assert strops.is_palindrome("racecar")


def test_is_palindrome_non_palindrome(strops: Strops) -> None:
    """Test that a non-palindrome is correctly identified."""
    assert not strops.is_palindrome("hello")


def test_is_palindrome_case_sensitivity(strops: Strops) -> None:
    """The implementation is case-sensitive, so 'Aba' is not a palindrome."""
    assert not strops.is_palindrome("Aba")


def test_is_palindrome_with_spaces(strops: Strops) -> None:
    """Test behavior with spaces - spaces are treated as characters."""
    assert strops.is_palindrome("a b a")


def test_is_palindrome_special_chars(strops: Strops) -> None:
    """Special characters are treated as regular characters."""
    assert strops.is_palindrome("a@a")


def test_is_palindrome_with_spaces_not_palindrome(strops: Strops) -> None:
    """Additional test: string with spaces that is not a palindrome."""
    assert not strops.is_palindrome("ab a")


def test_is_palindrome_two_characters_palindrome(strops: Strops) -> None:
    """Test two-character palindrome."""
    assert strops.is_palindrome("aa")


def test_is_palindrome_two_characters_not_palindrome(strops: Strops) -> None:
    """Test two-character non-palindrome."""
    assert not strops.is_palindrome("ab")


def test_is_palindrome_numbers_palindrome(strops: Strops) -> None:
    """Test palindrome with numeric characters."""
    assert strops.is_palindrome("12321")
    assert strops.is_palindrome("1221")


def test_is_palindrome_numbers_not_palindrome(strops: Strops) -> None:
    """Test non-palindrome with numeric characters."""
    assert not strops.is_palindrome("12345")


def test_is_palindrome_long_palindrome(strops: Strops) -> None:
    """Test with a longer palindrome string."""
    assert strops.is_palindrome("abcdefedcba")


def test_is_palindrome_mixed_special_characters(strops: Strops) -> None:
    """Test palindrome with mixed content."""
    assert strops.is_palindrome("a1b2b1a")
    assert strops.is_palindrome("!@#@!")


def test_is_palindrome_all_same_character(strops: Strops) -> None:
    """Edge case: all same character is always a palindrome."""
    assert strops.is_palindrome("aaaa")
    assert strops.is_palindrome("111")


def test_is_palindrome_null_string(strops: Strops) -> None:
    """Test that null input raises TypeError."""
    with pytest.raises(TypeError):
        strops.is_palindrome(None)  # type: ignore
