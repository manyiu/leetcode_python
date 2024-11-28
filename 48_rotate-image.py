from typing import List
import unittest


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                t, b = l, r

                topLeft = matrix[t][l + i]

                matrix[t][l + i] = matrix[b - i][l]

                matrix[b - i][l] = matrix[b][r - i]

                matrix[b][r - i] = matrix[t + i][r]

                matrix[t + i][r] = topLeft

            l += 1
            r -= 1


class TestSolution(unittest.TestCase):
    def test_0(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        Solution().rotate(matrix)
        self.assertEqual(matrix, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    def test_1(self):
        matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        Solution().rotate(matrix)
        self.assertEqual(
            matrix, [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
        )

    def test_2(self):
        matrix = [[1]]
        Solution().rotate(matrix)
        self.assertEqual(matrix, [[1]])

    def test_3(self):
        matrix = [[1, 2], [3, 4]]
        Solution().rotate(matrix)
        self.assertEqual(matrix, [[3, 1], [4, 2]])
