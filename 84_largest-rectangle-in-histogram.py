from typing import List
import unittest


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights)):
            insert_index = i
            while len(stack) > 0 and heights[i] < stack[-1][1]:
                max_area = max(max_area, (i - stack[-1][0]) * stack[-1][1])
                (popped_index, _) = stack.pop()
                insert_index = popped_index
            stack.append((insert_index, heights[i]))

        while stack:
            (popped_index, popped_height) = stack.pop()
            max_area = max(max_area, (len(heights) - popped_index) * popped_height)

        return max_area


class TestLargestRectangleArea(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual(
            solution.largestRectangleArea([2, 1, 5, 6, 2, 3]),
            10,
        )
        self.assertEqual(
            solution.largestRectangleArea([2, 1, 2]),
            3,
        )
        self.assertEqual(
            solution.largestRectangleArea([1, 2, 3, 4, 5]),
            9,
        )
        self.assertEqual(
            solution.largestRectangleArea([5, 4, 3, 2, 1]),
            9,
        )
        self.assertEqual(
            solution.largestRectangleArea([1, 1, 1, 1, 1]),
            5,
        )
        self.assertEqual(
            solution.largestRectangleArea([1, 1, 1, 1, 1, 1]),
            6,
        )
        self.assertEqual(
            solution.largestRectangleArea([1, 1, 1, 1, 1, 1, 1]),
            7,
        )
        self.assertEqual(
            solution.largestRectangleArea([1, 1, 1, 1, 1, 1, 1, 1]),
            8,
        )
        self.assertEqual(
            solution.largestRectangleArea([1, 1, 1, 1, 1, 1, 1, 1, 1]),
            9,
        )
        self.assertEqual(
            solution.largestRectangleArea([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
            10,
        )
        self.assertEqual(
            solution.largestRectangleArea([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
            11,
        )
