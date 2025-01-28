from typing import List
import unittest


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def helper(r: int, c: int) -> int:
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] <= 0:
                return 0

            count = grid[r][c]

            grid[r][c] = 0

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                count += helper(nr, nc)

            return count

        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, helper(r, c))

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        grid = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]
        output = 7
        self.assertEqual(Solution().findMaxFish(grid), output)

    def test_2(self):
        grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
        output = 1
        self.assertEqual(Solution().findMaxFish(grid), output)
