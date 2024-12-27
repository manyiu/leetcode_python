from typing import List
import unittest


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = 0
        curr_max = 0

        for value in values:
            res = max(res, curr_max + value)
            curr_max = max(curr_max, value) - 1

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().maxScoreSightseeingPair([8, 1, 5, 2, 6]), 11)

    def test_2(self):
        self.assertEqual(Solution().maxScoreSightseeingPair([1, 2]), 2)
