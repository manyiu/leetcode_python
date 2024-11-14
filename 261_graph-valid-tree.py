from typing import List
import unittest


class Solution:
    def validTree(self, n: int, edges: List[List[int]]):
        if n == 0:
            return True

        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = set()

        def dfs(node: int, previous: int) -> bool:
            if node in visit:
                return False

            visit.add(node)

            for dest in adj[node]:
                if dest != previous:
                    if not dfs(dest, node):
                        return False

            return True

        return dfs(0, -1) and len(visit) == n


class TestValidTree(unittest.TestCase):
    def test_1(self):
        n = 5
        edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
        self.assertEqual(Solution().validTree(n, edges), True)

    def test_2(self):
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
        self.assertEqual(Solution().validTree(n, edges), False)

    def test_3(self):
        n = 1
        edges = []
        self.assertEqual(Solution().validTree(n, edges), True)

    def test_4(self):
        n = 2
        edges = [[0, 1], [1, 0]]
        self.assertEqual(Solution().validTree(n, edges), False)

    def test_5(self):
        n = 3
        edges = [[0, 1], [1, 2]]
        self.assertEqual(Solution().validTree(n, edges), True)

    def test_6(self):
        n = 3
        edges = [[0, 1], [1, 2], [2, 0]]
        self.assertEqual(Solution().validTree(n, edges), False)

    def test_7(self):
        n = 4
        edges = [[1, 0], [2, 0], [3, 1], [3, 2]]
        self.assertEqual(Solution().validTree(n, edges), False)

    def test_8(self):
        n = 4
        edges = [[1, 0], [2, 0], [3, 1], [3, 2], [0, 3]]
        self.assertEqual(Solution().validTree(n, edges), False)

    def test_9(self):
        n = 4
        edges = [[1, 0], [2, 0], [3, 1], [3, 2], [0, 3], [2, 3]]
        self.assertEqual(Solution().validTree(n, edges), False)
