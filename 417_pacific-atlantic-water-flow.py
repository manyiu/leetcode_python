from typing import List
import unittest


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        pacific = set()
        atlantic = set()

        def dfs(row: int, column: int, visit: set, previousHeight):
            if (
                row < 0
                or row >= len(heights)
                or column < 0
                or column >= len(heights[row])
                or (row, column) in visit
                or previousHeight > heights[row][column]
            ):
                return

            visit.add((row, column))

            dfs(row - 1, column, visit, heights[row][column])
            dfs(row, column - 1, visit, heights[row][column])
            dfs(row + 1, column, visit, heights[row][column])
            dfs(row, column + 1, visit, heights[row][column])

        for i in range(len(heights)):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, len(heights[i]) - 1, atlantic, heights[i][len(heights[i]) - 1])

        for j in range(len(heights[0])):
            dfs(0, j, pacific, heights[0][j])
            dfs(len(heights) - 1, j, atlantic, heights[len(heights) - 1][j])

        for i in range(len(heights)):
            for j in range(len(heights[i])):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i, j])

        return res


class TestPacificAtlantic(unittest.TestCase):
    def test_1(self):
        heights = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
        self.assertEqual(
            Solution().pacificAtlantic(heights),
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
        )

    def test_2(self):
        heights = [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5],
        ]
        self.assertEqual(
            Solution().pacificAtlantic(heights),
            [[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]],
        )
