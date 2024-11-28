from typing import List
import unittest


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = set()
        col = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        for i in row:
            for j in range(len(matrix[i])):
                matrix[i][j] = 0

        for j in col:
            for i in range(len(matrix)):
                matrix[i][j] = 0


class TestSolution(unittest.TestCase):
    def test_0(self):
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        Solution().setZeroes(matrix)
        self.assertEqual(matrix, [[1, 0, 1], [0, 0, 0], [1, 0, 1]])

    def test_1(self):
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        Solution().setZeroes(matrix)
        self.assertEqual(matrix, [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])
