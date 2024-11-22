from typing import List
import unittest


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}

        def dfs(i: int, j: int, prev: int) -> int:
            if (
                i < 0
                or i >= len(matrix)
                or j < 0
                or j >= len(matrix[i])
                or prev >= matrix[i][j]
            ):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

            res = 0

            for dir in directions:
                nextI, nextJ = i + dir[0], j + dir[1]
                res = max(res, 1 + dfs(nextI, nextJ, matrix[i][j]))

            cache[(i, j)] = res

            return res

        res = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                res = max(res, dfs(i, j, -1))

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
        assert Solution().longestIncreasingPath(matrix) == 4

    def test_2(self):
        matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
        assert Solution().longestIncreasingPath(matrix) == 4

    def test_3(self):
        matrix = [[1]]
        assert Solution().longestIncreasingPath(matrix) == 1

    def test_4(self):
        matrix = [[7, 8, 9], [9, 7, 6], [7, 2, 3]]
        assert Solution().longestIncreasingPath(matrix) == 6
