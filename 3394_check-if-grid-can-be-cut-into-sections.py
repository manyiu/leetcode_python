from typing import List
import unittest


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x_sorted = sorted(rectangles)
        y_sorted = sorted(rectangles, key=lambda x: x[1])

        x_prev_edge = x_sorted[0][2]
        y_prev_edge = y_sorted[0][3]

        x_cut = 0
        y_cut = 0

        for i in range(1, len(rectangles)):
            if x_sorted[i][0] >= x_prev_edge:
                x_cut += 1
            x_prev_edge = max(x_prev_edge, x_sorted[i][2])
            if y_sorted[i][1] >= y_prev_edge:
                y_cut += 1
            y_prev_edge = max(y_prev_edge, y_sorted[i][3])

        return x_cut >= 2 or y_cut >= 2


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        n = 5
        rectangles = [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]
        output = True
        self.assertEqual(Solution().checkValidCuts(n, rectangles), output)

    def test_example_2(self):
        n = 4
        rectangles = [[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]]
        output = True
        self.assertEqual(Solution().checkValidCuts(n, rectangles), output)

    def test_example_3(self):
        n = 4
        rectangles = [
            [0, 2, 2, 4],
            [1, 0, 3, 2],
            [2, 2, 3, 4],
            [3, 0, 4, 2],
            [3, 2, 4, 4],
        ]
        output = False
        self.assertEqual(Solution().checkValidCuts(n, rectangles), output)
