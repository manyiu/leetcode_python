from collections import Counter
import unittest


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        char_freq = Counter(s)
        odd_freq = 0

        for freq in char_freq.values():
            if freq % 2 == 1:
                odd_freq += 1

        return odd_freq <= k


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "annabelle"
        k = 2
        output = True
        self.assertEqual(Solution().canConstruct(s, k), output)

    def test_2(self):
        s = "leetcode"
        k = 3
        output = False
        self.assertEqual(Solution().canConstruct(s, k), output)

    def test_3(self):
        s = "true"
        k = 4
        output = True
        self.assertEqual(Solution().canConstruct(s, k), output)

    def test_4(self):
        s = "yzyzyzyzyzyzyzy"
        k = 2
        output = True
        self.assertEqual(Solution().canConstruct(s, k), output)
