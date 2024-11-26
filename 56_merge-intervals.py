from typing import List
import unittest


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        res = [intervals[0]]

        for i in intervals[1:]:
            if i[0] <= res[-1][1]:
                res[-1][1] = max(i[1], res[-1][1])
            else:
                res.append(i)

        return res


class TestSolution(unittest.TestCase):
    def test_0(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        res = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(Solution().merge(intervals), res)

    def test_1(self):
        intervals = [[1, 4], [4, 5]]
        res = [[1, 5]]
        self.assertEqual(Solution().merge(intervals), res)

    def test_2(self):
        intervals = [[1, 4], [0, 4]]
        res = [[0, 4]]
        self.assertEqual(Solution().merge(intervals), res)
