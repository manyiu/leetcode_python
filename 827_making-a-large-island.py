from typing import List
import unittest


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        label_id = -1
        cell_to_label = {}
        label_value = {}

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def label_dfs(r: int, c: int) -> int:
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or grid[r][c] == 0
                or (r, c) in cell_to_label
            ):
                return 0

            cell_to_label[(r, c)] = label_id

            count = 1

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                count += label_dfs(nr, nc)

            return count

        for i in range(ROWS):
            for j in range(COLS):
                label_id += 1

                label_value[label_id] = label_dfs(i, j)

        res = max(label_value.values())

        for i in range(ROWS):
            for j in range(COLS):
                label_set = set()
                val = 0

                for dr, dc in directions:
                    nr = i + dr
                    nc = j + dc

                    if (nr, nc) in cell_to_label and cell_to_label[
                        (nr, nc)
                    ] not in label_set:
                        label_set.add(cell_to_label[(nr, nc)])
                        val += label_value[cell_to_label[(nr, nc)]]

                if grid[i][j] == 0:
                    val += 1

                res = max(res, val)

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        grid = [[1, 0], [0, 1]]
        output = 3
        self.assertEqual(Solution().largestIsland(grid), output)

    def test_2(self):
        grid = [[1, 1], [1, 0]]
        output = 4
        self.assertEqual(Solution().largestIsland(grid), output)

    def test_3(self):
        grid = [[1, 1], [1, 1]]
        output = 4
        self.assertEqual(Solution().largestIsland(grid), output)
