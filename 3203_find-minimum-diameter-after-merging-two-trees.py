import heapq
from math import ceil
from typing import List
import unittest


class Solution:
    def build_adjacency_list(self, edges: List[List[int]]) -> List[List[int]]:
        adjacencyList = [[] for _ in range(len(edges) + 1)]

        for u, v in edges:
            adjacencyList[u].append(v)
            adjacencyList[v].append(u)

        return adjacencyList

    def get_diameter(self, cur: int, par: int, adj: List[List[int]]) -> tuple[int, int]:
        max_d = 0
        max_child_paths = [0, 0]

        for nei in adj[cur]:
            if nei == par:
                continue
            nei_d, nei_max_leaf_path = self.get_diameter(nei, cur, adj)
            max_d = max(max_d, nei_d)
            heapq.heappush(max_child_paths, nei_max_leaf_path)
            heapq.heappop(max_child_paths)

        max_d = max(max_d, sum(max_child_paths))
        return (max_d, 1 + max(max_child_paths))

    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        adj1 = self.build_adjacency_list(edges1)
        adj2 = self.build_adjacency_list(edges2)

        d1, _ = self.get_diameter(0, -1, adj1)
        d2, _ = self.get_diameter(0, -1, adj2)

        return max(d1, d2, 1 + ceil(d1 / 2) + ceil(d2 / 2))


class TestSolution(unittest.TestCase):
    def test_1(self):
        edges1 = [[0, 1], [0, 2], [0, 3]]
        edges2 = [[0, 1]]
        self.assertEqual(Solution().minimumDiameterAfterMerge(edges1, edges2), 3)

    def test_2(self):
        edges1 = [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]]
        edges2 = [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]]
        self.assertEqual(Solution().minimumDiameterAfterMerge(edges1, edges2), 5)
