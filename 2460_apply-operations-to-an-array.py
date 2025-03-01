from typing import List
import unittest


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i, j = 0, 0

        while i < len(nums):
            if nums[i] == 0:
                i += 1
            elif i + 1 < len(nums) and nums[i] == nums[i + 1]:
                nums[j] = nums[i] * 2
                i += 2
                j += 1
            else:
                nums[j] = nums[i]
                i += 1
                j += 1

        while j < len(nums):
            nums[j] = 0
            j += 1

        return nums


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1, 2, 2, 1, 1, 0]
        output = [1, 4, 2, 0, 0, 0]
        self.assertEqual(Solution().applyOperations(nums), output)

    def test_2(self):
        nums = [0, 1]
        output = [1, 0]
        self.assertEqual(Solution().applyOperations(nums), output)
