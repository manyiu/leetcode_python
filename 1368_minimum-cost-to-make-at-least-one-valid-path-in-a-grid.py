from collections import deque
import heapq
from typing import List
import unittest


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque([(0, 0, 0)])  # (row, col, cost)
        min_cost = {}

        while q:
            row, col, cost = q.popleft()

            if (row, col) == (ROWS - 1, COLS - 1):
                return cost

            for d, (dr, dc) in enumerate(directions, 1):
                next_row, next_col = row + dr, col + dc
                next_cost = cost if d == grid[row][col] else cost + 1

                if (
                    0 <= next_row < ROWS
                    and 0 <= next_col < COLS
                    and next_cost < min_cost.get((next_row, next_col), float("inf"))
                ):
                    min_cost[(next_row, next_col)] = next_cost

                    if d == grid[row][col]:
                        q.appendleft((next_row, next_col, next_cost))
                    else:
                        q.append((next_row, next_col, next_cost))

    # def minCost(self, grid: List[List[int]]) -> int:
    #     m, n = len(grid), len(grid[0])

    #     visit = set()
    #     visit.add((0, 0))
    #     min_heap = [(0, 0, 0)]  # (cost, row, column)

    #     while min_heap:
    #         cost, row, column = heapq.heappop(min_heap)

    #         if row == m - 1 and column == n - 1:
    #             return cost

    #         visit.add((row, column))

    #         steps = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]

    #         for i in range(1, len(steps)):
    #             next_row = row + steps[i][0]
    #             next_column = column + steps[i][1]
    #             next_cost = cost + (0 if i == grid[row][column] else 1)

    #             if (
    #                 next_row < 0
    #                 or next_row >= m
    #                 or next_column < 0
    #                 or next_column >= n
    #                 or (next_row, next_column) in visit
    #             ):
    #                 continue

    #             heapq.heappush(min_heap, (next_cost, next_row, next_column))


class TestSolution(unittest.TestCase):
    def test_1(self):
        grid = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]
        output = 3
        self.assertEqual(Solution().minCost(grid), output)

    def test_2(self):
        grid = [[1, 1, 3], [3, 2, 2], [1, 1, 4]]
        output = 0
        self.assertEqual(Solution().minCost(grid), output)

    def test_3(self):
        grid = [[1, 2], [4, 3]]
        output = 1
        self.assertEqual(Solution().minCost(grid), output)

    def test_4(self):
        grid = [[2, 2, 2], [2, 2, 2]]
        output = 3
        self.assertEqual(Solution().minCost(grid), output)

    def test_5(self):
        grid = [[4]]
        output = 0
        self.assertEqual(Solution().minCost(grid), output)
