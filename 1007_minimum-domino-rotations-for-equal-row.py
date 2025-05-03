from collections import defaultdict
from typing import List
import unittest


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        unique_count = defaultdict(int)
        top_count = defaultdict(int)
        bottom_count = defaultdict(int)

        target_values = []

        for top, bottom in zip(tops, bottoms):
            top_count[top] += 1
            bottom_count[bottom] += 1

            if top == bottom:
                unique_count[top] += 1
            else:
                unique_count[top] += 1
                unique_count[bottom] += 1

            if unique_count[top] == len(tops):
                target_values.append(top)
            if unique_count[bottom] == len(tops):
                target_values.append(bottom)

        if len(target_values) == 0:
            return -1

        res = float('inf')

        for target in target_values:
            res = min(res, len(tops) -
                      top_count[target], len(bottoms) - bottom_count[target])

        return res


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        tops = [2, 1, 2, 4, 2, 2]
        bottoms = [5, 2, 6, 2, 3, 2]
        expected = 2
        self.assertEqual(Solution().minDominoRotations(
            tops, bottoms), expected)

    def test_example_2(self):
        tops = [3, 5, 1, 2, 3]
        bottoms = [3, 6, 3, 3, 4]
        expected = -1
        self.assertEqual(Solution().minDominoRotations(
            tops, bottoms), expected)

    def test_case_74(self):
        tops = [2, 1, 1, 1, 2, 2, 2, 1, 1, 2]
        bottoms = [1, 1, 2, 1, 1, 1, 1, 2, 1, 1]
        expected = 2
        self.assertEqual(Solution().minDominoRotations(
            tops, bottoms), expected)
