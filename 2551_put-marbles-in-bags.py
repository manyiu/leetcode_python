from heapq import nlargest, nsmallest
from itertools import pairwise
from typing import List
import unittest


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights) - 1

        adj_sum = [0] * n

        for i in range(len(adj_sum)):
            adj_sum[i] = weights[i] + weights[i + 1]

        adj_sum.sort()

        res = 0

        for i in range(k - 1):
            res += adj_sum[n - 1 - i] - adj_sum[i]

        return res

    # def putMarbles(self, weights: List[int], k: int) -> int:
    #     pair_sum = [a + b for a, b in pairwise(weights)]

    #     return sum(nlargest(k - 1, pair_sum)) - sum(nsmallest(k - 1, pair_sum))


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        weights = [1, 3, 5, 1]
        k = 2
        output = 4
        self.assertEqual(Solution().putMarbles(weights, k), output)

    def test_example_2(self):
        weights = [1, 3]
        k = 2
        output = 0
        self.assertEqual(Solution().putMarbles(weights, k), output)
