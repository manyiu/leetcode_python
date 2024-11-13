from typing import List
import unittest


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        fresh = set()
        minute = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                elif grid[i][j] == 2:
                    rotten.append((i, j))

        while rotten and len(fresh) > 0:
            nextRotten = []

            for orange in rotten:
                up = (orange[0] - 1, orange[1])
                down = (orange[0] + 1, orange[1])
                left = (orange[0], orange[1] - 1)
                right = (orange[0], orange[1] + 1)

                directions = [up, down, left, right]

                for direction in directions:
                    if direction in fresh:
                        fresh.remove(direction)
                        nextRotten.append(direction)

            rotten = nextRotten
            minute += 1

        if len(fresh) > 0:
            return -1

        return minute


class TestOrangesRotting(unittest.TestCase):
    def test_1(self):
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        self.assertEqual(Solution().orangesRotting(grid), 4)

    def test_2(self):
        grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
        self.assertEqual(Solution().orangesRotting(grid), -1)

    def test_3(self):
        grid = [[0, 2]]
        self.assertEqual(Solution().orangesRotting(grid), 0)
