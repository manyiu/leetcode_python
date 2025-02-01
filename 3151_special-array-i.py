from typing import List
import unittest


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True

        for i in range(1, len(nums)):
            if nums[i - 1] % 2 == nums[i] % 2:
                return False

        return True


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1]
        output = True
        self.assertEqual(Solution().isArraySpecial(nums), output)

    def test_2(self):
        nums = [2, 1, 4]
        output = True
        self.assertEqual(Solution().isArraySpecial(nums), output)

    def test_3(self):
        nums = [4, 3, 1, 6]
        output = False
        self.assertEqual(Solution().isArraySpecial(nums), output)
