from typing import List
import unittest


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_val = 0
        max_val = 0
        curr_val = 0

        for difference in differences:
            curr_val += difference
            min_val = min(curr_val, min_val)
            max_val = max(curr_val, max_val)

        val_range = max_val - min_val
        allow_range = upper - lower

        if val_range > allow_range:
            return 0

        return allow_range - val_range + 1


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        differences = [1, -3, 4]
        lower = 1
        upper = 6
        expected = 2
        self.assertEqual(Solution().numberOfArrays(differences, lower, upper), expected)

    def test_example_2(self):
        differences = [3, -4, 5, 1, -2]
        lower = -4
        upper = 5
        expected = 4
        self.assertEqual(Solution().numberOfArrays(differences, lower, upper), expected)

    def test_example_3(self):
        differences = [4, -7, 2]
        lower = 3
        upper = 6
        expected = 0
        self.assertEqual(Solution().numberOfArrays(differences, lower, upper), expected)
