from typing import List
import unittest


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        curr = 0
        res = 0

        for r in range(len(nums)):
            while curr & nums[r]:
                curr ^= nums[l]
                l += 1
            res = max(res, r - l + 1)
            curr |= nums[r]

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1, 3, 8, 48, 10]
        output = 3
        self.assertEqual(Solution().longestNiceSubarray(nums), output)

    def test_2(self):
        nums = [3, 1, 5, 11, 13]
        output = 1
        self.assertEqual(Solution().longestNiceSubarray(nums), output)
