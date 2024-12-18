from typing import List
import unittest


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stack = []

        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                prices[stack.pop()] -= prices[i]
            stack.append(i)

        return prices

    # def finalPrices(self, prices: List[int]) -> List[int]:
    #     n = len(prices)

    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             if prices[j] <= prices[i]:
    #                 prices[i] = prices[i] - prices[j]
    #                 break

    #     return prices


class TestSolution(unittest.TestCase):
    def test_1(self):
        prices = [8, 4, 6, 2, 3]
        self.assertEqual(Solution().finalPrices(prices), [4, 2, 4, 2, 3])

    def test_2(self):
        prices = [1, 2, 3, 4, 5]
        self.assertEqual(Solution().finalPrices(prices), [1, 2, 3, 4, 5])

    def test_3(self):
        prices = [10, 1, 1, 6]
        self.assertEqual(Solution().finalPrices(prices), [9, 0, 1, 6])
