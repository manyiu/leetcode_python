from typing import List
import unittest


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0

        for word in words:
            if word.startswith(pref):
                res += 1
        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        words = ["pay", "attention", "practice", "attend"]
        pref = "att"
        output = 2
        self.assertEqual(Solution().prefixCount(words, pref), output)

    def test_2(self):
        words = ["leetcode", "win", "loops", "success"]
        pref = "code"
        output = 0
        self.assertEqual(Solution().prefixCount(words, pref), output)
