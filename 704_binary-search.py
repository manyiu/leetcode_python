from typing import List
import unittest


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return -1


class TestSearch(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual(
            solution.search([-1, 0, 3, 5, 9, 12], 9),
            4,
        )

        self.assertEqual(
            solution.search([-1, 0, 3, 5, 9, 12], 2),
            -1,
        )
