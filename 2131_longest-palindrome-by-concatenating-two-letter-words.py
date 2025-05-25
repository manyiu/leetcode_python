from collections import defaultdict
from typing import List
import unittest


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        pair = 0
        self_palindrome = 0
        word_freq = defaultdict(int)

        for word in words:
            word_freq[word] += 1

            if word[0] == word[1]:
                self_palindrome += 1

                if word_freq[word] == 2:
                    pair += 2
                    word_freq[word] = 0
                    self_palindrome -= 2
            elif word_freq[word[1] + word[0]] > 0:
                pair += 2
                word_freq[word] -= 1
                word_freq[word[1] + word[0]] -= 1

        return pair * 2 + min(2, self_palindrome * 2)


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        words = ["lc", "cl", "gg"]
        expected = 6
        result = Solution().longestPalindrome(words)
        self.assertEqual(result, expected)

    def test_example_2(self):
        words = ["ab", "ty", "yt", "lc", "cl", "ab"]
        expected = 8
        result = Solution().longestPalindrome(words)
        self.assertEqual(result, expected)

    def test_example_3(self):
        words = ["cc", "ll", "xx"]
        expected = 2
        result = Solution().longestPalindrome(words)
        self.assertEqual(result, expected)
