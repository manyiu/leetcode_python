from collections import defaultdict
from typing import List
import unittest


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)
        res = 0

        for a, b in dominoes:
            if a > b:
                a, b = b, a

            res += count[(a, b)]
            count[(a, b)] += 1

        return res


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        dominoes = [[1, 2], [2, 1], [3, 4], [5, 6]]
        expected = 1
        self.assertEqual(Solution().numEquivDominoPairs(dominoes), expected)

    def test_example_2(self):
        dominoes = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
        expected = 3
        self.assertEqual(Solution().numEquivDominoPairs(dominoes), expected)
