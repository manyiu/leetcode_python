from collections import defaultdict
from typing import Counter
import unittest


class Solution:
    def minimumLength(self, s: str) -> int:
        res = len(s)
        counter = defaultdict(int)

        for c in s:
            counter[c] += 1
            if counter[c] >= 3:
                res -= 2
                counter[c] -= 2

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "abaacbcbb"
        res = 5
        self.assertEqual(res, Solution().minimumLength(s))

    def test_2(self):
        s = "aa"
        res = 2
        self.assertEqual(res, Solution().minimumLength(s))
