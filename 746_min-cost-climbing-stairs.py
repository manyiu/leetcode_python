from typing import List
import unittest


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [cost[0], cost[1]]

        for i in range(2, len(cost)):
            dp[0], dp[1] = dp[1], cost[i] + min(dp[0], dp[1])

        return min(dp[0], dp[1])

    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     dp = [0] * (len(cost))
    #     dp[0], dp[1] = cost[0], cost[1]

    #     for i in range(2, len(cost)):
    #         dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

    #     return min(dp[len(dp) - 1], dp[len(dp) - 2])

    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     cache = {}

    #     def dfs(i: int) -> int:
    #         if i >= len(cost):
    #             return 0

    #         if i in cache:
    #             return cache[i]

    #         oneStep = cost[i] + dfs(i + 1)
    #         twoStep = cost[i] + dfs(i + 2)
    #         cache[i] = min(oneStep, twoStep)
    #         return cache[i]

    #     return min(dfs(0), dfs(1))

    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     def dfs(i: int) -> int:
    #         if i >= len(cost):
    #             return 0

    #         oneStep = cost[i] + dfs(i + 1)
    #         twoStep = cost[i] + dfs(i + 2)

    #         return min(oneStep, twoStep)

    #     return min(dfs(0), dfs(1))


class TestSolution(unittest.TestCase):
    def test_1(self):
        assert Solution().minCostClimbingStairs([10, 15, 20]) == 15

    def test_2(self):
        assert (
            Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
        )
