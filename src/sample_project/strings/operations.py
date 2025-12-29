"""String operations class.

This module provides the Strops class for performing string manipulation
operations such as reversal and palindrome checking.
"""


class Strops:
    """String operations utility class.

    An instance-based class providing methods for common string operations
    including reversal and palindrome detection. Operations are case-sensitive
    and whitespace-sensitive.

    Examples:
        >>> strops = Strops()
        >>> strops.reverse("hello")
        'olleh'
        >>> strops.is_palindrome("racecar")
        True
        >>> strops.is_palindrome("hello")
        False
    """

    def reverse(self, s: str) -> str:
        """Reverse a string.

        Takes a string and returns a new string with all characters in
        reverse order. This operation is case-sensitive and preserves all
        characters including whitespace.

        Args:
            s: The string to reverse.

        Returns:
            The reversed string. Returns empty string if input is empty.

        Raises:
            TypeError: If s is None.

        Note:
            Time complexity: O(n) where n is the length of the string.
            Space complexity: O(n) for the reversed string.

        Examples:
            >>> strops = Strops()
            >>> strops.reverse("hello")
            'olleh'
            >>> strops.reverse("Hello World")
            'dlroW olleH'
            >>> strops.reverse("")
            ''
        """
        if s is None:
            raise TypeError("String cannot be None")
        return s[::-1]

    def is_palindrome(self, s: str) -> bool:
        """Check if a string is a palindrome.

        Determines whether the given string reads the same forwards and
        backwards. The check is case-sensitive and whitespace-sensitive.

        Args:
            s: The string to check.

        Returns:
            True if the string is a palindrome, False otherwise.
            Empty strings are considered palindromes.

        Raises:
            TypeError: If s is None.

        Note:
            Time complexity: O(n) where n is the length of the string.
            Space complexity: O(n) for the reversed string comparison.

        Examples:
            >>> strops = Strops()
            >>> strops.is_palindrome("racecar")
            True
            >>> strops.is_palindrome("hello")
            False
            >>> strops.is_palindrome("A man a plan a canal Panama")
            False
            >>> strops.is_palindrome("")
            True
        """
        if s is None:
            raise TypeError("String cannot be None")
        return s == s[::-1]
