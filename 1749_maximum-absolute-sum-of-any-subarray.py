from typing import List
import unittest


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_abs_sum = 0
        curr_sum = 0
        pre_min = 0
        pre_max = 0

        for num in nums:
            curr_sum += num
            max_abs_sum = max(
                max_abs_sum, abs(curr_sum - pre_min), abs(curr_sum - pre_max)
            )
            pre_min = min(pre_min, curr_sum)
            pre_max = max(pre_max, curr_sum)

        return max_abs_sum


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1, -3, 2, 3, -4]
        output = 5
        self.assertEqual(Solution().maxAbsoluteSum(nums), output)

    def test_2(self):
        nums = [2, -5, 1, -4, 3, -2]
        output = 8
        self.assertEqual(Solution().maxAbsoluteSum(nums), output)
