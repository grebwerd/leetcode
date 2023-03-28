import unittest
import pytest

from interview_questions import printCharactersInString, isPalindrome, isAnagram


class MyTestCase(unittest.TestCase):
    def test_something(self):
        expected = {"h": 1, "e": 1, "l": 2, "o": 1}
        actual = printCharactersInString("hello")
        assert expected == actual, f"expected: {expected} did not match: {actual}"

    def test_isPalidrome(self):
        input = "racecar"
        is_palidrome = isPalindrome(input)
        assert is_palidrome, f"expected string: {input} to be a palindrome, but failed"

    def test_isAnagram(self):
        input_1 = "racecar"
        input_2 = "acecare"
        assert isAnagram(input_1, input_2), f"expected anagrams: {input_1} and {input_2}, but were not"

if __name__ == '__main__':
    unittest.main()
