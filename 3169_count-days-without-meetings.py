from typing import List
import unittest


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        last_day = 0

        res = 0

        for i in range(len(meetings)):
            if meetings[i][0] > last_day:
                res += meetings[i][0] - last_day - 1
            last_day = max(last_day, meetings[i][1])

        return res + days - last_day


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        days = 10
        meetings = [[5, 7], [1, 3], [9, 10]]
        output = 2
        self.assertEqual(Solution().countDays(days, meetings), output)

    def test_example_2(self):
        days = 5
        meetings = [[2, 4], [1, 3]]
        output = 1
        self.assertEqual(Solution().countDays(days, meetings), output)

    def test_example_3(self):
        days = 6
        meetings = [[1, 6]]
        output = 0
        self.assertEqual(Solution().countDays(days, meetings), output)
