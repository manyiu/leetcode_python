from typing import List
import unittest


class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, node: int):
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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for nodeA, nodeB in edges:
            adj[nodeA].append(nodeB)
            adj[nodeB].append(nodeA)

        visit = set()

        def dfs(i) -> bool:
            if i in visit:
                return False

            visit.add(i)

            for dist in adj[i]:
                dfs(dist)

            return True

        count = 0

        for i in range(n):
            if dfs(i):
                count += 1

        return count

    # def countComponents(self, n: int, edges: List[List[int]]) -> int:
    #     uf = UnionFind(n)

    #     for nodeA, nodeB in edges:
    #         uf.union(nodeA, nodeB)

    #     compSet = set()

    #     for i in range(n):
    #         root = uf.find(i)
    #         compSet.add(root)

    #     return len(compSet)


class TestSolution(unittest.TestCase):
    def test_1(self):
        n = 5
        edges = [[0, 1], [1, 2], [3, 4]]
        self.assertEqual(Solution().countComponents(n, edges), 2)

    def test_2(self):
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
        self.assertEqual(Solution().countComponents(n, edges), 1)

    def test_3(self):
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]
        self.assertEqual(Solution().countComponents(n, edges), 1)

    def test_4(self):
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [1, 3]]
        self.assertEqual(Solution().countComponents(n, edges), 1)

    def test_5(self):
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [3, 4], [1, 3]]
        self.assertEqual(Solution().countComponents(n, edges), 1)

    def test_6(self):
        n = 1
        edges = []
        self.assertEqual(Solution().countComponents(n, edges), 1)

    def test_7(self):
        n = 2
        edges = [[0, 1], [1, 0]]
        self.assertEqual(Solution().countComponents(n, edges), 1)

    def test_8(self):
        n = 3
        edges = [[0, 1], [1, 2]]
        self.assertEqual(Solution().countComponents(n, edges), 1)

    def test_9(self):
        n = 3
        edges = [[0, 1], [1, 2], [0, 2]]
        self.assertEqual(Solution().countComponents(n, edges), 1)
