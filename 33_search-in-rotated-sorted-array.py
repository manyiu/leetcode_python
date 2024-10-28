from typing import List
import unittest


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[r] > nums[m]:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

        return -1


class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        self.assertEqual(Solution().search(nums, target), 4)

    def test_1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        self.assertEqual(Solution().search(nums, target), -1)

    def test_2(self):
        nums = [1]
        target = 0
        self.assertEqual(Solution().search(nums, target), -1)

    def test_3(self):
        nums = [1]
        target = 1
        self.assertEqual(Solution().search(nums, target), 0)

    def test_4(self):
        nums = [1, 3]
        target = 3
        self.assertEqual(Solution().search(nums, target), 1)

    def test_5(self):
        nums = [3, 1]
        target = 3
        self.assertEqual(Solution().search(nums, target), 0)

    def test_6(self):
        nums = [3, 1]
        target = 1
        self.assertEqual(Solution().search(nums, target), 1)

    def test_7(self):
        nums = [3, 1]
        target = 0
        self.assertEqual(Solution().search(nums, target), -1)

    def test_8(self):
        nums = [3, 1, 2]
        target = 0
        self.assertEqual(Solution().search(nums, target), -1)

    def test_9(self):
        nums = [3, 1, 2]
        target = 1
        self.assertEqual(Solution().search(nums, target), 1)
