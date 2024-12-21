from typing import List
import unittest


class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        adj = [[] for _ in range(n)]

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        res = 0

        def dfs(curr, parent):
            nonlocal res

            total = values[curr]

            for child in adj[curr]:
                if child != parent:
                    total += dfs(child, curr)

            if total % k == 0:
                res += 1

            return total

        dfs(0, -1)

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        n = 5
        edges = [[0, 2], [1, 2], [1, 3], [2, 4]]
        values = [1, 8, 1, 4, 4]
        k = 6
        self.assertEqual(Solution().maxKDivisibleComponents(n, edges, values, k), 2)

    def test_2(self):
        n = 7
        edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]
        values = [3, 0, 6, 1, 5, 2, 1]
        k = 3
        self.assertEqual(Solution().maxKDivisibleComponents(n, edges, values, k), 3)
