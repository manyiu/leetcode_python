from typing import List
import unittest


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1

        return l

    # def removeDuplicates(self, nums: List[int]) -> int:
    #     l, r = 0, 0

    #     while r < len(nums):
    #         while r + 1 < len(nums) and nums[r] == nums[r + 1]:
    #             r += 1

    #         nums[l] = nums[r]

    #         l += 1
    #         r += 1

    #     return l


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1, 1, 2]
        res = 2
        self.assertEqual(res, Solution().removeDuplicates(nums))

    def test_2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        res = 5
        self.assertEqual(res, Solution().removeDuplicates(nums))
