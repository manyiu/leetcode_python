from typing import List
import unittest


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            res |= nums[i]

        return res * (1 << (n - 1))

    # def subsetXORSum(self, nums: List[int]) -> int:
    #     def helper(idx: int, curr_xor: int) -> int:
    #         if idx >= len(nums):
    #             return curr_xor

    #         skip = helper(idx + 1, curr_xor)

    #         curr_xor ^= nums[idx]

    #         take = helper(idx + 1, curr_xor)

    #         return skip + take

    #     return helper(0, 0)


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        nums = [1, 3]
        expected = 6
        self.assertEqual(Solution().subsetXORSum(nums), expected)

    def test_example_2(self):
        nums = [5, 1, 6]
        expected = 28
        self.assertEqual(Solution().subsetXORSum(nums), expected)

    def test_example_3(self):
        nums = [3, 4, 5, 6, 7, 8]
        expected = 480
        self.assertEqual(Solution().subsetXORSum(nums), expected)
