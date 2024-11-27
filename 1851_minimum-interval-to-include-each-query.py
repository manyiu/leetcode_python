import heapq
from typing import List
import unittest


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        minHeap = []
        resHash = {}
        i = 0

        for query in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= query:
                heapq.heappush(
                    minHeap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1])
                )
                i += 1

            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)

            if minHeap:
                resHash[query] = minHeap[0][0]
            else:
                resHash[query] = -1

        res = []

        for query in queries:
            res.append(resHash[query])

        return res


class TestSolution(unittest.TestCase):
    def test_0(self):
        intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
        queries = [2, 3, 4, 5]
        self.assertEqual(Solution().minInterval(intervals, queries), [3, 3, 1, 4])

    def test_1(self):
        intervals = [[2, 3], [2, 5], [1, 8], [20, 25]]
        queries = [2, 19, 5, 22]
        self.assertEqual(Solution().minInterval(intervals, queries), [2, -1, 4, 6])

    def test_2(self):
        intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
        queries = [2, 3, 4, 5]
        self.assertEqual(Solution().minInterval(intervals, queries), [3, 3, 1, 4])

    def test_3(self):
        intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
        queries = [2, 3, 4, 5]
        self.assertEqual(Solution().minInterval(intervals, queries), [3, 3, 1, 4])

    def test_4(self):
        intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
        queries = [2, 3, 4, 5]
        self.assertEqual(Solution().minInterval(intervals, queries), [3, 3, 1, 4])

    def test_5(self):
        intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
        queries = [2, 3, 4, 5]
        self.assertEqual(Solution().minInterval(intervals, queries), [3, 3, 1, 4])

    def test_6(self):
        intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
        queries = [2, 3, 4, 5]
        self.assertEqual
