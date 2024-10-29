from typing import List
import unittest


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return True

            while l < m and nums[l] == nums[m]:
                l += 1

            while r > m and nums[r] == nums[m]:
                r -= 1

            if nums[l] <= nums[m]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return False


class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [2, 5, 6, 0, 0, 1, 2]
        target = 0
        self.assertEqual(Solution().search(nums, target), True)

    def test_1(self):
        nums = [2, 5, 6, 0, 0, 1, 2]
        target = 3
        self.assertEqual(Solution().search(nums, target), False)

    def test_2(self):
        nums = [1]
        target = 0
        self.assertEqual(Solution().search(nums, target), False)

    def test_3(self):
        nums = [1]
        target = 1
        self.assertEqual(Solution().search(nums, target), True)

    def test_4(self):
        nums = [1, 3]
        target = 3
        self.assertEqual(Solution().search(nums, target), True)

    def test_5(self):
        nums = [3, 1]
        target = 3
        self.assertEqual(Solution().search(nums, target), True)

    def test_6(self):
        nums = [3, 1]
        target = 0
        self.assertEqual(Solution().search(nums, target), False)

    def test_7(self):
        nums = [1, 0, 1, 1, 1]
        target = 0
        self.assertEqual(Solution().search(nums, target), True)
