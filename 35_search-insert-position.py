from typing import List
import unittest


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        i = -1

        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[m] < target:
                i = max(i, m + 1)
                l = m + 1
            else:
                r = m - 1

        return i


class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [1, 3, 5, 6]
        target = 5
        self.assertEqual(Solution().searchInsert(nums, target), 2)

    def test_1(self):
        nums = [1, 3, 5, 6]
        target = 2
        self.assertEqual(Solution().searchInsert(nums, target), 1)

    def test_2(self):
        nums = [1, 3, 5, 6]
        target = 7
        self.assertEqual(Solution().searchInsert(nums, target), 4)

    def test_3(self):
        nums = [1, 3, 5, 6]
        target = 0
        self.assertEqual(Solution().searchInsert(nums, target), 0)

    def test_4(self):
        nums = [1]
        target = 0
        self.assertEqual(Solution().searchInsert(nums, target), 0)

    def test_5(self):
        nums = [1]
        target = 1
        self.assertEqual(Solution().searchInsert(nums, target), 0)

    def test_6(self):
        nums = [1]
        target = 2
        self.assertEqual(Solution().searchInsert(nums, target), 1)

    def test_7(self):
        nums = [1, 3]
        target = 2
        self.assertEqual(Solution().searchInsert(nums, target), 1)

    def test_8(self):
        nums = [1, 3]
        target = 3
        self.assertEqual(Solution().searchInsert(nums, target), 1)

    def test_9(self):
        nums = [1, 3]
        target = 4
        self.assertEqual(Solution().searchInsert(nums, target), 2)

    def test_10(self):
        nums = [1, 3]
        target = 0
        self.assertEqual(Solution().searchInsert(nums, target), 0)
