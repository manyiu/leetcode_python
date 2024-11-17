import heapq
from typing import List
import unittest


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minHeap = [(grid[0][0], (0, 0))]
        visit = set()
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        while minHeap:
            weight, pos = heapq.heappop(minHeap)

            if pos in visit:
                continue

            visit.add(pos)

            i, j = pos

            if i == n - 1 and j == n - 1:
                return weight

            for direction in directions:
                iStep, jStep = direction
                iNext, jNext = i + iStep, j + jStep
                if iNext >= 0 and iNext < n and jNext >= 0 and jNext < n:
                    heapq.heappush(
                        minHeap, (max(weight, grid[iNext][jNext]), (iNext, jNext))
                    )

        return -1


class TestSolution(unittest.TestCase):
    def test_1(self):
        grid = [[0, 2], [1, 3]]
        self.assertEqual(Solution().swimInWater(grid), 3)

    def test_2(self):
        grid = [
            [0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6],
        ]
        self.assertEqual(Solution().swimInWater(grid), 16)
