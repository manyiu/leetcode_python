from typing import List
import unittest


class Solution:
    def helper(self, nums: List[int]) -> int:
        a, b = 0, 0

        for num in nums:
            a, b = b, max(a + num, b)

        return b

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))


class TestSolution(unittest.TestCase):
    def test_1(self):
        assert Solution().rob([2, 3, 2]) == 3

    def test_2(self):
        assert Solution().rob([1, 2, 3, 1]) == 4

    def test_3(self):
        assert Solution().rob([1, 2, 3]) == 3
