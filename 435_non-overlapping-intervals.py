from typing import List
import unittest


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort()
        res = 0

        previous = intervals[0]

        for interval in intervals[1:]:
            if interval[0] < previous[1]:
                if interval[1] < previous[1]:
                    previous = interval
                res += 1
            else:
                previous = interval

        return res


class TestSolution(unittest.TestCase):
    def test_0(self):
        intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
        self.assertEqual(Solution().eraseOverlapIntervals(intervals), 1)

    def test_1(self):
        intervals = [[1, 2], [1, 2], [1, 2]]
        self.assertEqual(Solution().eraseOverlapIntervals(intervals), 2)

    def test_2(self):
        intervals = [[1, 2], [2, 3]]
        self.assertEqual(Solution().eraseOverlapIntervals(intervals), 0)

    def test_3(self):
        intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]
        self.assertEqual(Solution().eraseOverlapIntervals(intervals), 2)

    def test_4(self):
        intervals = [[1, 2], [2, 3], [3, 4], [4, 5]]
        self.assertEqual(Solution().eraseOverlapIntervals(intervals), 0)

    def test_5(self):
        intervals = [[1, 2]]
        self.assertEqual(Solution().eraseOverlapIntervals(intervals), 0)

    def test_6(self):
        intervals = []
        self.assertEqual(Solution().eraseOverlapIntervals(intervals), 0)

    def test_7(self):
        intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
        self.assertEqual(Solution().eraseOverlapIntervals(intervals), 1)
