from typing import List
import unittest


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0

        for i in range(0, len(nums) - 2):
            if nums[i] == 0:
                res += 1
                nums[i] = 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1

        for i in range(len(nums) - 2, len(nums)):
            if nums[i] != 1:
                return -1

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [0, 1, 1, 1, 0, 0]
        output = 3
        self.assertEqual(Solution().minOperations(nums), output)

    def test_2(self):
        nums = [0, 1, 1, 1]
        output = -1
        self.assertEqual(Solution().minOperations(nums), output)
