from typing import List
import unittest


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        visited = set()

        missing = 0
        repeated = 0

        for row in grid:
            for value in row:
                if value in visited:
                    repeated = value
                visited.add(value)

        for i in range(1, len(grid) ** 2 + 1):
            if i not in visited:
                missing = i
                break

        return [repeated, missing]


class TestSolution(unittest.TestCase):
    def test_1(self):
        grid = [[1, 3], [2, 2]]
        output = [2, 4]
        self.assertEqual(Solution().findMissingAndRepeatedValues(grid), output)

    def test_2(self):
        grid = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
        output = [9, 5]
        self.assertEqual(Solution().findMissingAndRepeatedValues(grid), output)
