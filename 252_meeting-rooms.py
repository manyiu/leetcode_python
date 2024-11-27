from typing import List
import unittest


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) <= 1:
            return True

        intervals.sort()
        previousEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start < previousEnd:
                return False
            previousEnd = end

        return True


class TestSolution(unittest.TestCase):
    def test_0(self):
        intervals = [[0, 30], [5, 10], [15, 20]]
        self.assertEqual(Solution().canAttendMeetings(intervals), False)

    def test_1(self):
        intervals = [[7, 10], [2, 4]]
        self.assertEqual(Solution().canAttendMeetings(intervals), True)

    def test_2(self):
        intervals = [[13, 15], [1, 13]]
        self.assertEqual(Solution().canAttendMeetings(intervals), True)

    def test_3(self):
        intervals = [[1, 2], [2, 3], [3, 4], [4, 5]]
        self.assertEqual(Solution().canAttendMeetings(intervals), True)

    def test_4(self):
        intervals = [[1, 2]]
        self.assertEqual(Solution().canAttendMeetings(intervals), True)

    def test_5(self):
        intervals = []
        self.assertEqual(Solution().canAttendMeetings(intervals), True)

    def test_6(self):
        intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
        self.assertEqual(Solution().canAttendMeetings(intervals), False)
