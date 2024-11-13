from typing import List
import unittest


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def dfs(row: int, column: int, init: bool):
            nonlocal res

            if (
                row < 0
                or row >= len(grid)
                or column < 0
                or column >= len(grid[row])
                or grid[row][column] == "0"
            ):
                return

            if init:
                res += 1

            grid[row][column] = "0"

            dfs(row - 1, column, False)
            dfs(row, column - 1, False)
            dfs(row + 1, column, False)
            dfs(row, column + 1, False)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                dfs(i, j, True)

        return res


class TestSolution(unittest.TestCase):

    def test_solution(self):
        solution = Solution()

        self.assertEqual(
            solution.numIslands(
                [
                    ["1", "1", "1", "1", "0"],
                    ["1", "1", "0", "1", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"],
                ]
            ),
            1,
        )

        self.assertEqual(
            solution.numIslands(
                [
                    ["1", "1", "0", "0", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "1", "0", "0"],
                    ["0", "0", "0", "1", "1"],
                ]
            ),
            3,
        )
