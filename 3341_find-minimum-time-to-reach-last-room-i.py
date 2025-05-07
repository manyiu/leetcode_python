import heapq
from typing import List
import unittest


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        N = len(moveTime)
        M = len(moveTime[0])

        min_heap = [(0, 0, 0)] # (time, r, c)
        visited = set()

        while min_heap:
            time, r, c = heapq.heappop(min_heap)

            if (r, c) in visited:
                continue

            visited.add((r, c))

            if r == N - 1 and c == M - 1:
                return time
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visited:
                    heapq.heappush(min_heap, (max(time + 1, moveTime[nr][nc] + 1), nr, nc))


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        moveTime = [[0,4],[4,4]]
        expected = 6
        self.assertEqual(Solution().minTimeToReach(moveTime), expected)

    def test_example_2(self):
        moveTime = [[0,0,0],[0,0,0]]
        expected = 3
        self.assertEqual(Solution().minTimeToReach(moveTime), expected)

    def test_example_3(self):
        moveTime = [[0,1],[1,2]]
        expected = 3
        self.assertEqual(Solution().minTimeToReach(moveTime), expected)
