from typing import List
import unittest


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if (total + target) % 2 != 0 or (total + target) < 0:
            return 0

        sumTarget = (total + target) // 2

        dp = [0] * (sumTarget + 1)
        dp[0] = 1

        for num in nums:
            curr = [0] * (sumTarget + 1)

            for i in range(sumTarget + 1):
                if i - num >= 0:
                    curr[i] = dp[i - num] + dp[i]
                else:
                    curr[i] = dp[i]

            dp = curr

        return dp[sumTarget]


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1, 1, 1, 1, 1]
        target = 3
        assert Solution().findTargetSumWays(nums, target) == 5

    def test_2(self):
        nums = [1]
        target = 1
        assert Solution().findTargetSumWays(nums, target) == 1

    def test_3(self):
        nums = [0, 0, 0, 0, 0, 0, 0, 0, 1]
        target = 1
        assert Solution().findTargetSumWays(nums, target) == 256
