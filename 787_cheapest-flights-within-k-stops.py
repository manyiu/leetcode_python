import heapq
from typing import List
import unittest


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        adj = [[] for _ in range(n)]
        dp = [[float("infinity")] * n for _ in range(k + 1)]

        for a, b, cost in flights:
            adj[a].append((cost, b))

        minHeap = [(0, src, -1)]

        while minHeap:
            cost, dist, stops = heapq.heappop(minHeap)

            if dist == dst:
                return cost

            if stops < k:
                for nextCost, nextDist in adj[dist]:
                    newCost = cost + nextCost
                    if newCost < dp[stops + 1][nextDist]:
                        dp[stops + 1][nextDist] = newCost
                        heapq.heappush(minHeap, (newCost, nextDist, stops + 1))

        return -1


class TestSolution(unittest.TestCase):
    def test_0(self):
        n = 4
        flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
        src = 0
        dst = 3
        k = 1
        res = 700
        self.assertEqual(Solution().findCheapestPrice(n, flights, src, dst, k), res)

    def test_1(self):
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 1
        res = 200
        self.assertEqual(Solution().findCheapestPrice(n, flights, src, dst, k), res)

    def test_2(self):
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 0
        res = 500
        self.assertEqual(Solution().findCheapestPrice(n, flights, src, dst, k), res)
