import heapq
from typing import List
import unittest


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        ROWS, COLS = len(heightMap), len(heightMap[0])

        min_heap = []

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1:
                    heapq.heappush(min_heap, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1

        res = 0
        max_h = -1

        while min_heap:
            h, r, c = heapq.heappop(min_heap)
            max_h = max(max_h, h)
            res += max_h - h

            direction = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

            for next_r, next_c in direction:
                if (
                    next_r < 0
                    or next_c < 0
                    or next_r >= ROWS
                    or next_c >= COLS
                    or heightMap[next_r][next_c] == -1
                ):
                    continue

                heapq.heappush(min_heap, (heightMap[next_r][next_c], next_r, next_c))
                heightMap[next_r][next_c] = -1

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        heightMap = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
        self.assertEqual(Solution().trapRainWater(heightMap), 4)

    def test_2(self):
        heightMap = [
            [3, 3, 3, 3, 3],
            [3, 2, 2, 2, 3],
            [3, 2, 1, 2, 3],
            [3, 2, 2, 2, 3],
            [3, 3, 3, 3, 3],
        ]
        self.assertEqual(Solution().trapRainWater(heightMap), 10)
