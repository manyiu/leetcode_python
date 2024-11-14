from typing import List
import unittest


class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, node: int) -> int:
        curr = node

        while self.parent[curr] != curr:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]

        return curr

    def union(self, a: int, b: int) -> bool:
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return False

        if self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        elif self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))

        res = []

        for edge in edges:
            nodeA, nodeB = edge
            if not uf.union(nodeA, nodeB):
                res = edge

        return res


class TestFindRedundantConnection(unittest.TestCase):
    def test_1(self):
        edges = [[1, 2], [1, 3], [2, 3]]
        self.assertEqual(Solution().findRedundantConnection(edges), [2, 3])

    def test_2(self):
        edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
        self.assertEqual(Solution().findRedundantConnection(edges), [1, 4])

    def test_3(self):
        edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5], [2, 5]]
        self.assertEqual(Solution().findRedundantConnection(edges), [2, 5])
