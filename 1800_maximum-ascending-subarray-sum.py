from typing import List
import unittest


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res, curr = nums[0], nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += nums[i]
                res = max(res, curr)
            else:
                curr = nums[i]

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [10, 20, 30, 5, 10, 50]
        output = 65
        self.assertEqual(Solution().maxAscendingSum(nums), output)

    def test_2(self):
        nums = [10, 20, 30, 40, 50]
        output = 150
        self.assertEqual(Solution().maxAscendingSum(nums), output)

    def test_3(self):
        nums = [12, 17, 15, 13, 10, 11, 12]
        output = 33
        self.assertEqual(Solution().maxAscendingSum(nums), output)
