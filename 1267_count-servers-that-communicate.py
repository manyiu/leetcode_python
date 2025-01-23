from typing import List
import unittest


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        row_group = [[] for _ in range(ROWS)]
        col_group = [[] for _ in range(COLS)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    row_group[r].append((r, c))
                    col_group[c].append((r, c))

        res = 0
        visit = set()

        for row in row_group:
            if len(row) >= 2:
                for cell in row:
                    if cell not in visit:
                        res += 1
                    visit.add(cell)

        for col in col_group:
            if len(col) >= 2:
                for cell in col:
                    if cell not in visit:
                        res += 1
                    visit.add(cell)

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        grid = [[1, 0], [0, 1]]
        output = 0
        self.assertEqual(Solution().countServers(grid), output)

    def test_2(self):
        grid = [[1, 0], [1, 1]]
        output = 3
        self.assertEqual(Solution().countServers(grid), output)

    def test_3(self):
        grid = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        output = 4
        self.assertEqual(Solution().countServers(grid), output)
