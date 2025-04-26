from typing import List
import unittest


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        min_i = max_i = bad_i = -1
        res = 0

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                bad_i = i
            if num == minK:
                min_i = i
            if num == maxK:
                max_i = i

            res += max(0, min(min_i, max_i) - bad_i)

        return res


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        nums = [1, 3, 5, 2, 7, 5]
        minK = 1
        maxK = 5
        expected = 2
        self.assertEqual(Solution().countSubarrays(nums, minK, maxK), expected)

    def test_example_2(self):
        nums = [1, 1, 1, 1]
        minK = 1
        maxK = 1
        expected = 10
        self.assertEqual(Solution().countSubarrays(nums, minK, maxK), expected)
