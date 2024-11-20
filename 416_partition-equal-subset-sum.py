from typing import List
import unittest


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0

        for num in nums:
            total += num

        if total % 2 != 0:
            return False

        dp = [False] * (total // 2 + 1)
        dp[0] = True

        for num in nums:
            currDp = dp[:]
            for i in range(1, len(dp)):
                if i - num >= 0 and dp[i - num]:
                    currDp[i] = True
            dp = currDp

        return dp[len(dp) - 1]


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1, 5, 11, 5]
        assert Solution().canPartition(nums) == True

    def test_2(self):
        nums = [1, 2, 3, 5]
        assert Solution().canPartition(nums) == False

    def test_3(self):
        nums = [1, 2, 5]
        assert Solution().canPartition(nums) == False

    def test_4(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        assert Solution().canPartition(nums) == True

    def test_5(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8]
        assert Solution().canPartition(nums) == True
