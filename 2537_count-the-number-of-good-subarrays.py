from collections import defaultdict
from typing import List
import unittest


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        N = len(nums)
        count = defaultdict(int)
        res = 0
        pair = 0
        l = 0

        for r in range(N):
            pair += count[nums[r]]
            count[nums[r]] += 1

            while pair >= k:
                res += N - r
                count[nums[l]] -= 1
                pair -= count[nums[l]]
                l += 1

        return res


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        nums = [1, 1, 1, 1, 1]
        k = 10
        expected = 1
        self.assertEqual(Solution().countGood(nums, k), expected)

    def test_example_2(self):
        nums = [3, 1, 4, 3, 2, 2, 4]
        k = 2
        expected = 4
        self.assertEqual(Solution().countGood(nums, k), expected)
