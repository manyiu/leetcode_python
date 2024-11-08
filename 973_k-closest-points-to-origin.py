import heapq
from typing import List
import unittest


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            minHeap.append((dist, point))

        heapq.heapify(minHeap)

        result = []

        for _ in range(k):
            _, point = heapq.heappop(minHeap)
            result.append(point)

        return result


class TestSolution(unittest.TestCase):
    def test_1(self):
        points = [[1, 3], [-2, 2]]
        k = 1
        res = [[-2, 2]]
        self.assertEqual(Solution().kClosest(points, k), res)

    def test_2(self):
        points = [[3, 3], [5, -1], [-2, 4]]
        k = 2
        res = [[3, 3], [-2, 4]]
        self.assertEqual(Solution().kClosest(points, k), res)
