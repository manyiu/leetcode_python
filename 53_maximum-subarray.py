from typing import List
import unittest


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalMax = nums[0]
        localMax = 0

        for num in nums:
            localMax = num + max(localMax, 0)
            globalMax = max(globalMax, localMax)

        return globalMax


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        assert Solution().maxSubArray(nums) == 6

    def test_2(self):
        nums = [1]
        assert Solution().maxSubArray(nums) == 1

    def test_3(self):
        nums = [5, 4, -1, 7, 8]
        assert Solution().maxSubArray(nums) == 23

    def test_4(self):
        nums = [-1]
        assert Solution().maxSubArray(nums) == -1

    def test_5(self):
        nums = [-2, 1]
        assert Solution().maxSubArray(nums) == 1
