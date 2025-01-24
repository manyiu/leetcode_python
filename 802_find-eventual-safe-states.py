from collections import defaultdict
from typing import List
import unittest


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = {}

        def dfs(node: int) -> bool:
            if node in safe:
                return safe[node]

            safe[node] = False

            for nei in graph[node]:
                if not dfs(nei):
                    safe[node] = False
                    return False

            safe[node] = True

            return True

        res = []

        for i in range(len(graph)):
            if dfs(i):
                res.append(i)

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
        output = [2, 4, 5, 6]
        self.assertEqual(Solution().eventualSafeNodes(graph), output)

    def test_2(self):
        graph = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
        output = [4]
        self.assertEqual(Solution().eventualSafeNodes(graph), output)
