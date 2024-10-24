from typing import List
import unittest


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, maxGain = 10*10*10*10*10, -1

        for price in prices:
            minPrice = min(minPrice, price)
            maxGain = max(maxGain, price - minPrice)

        return max(maxGain, 0)


class TestSolution(unittest.TestCase):
    def test(self):
        prices = [7,1,5,3,6,4]
        self.assertEqual(Solution().maxProfit(prices), 5)
        prices = [7,6,4,3,1]
        self.assertEqual(Solution().maxProfit(prices), 0)
