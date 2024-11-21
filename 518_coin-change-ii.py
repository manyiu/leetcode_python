from typing import List
import unittest


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(1, len(dp)):
                if i - coin >= 0:
                    dp[i] += dp[i - coin]

        return dp[amount]


class TestSolution(unittest.TestCase):
    def test_1(self):
        amount = 5
        coins = [1, 2, 5]
        assert Solution().change(amount, coins) == 4

    def test_2(self):
        amount = 3
        coins = [2]
        assert Solution().change(amount, coins) == 0

    def test_3(self):
        amount = 10
        coins = [10]
        assert Solution().change(amount, coins) == 1
