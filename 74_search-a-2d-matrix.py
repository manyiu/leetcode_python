from typing import List
import unittest


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        row = -1

        while t <= b:
            m = (t + b) // 2

            if matrix[m][0] <= target <= matrix[m][len(matrix[m]) - 1]:
                row = m
                break

            if target < matrix[m][0]:
                b = m - 1
            else:
                t = m + 1

        if row == -1:
            return False

        l, r = 0, len(matrix[row])

        while l <= r:
            m = (l + r) // 2

            if target == matrix[row][m]:
                return True

            if target < matrix[row][m]:
                r = m - 1
            else:
                l = m + 1

        return False


class TestSearchMatrix(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual(
            solution.searchMatrix(
                [
                    [1, 3, 5, 7],
                    [10, 11, 16, 20],
                    [23, 30, 34, 50],
                ],
                3,
            ),
            True,
        )
        self.assertEqual(
            solution.searchMatrix(
                [
                    [1, 3, 5, 7],
                    [10, 11, 16, 20],
                    [23, 30, 34, 50],
                ],
                13,
            ),
            False,
        )
        self.assertEqual(
            solution.searchMatrix(
                [
                    [1, 3, 5, 7],
                    [10, 11, 16, 20],
                    [23, 30, 34, 50],
                ],
                1,
            ),
            True,
        )
        self.assertEqual(
            solution.searchMatrix(
                [
                    [1, 3, 5, 7],
                    [10, 11, 16, 20],
                    [23, 30, 34, 50],
                ],
                50,
            ),
            True,
        )
        self.assertEqual(
            solution.searchMatrix(
                [
                    [1, 3, 5, 7],
                    [10, 11, 16, 20],
                    [23, 30, 34, 50],
                ],
                0,
            ),
            False,
        )
        self.assertEqual(
            solution.searchMatrix(
                [
                    [1, 3, 5, 7],
                    [10, 11, 16, 20],
                    [23, 30, 34, 50],
                ],
                51,
            ),
            False,
        )
        self.assertEqual(
            solution.searchMatrix(
                [
                    [1, 3, 5, 7],
                    [10, 11, 16, 20],
                    [23, 30, 34, 50],
                ],
                15,
            ),
            False,
        )
