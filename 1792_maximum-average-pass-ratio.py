import heapq
from typing import List
import unittest


class Solution:
    def profile(self, p: int, t: int) -> float:
        return (p + 1) / (t + 1) - (p / t)

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        maxHeap = [(-self.profile(p, t), p, t) for p, t in classes]
        heapq.heapify(maxHeap)

        for _ in range(extraStudents):
            _, p, t = heapq.heappop(maxHeap)
            newP, newT = p + 1, t + 1
            heapq.heappush(maxHeap, (-self.profile(newP, newT), newP, newT))

        res = 0

        for _, p, t in maxHeap:
            res += p / t

        res /= len(classes)

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        classes = [[1, 2], [3, 5], [2, 2]]
        extraStudents = 2
        res = 0.78333
        self.assertAlmostEqual(
            Solution().maxAverageRatio(classes, extraStudents), res, places=5
        )

    def test_2(self):
        classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
        extraStudents = 4
        res = 0.53485
        self.assertAlmostEqual(
            Solution().maxAverageRatio(classes, extraStudents), res, places=5
        )
