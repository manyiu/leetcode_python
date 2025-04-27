from typing import List
import unittest


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums) - 2):
            if (nums[i] + nums[i + 2]) * 2 == nums[i + 1]:
                res += 1

        return res


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        nums = [1, 2, 1, 4, 1]
        expected = 1
        self.assertEqual(Solution().countSubarrays(nums), expected)

    def test_example_2(self):
        nums = [1, 1, 1]
        expected = 0
        self.assertEqual(Solution().countSubarrays(nums), expected)
