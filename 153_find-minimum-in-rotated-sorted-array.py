from typing import List
import unittest


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        return nums[l]


class TestFindMin(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual(
            solution.findMin([3, 4, 5, 1, 2]),
            1,
        )
        self.assertEqual(
            solution.findMin([4, 5, 6, 7, 0, 1, 2]),
            0,
        )
        self.assertEqual(
            solution.findMin([11, 13, 15, 17]),
            11,
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
            solution.findMin([2, 1]),
            1,
        )
        self.assertEqual(
            solution.findMin([3, 1, 2]),
            1,
        )
        self.assertEqual(
            solution.findMin([2, 3, 1]),
            1,
        )
        self.assertEqual(
            solution.findMin([1, 2, 3]),
            1,
        )
        self.assertEqual(
            solution.findMin([3, 1, 2, 3]),
            1,
        )
        self.assertEqual(
            solution.findMin([4, 5, 1, 2, 3]),
            1,
        )