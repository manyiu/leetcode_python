from typing import List
import unittest


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return len(intervals)

        starts = [start for start, _ in intervals]
        ends = [end for _, end in intervals]

        starts.sort()
        ends.sort()

        res = 0
        count = 0

        s, e = 0, 0

        while s < len(intervals):
            if starts[s] < ends[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)

        return res


class TestSolution(unittest.TestCase):
    def test_0(self):
        intervals = [[0, 30], [5, 10], [15, 20]]
        self.assertEqual(Solution().minMeetingRooms(intervals), 2)

    def test_1(self):
        intervals = [[7, 10], [2, 4]]
        self.assertEqual(Solution().minMeetingRooms(intervals), 1)

    def test_2(self):
        intervals = [[13, 15], [1, 13]]
        self.assertEqual(Solution().minMeetingRooms(intervals), 1)

    def test_3(self):
        intervals = [[1, 2], [2, 3], [3, 4], [4, 5]]
        self.assertEqual(Solution().minMeetingRooms(intervals), 1)

    def test_4(self):
        intervals = [[1, 2]]
        self.assertEqual(Solution().minMeetingRooms(intervals), 1)

    def test_5(self):
        intervals = []
        self.assertEqual(Solution().minMeetingRooms(intervals), 0)

    def test_6(self):
        intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
        self.assertEqual(Solution().minMeetingRooms(intervals), 2)
