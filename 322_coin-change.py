from typing import List
import unittest


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("infinity")] * (amount + 1)

        dp[0] = 0

        for i in range(1, len(dp)):
            for j in range(len(coins)):
                if i - coins[j] >= 0:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        if dp[len(dp) - 1] == float("infinity"):
            return -1

        return dp[len(dp) - 1]

    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     minCount = float("infinity")

    #     def dfs(i: int, count: int, target: int):
    #         nonlocal minCount
    #         if target == 0 and count < minCount:
    #             minCount = count
    #             return

    #         if target < 0 or i >= len(coins):
    #             return

    #         dfs(i, count + 1, target - coins[i])
    #         dfs(i + 1, count, target)

    #     dfs(0, 0, amount)

    #     if minCount == float("infinity"):
    #         return -1

    #     return minCount


class TestSolution(unittest.TestCase):
    def test_1(self):
        coins = [1, 2, 5]
        amount = 11
        assert Solution().coinChange(coins, amount) == 3

    def test_2(self):
        coins = [2]
        amount = 3
        assert Solution().coinChange(coins, amount) == -1

    def test_3(self):
        coins = [1]
        amount = 0
        assert Solution().coinChange(coins, amount) == 0
