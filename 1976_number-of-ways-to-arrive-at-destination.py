from collections import defaultdict
import heapq
from typing import List
import unittest


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7

        adj = defaultdict(list)

        for a, b, w in roads:
            adj[a].append((b, w))
            adj[b].append((a, w))

        min_heap = [(0, 0)]
        dist = [float("inf")] * n
        ways = [0] * n

        dist[0] = 0
        ways[0] = 1

        while min_heap:
            d, node = heapq.heappop(min_heap)

            if d > dist[node]:
                continue

            for nei, w in adj[node]:
                nd = d + w

                if nd < dist[nei]:
                    dist[nei] = nd
                    ways[nei] = ways[node]
                    heapq.heappush(min_heap, (nd, nei))
                elif nd == dist[nei]:
                    ways[nei] += ways[node]

        return ways[n - 1] % MOD


class TestSolution(unittest.TestCase):
    def test_exampmle_1(self):
        n = 7
        roads = [
            [0, 6, 7],
            [0, 1, 2],
            [1, 2, 3],
            [1, 3, 3],
            [6, 3, 3],
            [3, 5, 1],
            [6, 5, 1],
            [2, 5, 1],
            [0, 4, 5],
            [4, 6, 2],
        ]
        output = 4
        self.assertEqual(Solution().countPaths(n, roads), output)

    def test_exampmle_2(self):
        n = 2
        roads = [[1, 0, 10]]
        output = 1
        self.assertEqual(Solution().countPaths(n, roads), output)
