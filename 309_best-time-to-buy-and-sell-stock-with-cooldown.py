from typing import List
import unittest


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        buy, prevBuy = -prices[0], 0
        sell, prevSell = 0, 0

        for price in prices:
            prevBuy = buy
            buy = max(prevSell - price, prevBuy)
            prevSell = sell
            sell = max(prevBuy + price, prevSell)

        return sell

    # def maxProfit(self, prices: List[int]) -> int:
    #     def dfs(i: int, hasStock: bool, boughtPrice: int, profit: int) -> int:
    #         if i >= len(prices):
    #             return profit

    #         if hasStock:
    #             sellNow = dfs(i + 2, False, 0, profit + prices[i] - boughtPrice)
    #             sellLater = dfs(i + 1, True, boughtPrice, profit)
    #             return max(sellNow, sellLater)
    #         else:
    #             buyNow = dfs(i + 1, True, prices[i], profit)
    #             buyLater = dfs(i + 1, False, boughtPrice, profit)
    #             return max(buyNow, buyLater)

    #     return dfs(0, False, 0, 0)


class TestSolution(unittest.TestCase):
    def test_1(self):
        prices = [1, 2, 3, 0, 2]
        assert Solution().maxProfit(prices) == 3

    def test_2(self):
        prices = [1]
        assert Solution().maxProfit(prices) == 0
