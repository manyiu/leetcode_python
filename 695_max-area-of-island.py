from typing import List
import unittest


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        def dfs(row: int, column: int) -> int:
            if (
                row < 0
                or row >= len(grid)
                or column < 0
                or column >= len(grid[row])
                or grid[row][column] == 0
            ):
                return 0

            grid[row][column] = 0

            area = (
                1
                + dfs(row - 1, column)
                + dfs(row, column - 1)
                + dfs(row + 1, column)
                + dfs(row, column + 1)
            )

            return area

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                res = max(res, dfs(i, j))

        return res


class TestSolution(unittest.TestCase):

    def test_solution(self):
        solution = Solution()

        self.assertEqual(
            solution.maxAreaOfIsland(
                [
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                ]
            ),
            6,
        )

        self.assertEqual(
            solution.maxAreaOfIsland(
                [
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                ]
            ),
            0,
        )
