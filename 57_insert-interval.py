from typing import List
import unittest


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1]),
                ]

        res.append(newInterval)

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        intervals = [[1, 3], [6, 9]]
        newInterval = [2, 5]
        assert Solution().insert(intervals, newInterval) == [[1, 5], [6, 9]]

    def test_2(self):
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInterval = [4, 8]
        assert Solution().insert(intervals, newInterval) == [[1, 2], [3, 10], [12, 16]]

    def test_3(self):
        intervals = []
        newInterval = [5, 7]
        assert Solution().insert(intervals, newInterval) == [[5, 7]]

    def test_4(self):
        intervals = [[1, 5]]
        newInterval = [2, 3]
        assert Solution().insert(intervals, newInterval) == [[1, 5]]

    def test_5(self):
        intervals = [[1, 5]]
        newInterval = [2, 7]
        assert Solution().insert(intervals, newInterval) == [[1, 7]]
