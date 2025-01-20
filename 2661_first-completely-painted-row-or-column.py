from typing import List
import unittest


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        coord = {}

        for r in range(m):
            for c in range(n):
                coord[mat[r][c]] = (r, c)

        row_count = [0] * m
        column_count = [0] * n

        for i, a in enumerate(arr):
            r, c = coord[a]

            row_count[r] += 1
            column_count[c] += 1

            if row_count[r] == n or column_count[c] == m:
                return i


class TestSolution(unittest.TestCase):
    def test_1(self):
        arr = [1, 3, 4, 2]
        mat = [[1, 4], [2, 3]]
        output = 2
        self.assertEqual(Solution().firstCompleteIndex(arr, mat), output)

    def test_2(self):
        arr = [2, 8, 7, 4, 1, 3, 5, 6, 9]
        mat = [[3, 2, 5], [1, 4, 6], [8, 7, 9]]
        output = 3
        self.assertEqual(Solution().firstCompleteIndex(arr, mat), output)
