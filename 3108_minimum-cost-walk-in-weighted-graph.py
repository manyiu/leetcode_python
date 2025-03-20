from typing import List
import unittest


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, n: int) -> int:
        curr = n

        while curr != self.parent[curr]:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]

        return curr

    def union(self, a: int, b: int) -> bool:
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        if self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
        elif self.rank[root_b] > self.rank[root_a]:
            self.parent[root_a] = root_b
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1

        return True


class Solution:
    def minimumCost(
        self, n: int, edges: List[List[int]], query: List[List[int]]
    ) -> List[int]:
        uf = UnionFind(n)

        for a, b, _ in edges:
            uf.union(a, b)

        root_cost = {}

        for a, b, v in edges:
            root = uf.find(a)

            if root not in root_cost:
                root_cost[root] = v
            else:
                root_cost[root] &= v

        res = [-1] * len(query)

        for i, (a, b) in enumerate(query):
            root_a = uf.find(a)
            root_b = uf.find(b)

            if root_a == root_b:
                res[i] = root_cost[root_a]

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        n = 5
        edges = [[0, 1, 7], [1, 3, 7], [1, 2, 1]]
        query = [[0, 3], [3, 4]]
        output = [1, -1]
        self.assertEqual(Solution().minimumCost(n, edges, query), output)

    def test_2(self):
        n = 3
        edges = [[0, 2, 7], [0, 1, 15], [1, 2, 6], [1, 2, 1]]
        query = [[1, 2]]
        output = [0]
        self.assertEqual(Solution().minimumCost(n, edges, query), output)
