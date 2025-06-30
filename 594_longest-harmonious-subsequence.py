from collections import defaultdict
from typing import List
import unittest


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        accum = defaultdict(int)
        res = 0

        for num in nums:
            accum[num] += 1
        for num in accum:
            if num + 1 in accum:
                res = max(res, accum[num] + accum[num + 1])

        return res


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        nums = [1, 3, 2, 2, 5, 2, 3, 7]
        expected = 5
        actual = Solution().findLHS(nums)
        self.assertEqual(actual, expected)

    def test_example_2(self):
        nums = [1, 2, 3, 4]
        expected = 2
        actual = Solution().findLHS(nums)
        self.assertEqual(actual, expected)

    def test_example_3(self):
        nums = [1, 1, 1, 1]
        expected = 0
        actual = Solution().findLHS(nums)
        self.assertEqual(actual, expected)
