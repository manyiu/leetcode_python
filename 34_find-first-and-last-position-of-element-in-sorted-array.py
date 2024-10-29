from typing import List
import unittest


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] >= target:
                r = m - 1
            else:
                l = m + 1

        if l >= len(nums) or nums[l] != target:
            return [-1, -1]

        start = l

        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] <= target:
                l = m + 1
            else:
                r = m - 1

        end = r

        return [start, end]


class TestSolution(unittest.TestCase):
    def test(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        self.assertEqual(Solution().searchRange(nums, target), [3, 4])
        nums = [5, 7, 7, 8, 8, 10]
        target = 6
        self.assertEqual(Solution().searchRange(nums, target), [-1, -1])
        nums = []
        target = 0
        self.assertEqual(Solution().searchRange(nums, target), [-1, -1])
        nums = [1]
        target = 1
        self.assertEqual(Solution().searchRange(nums, target), [0, 0])
        nums = [1]
        target = 0
        self.assertEqual(Solution().searchRange(nums, target), [-1, -1])
        nums = [1, 2]
        target = 2
        self.assertEqual(Solution().searchRange(nums, target), [1, 1])
        nums = [1, 2]
        target = 1
        self.assertEqual(Solution().searchRange(nums, target), [0, 0])
        nums = [2, 2]
        target = 3
        self.assertEqual(Solution().searchRange(nums, target), [-1, -1])
