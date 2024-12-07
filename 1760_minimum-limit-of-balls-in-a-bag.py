from typing import List
import unittest


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)

        while left <= right:
            mid = (left + right) // 2

            operationsCount = sum([(num - 1) // mid for num in nums])

            if operationsCount <= maxOperations:
                right = mid - 1
            else:
                left = mid + 1

        return left


class TestSolution(unittest.TestCase):
    def test_0(self):
        solution = Solution()
        self.assertEqual(
            solution.minimumSize([9], 2),
            3,
        )

    def test_1(self):
        solution = Solution()
        self.assertEqual(
            solution.minimumSize([2, 4, 8, 2], 4),
            2,
        )

    def test_2(self):
        solution = Solution()
        self.assertEqual(
            solution.minimumSize([7, 17], 2),
            7,
        )
