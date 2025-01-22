from collections import deque
from typing import List
import unittest


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROWS = len(isWater)
        COLS = len(isWater[0])

        added = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if isWater[r][c] == 1:
                    q.append((r, c))
                    added.add((r, c))

        res = [[-1 for _ in range(COLS)] for _ in range(ROWS)]

        level = 0

        while q:
            next_q = deque()

            direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]

            for r, c in q:
                res[r][c] = level
                for dr, dc in direction:
                    nr = r + dr
                    nc = c + dc
                    if (
                        nr < 0
                        or nc < 0
                        or nr >= ROWS
                        or nc >= COLS
                        or (nr, nc) in added
                    ):
                        continue
                    next_q.append((nr, nc))
                    added.add((nr, nc))
            q = next_q
            level += 1

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        isWater = [[0, 1], [0, 0]]
        output = [[1, 0], [2, 1]]
        self.assertEqual(Solution().highestPeak(isWater), output)

    def test_2(self):
        isWater = [[0, 0, 1], [1, 0, 0], [0, 0, 0]]
        output = [[1, 1, 0], [0, 1, 1], [1, 2, 2]]
        self.assertEqual(Solution().highestPeak(isWater), output)
