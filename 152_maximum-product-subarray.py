from typing import List
import unittest


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMin, currMax = 1, 1

        for num in nums:
            currMin, currMax = min(currMin * num, currMax * num, num), max(
                currMin * num, currMax * num, num
            )
            res = max(res, currMax)

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [2, 3, -2, 4]
        assert Solution().maxProduct(nums) == 6

    def test_2(self):
        nums = [-2, 0, -1]
        assert Solution().maxProduct(nums) == 0
