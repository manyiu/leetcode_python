from typing import List
import unittest


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else:
                r -= 1

        return nums[l]


class TestFindMin(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(
            solution.findMin([1, 3, 5]),
            1,
        )
        self.assertEqual(
            solution.findMin([2, 2, 2, 0, 1]),
            0,
        )
        self.assertEqual(
            solution.findMin([1]),
            1,
        )
        self.assertEqual(
            solution.findMin([1, 2]),
            1,
        )
        self.assertEqual(
            solution.findMin([-12, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
            -12,
        )
        self.assertEqual(
            solution.findMin([1, 3, 3]),
            1,
        )
        self.assertEqual(
            solution.findMin([1, 10, 10, 10, 10]),
            1,
        )
