from typing import List
import unittest


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        values = [(num, i) for i, num in enumerate(nums)]
        values.sort(reverse=True)
        first_k = values[:k]
        return [num for num, _ in sorted(first_k, key=lambda x: x[1])]


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        nums = [2, 1, 3, 3]
        k = 2
        expected = [3, 3]
        actual = Solution().maxSubsequence(nums, k)
        self.assertEqual(actual, expected)

    def test_example_2(self):
        nums = [-1, -2, 3, 4]
        k = 3
        expected = [-1, 3, 4]
        actual = Solution().maxSubsequence(nums, k)
        self.assertEqual(actual, expected)

    def test_example_3(self):
        nums = [3, 4, 3, 3]
        k = 2
        expected = [4, 3]
        actual = Solution().maxSubsequence(nums, k)
        self.assertEqual(actual, expected)
