from typing import List
import unittest


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0

        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1

        return l


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [3, 2, 2, 3]
        val = 3
        res = 2
        self.assertEqual(res, Solution().removeElement(nums, val))

    def test_2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        res = 5
        self.assertEqual(res, Solution().removeElement(nums, val))

    def test_3(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 3
        res = 7
        self.assertEqual(res, Solution().removeElement(nums, val))

    def test_4(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 4
        res = 7
        self.assertEqual(res, Solution().removeElement(nums, val))
