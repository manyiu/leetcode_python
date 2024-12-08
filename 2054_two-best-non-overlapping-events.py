import heapq
from typing import List
import unittest


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()

        minHeap = []  # [(end, value)]
        prevMax = 0
        res = 0

        for start, end, value in events:
            while minHeap and minHeap[0][0] < start:
                prevMax = max(prevMax, minHeap[0][1])
                heapq.heappop(minHeap)

            res = max(res, prevMax + value)
            heapq.heappush(minHeap, (end, value))

        return res


class TestSolution(unittest.TestCase):
    def test_0(self):
        events = [[1, 3, 2], [4, 5, 2], [2, 4, 3]]
        assert Solution().maxTwoEvents(events) == 4

    def test_1(self):
        events = [[1, 3, 2], [4, 5, 2], [1, 5, 5]]
        assert Solution().maxTwoEvents(events) == 5

    def test_2(self):
        events = [[1, 5, 3], [1, 5, 1], [6, 6, 5]]
        assert Solution().maxTwoEvents(events) == 8

    def test_3(self):
        events = [
            [66, 97, 90],
            [98, 98, 68],
            [38, 49, 63],
            [91, 100, 42],
            [92, 100, 22],
            [1, 77, 50],
            [64, 72, 97],
        ]
        assert Solution().maxTwoEvents(events) == 165
