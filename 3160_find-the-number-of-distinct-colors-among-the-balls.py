from collections import defaultdict
from typing import List
import unittest


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = {}
        color_count = defaultdict(int)
        res = [0]

        for ball, color in queries:
            res.append(res[-1])

            if ball in colors:
                color_count[colors[ball]] -= 1

                if color_count[colors[ball]] == 0:
                    res[-1] -= 1

            colors[ball] = color
            color_count[color] += 1

            if color_count[color] == 1:
                res[-1] += 1

        return res[1:]


class TestSolution(unittest.TestCase):
    def test_1(self):
        limit = 4
        queries = [[1, 4], [2, 5], [1, 3], [3, 4]]
        output = [1, 2, 2, 3]
        self.assertEqual(Solution().queryResults(limit, queries), output)

    def test_2(self):
        limit = 4
        queries = [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]
        output = [1, 2, 2, 3, 4]
        self.assertEqual(Solution().queryResults(limit, queries), output)
