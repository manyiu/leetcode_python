import unittest
from collections import defaultdict
from typing import List


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        count = defaultdict(int)

        for pos, num in fruits:
            count[pos] += num

        prefix_left = [0] * (k + 1)
        prefix_right = [0] * (k + 1)

        for i in range(1, k + 1):
            prefix_left[i] = prefix_left[i - 1] + count[startPos - i]
            prefix_right[i] = prefix_right[i - 1] + count[startPos + i]

        res = 0

        for i in range(1, k + 1):
            left = prefix_left[i]
            right = prefix_right[k - (i * 2)] if k - (i * 2) >= 0 else 0
            res = max(res, left + right)

            right = prefix_right[i]
            left = prefix_left[k - (i * 2)] if k - (i * 2) >= 0 else 0
            res = max(res, left + right)

        return res + count[startPos]


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        fruits = [[2, 8], [6, 3], [8, 6]]
        startPos = 5
        k = 4
        expected = 9
        actual = Solution().maxTotalFruits(fruits, startPos, k)
        self.assertEqual(actual, expected)

    def test_example_2(self):
        fruits = [[0, 9], [4, 1], [5, 7], [6, 2], [7, 4], [10, 9]]
        startPos = 5
        k = 4
        expected = 14
        actual = Solution().maxTotalFruits(fruits, startPos, k)
        self.assertEqual(actual, expected)

    def test_example_3(self):
        fruits = [[0, 3], [6, 4], [8, 5]]
        startPos = 3
        k = 2
        expected = 0
        actual = Solution().maxTotalFruits(fruits, startPos, k)
        self.assertEqual(actual, expected)
