import heapq
from typing import List
import unittest


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        adj = {}

        for prob, (src, dist) in zip(succProb, edges):
            if src not in adj:
                adj[src] = []
            adj[src].append((prob, dist))
            if dist not in adj:
                adj[dist] = []
            adj[dist].append((prob, src))

        maxHeap = []

        if start_node in adj:
            for prob, dist in adj[start_node]:
                heapq.heappush(maxHeap, (-prob, dist))

        visit = set()

        while maxHeap:
            negProb, dist = heapq.heappop(maxHeap)
            prob = -negProb

            if dist == end_node:
                return prob

            if dist in visit:
                continue

            visit.add(dist)

            if dist in adj:
                for nextProb, nextDist in adj[dist]:
                    heapq.heappush(maxHeap, (-(prob * nextProb), nextDist))

        return 0


class TestSolution(unittest.TestCase):
    def test_1(self):
        n = 3
        edges = [[0, 1], [1, 2], [0, 2]]
        succProb = [0.5, 0.5, 0.2]
        start_node = 0
        end_node = 2
        self.assertEqual(
            Solution().maxProbability(n, edges, succProb, start_node, end_node), 0.25
        )

    def test_2(self):
        n = 3
        edges = [[0, 1], [1, 2], [0, 2]]
        succProb = [0.5, 0.5, 0.3]
        start_node = 0
        end_node = 2
        self.assertEqual(
            Solution().maxProbability(n, edges, succProb, start_node, end_node), 0.3
        )

    def test_3(self):
        n = 3
        edges = [[0, 1]]
        succProb = [0.5]
        start_node = 0
        end_node = 2
        self.assertEqual(
            Solution().maxProbability(n, edges, succProb, start_node, end_node), 0
        )

    def test_4(self):
        n = 5
        edges = [[1, 4], [2, 4], [0, 4], [0, 3], [0, 2], [2, 3]]
        succProb = [0.37, 0.17, 0.93, 0.23, 0.39, 0.04]
        start_node = 3
        end_node = 4
        self.assertEqual(
            Solution().maxProbability(n, edges, succProb, start_node, end_node), 0.2139
        )
