from typing import List
import unittest


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        prefix_row1 = grid[0].copy()
        prefix_row2 = grid[1].copy()

        for i in range(1, N):
            prefix_row1[i] += prefix_row1[i - 1]
            prefix_row2[i] += prefix_row2[i - 1]

        res = float("infinity")

        for i in range(N):
            top = prefix_row1[-1] - prefix_row1[i]
            bottom = prefix_row2[i - 1] if i > 0 else 0
            res = min(res, max(top, bottom))

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        grid = [[2, 5, 4], [1, 5, 1]]
        output = 4
        self.assertEqual(Solution().gridGame(grid), output)

    def test_2(self):
        grid = [[3, 3, 1], [8, 5, 2]]
        output = 4
        self.assertEqual(Solution().gridGame(grid), output)

    def test_3(self):
        grid = [[1, 3, 1, 15], [1, 3, 3, 1]]
        output = 7
        self.assertEqual(Solution().gridGame(grid), output)
