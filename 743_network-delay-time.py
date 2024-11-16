import heapq
from typing import List
import unittest


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        for src, dist, weight in times:
            if src not in adj:
                adj[src] = []
            adj[src].append((dist, weight))

        visit = set()
        visit.add(k)
        minHeap = []

        if k in adj:
            for dist, weight in adj[k]:
                heapq.heappush(minHeap, (weight, dist))

        time = -1

        while minHeap:
            weight, dist = heapq.heappop(minHeap)

            if dist in visit:
                continue

            visit.add(dist)
            time = max(time, weight)

            if dist in adj:
                for nextDist, nextWeight in adj[dist]:
                    heapq.heappush(minHeap, (weight + nextWeight, nextDist))

        if len(visit) != n:
            return -1

        return time


class TestSolution(unittest.TestCase):
    def test_1(self):
        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        n = 4
        k = 2
        self.assertEqual(Solution().networkDelayTime(times, n, k), 2)

    def test_2(self):
        times = [[1, 2, 1]]
        n = 2
        k = 1
        self.assertEqual(Solution().networkDelayTime(times, n, k), 1)

    def test_3(self):
        times = [[1, 2, 1]]
        n = 2
        k = 2
        self.assertEqual(Solution().networkDelayTime(times, n, k), -1)

    def test_4(self):
        times = [[1, 2, 1], [2, 3, 2], [1, 3, 2]]
        n = 3
        k = 1
        self.assertEqual(Solution().networkDelayTime(times, n, k), 2)
