from typing import List
import unittest


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        if len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])

        dp = nums[:]

        dp[2] = nums[0] + nums[2]

        for i in range(3, len(nums)):
            dp[i] = nums[i] + max(dp[i - 3], dp[i - 2])

        return max(dp[len(dp) - 2], dp[len(dp) - 1])

    # def rob(self, nums: List[int]) -> int:
    #     cache = {}

    #     def dfs(i: int) -> int:
    #         if i < 0:
    #             return 0
    #         if i in cache:
    #             return cache[i]

    #         cache[i] = nums[i] + max(dfs(i - 3), dfs(i - 2))
    #         return cache[i]

    #     return max(dfs(len(nums) - 1), dfs(len(nums) - 2))

    # def rob(self, nums: List[int]) -> int:
    #     def dfs(i: int) -> int:
    #         if i < 0:
    #             return 0

    #         return nums[i] + max(dfs(i - 3), dfs(i - 2))

    #     return max(dfs(len(nums) - 1), dfs(len(nums) - 2))


class TestSolution(unittest.TestCase):
    def test_1(self):
        assert Solution().rob([1, 2, 3, 1]) == 4

    def test_2(self):
        assert Solution().rob([2, 7, 9, 3, 1]) == 12
