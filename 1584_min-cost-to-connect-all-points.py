import heapq
from typing import List
import unittest


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0

        adj = {}

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(
                    points[i][1] - points[j][1]
                )

                if i not in adj:
                    adj[i] = []
                adj[i].append((dist, j))
                if j not in adj:
                    adj[j] = []
                adj[j].append((dist, i))

        minHeap = []

        for dist, point in adj[0]:
            heapq.heappush(minHeap, (dist, point))

        total = 0

        visit = set()
        visit.add(0)

        while minHeap:
            dist, point = heapq.heappop(minHeap)

            if point in visit:
                continue

            visit.add(point)

            total += dist

            for nextDist, nextPoint in adj[point]:
                heapq.heappush(minHeap, (nextDist, nextPoint))

        return total


class TestSolution(unittest.TestCase):
    def test_1(self):
        points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
        self.assertEqual(Solution().minCostConnectPoints(points), 20)

    def test_2(self):
        points = [[3, 12], [-2, 5], [-4, 1]]
        self.assertEqual(Solution().minCostConnectPoints(points), 18)

    def test_3(self):
        points = [[0, 0], [1, 1], [1, 0], [-1, 1]]
        self.assertEqual(Solution().minCostConnectPoints(points), 4)
