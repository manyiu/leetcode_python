from typing import List
import unittest


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l, r = min(nums), max(nums)

        while l <= r:
            m = l + (r - l) // 2

            curr = 0
            last = -2

            for i in range(len(nums)):
                if nums[i] <= m and i != last + 1:
                    curr += 1
                    last = i

            if curr >= k:
                r = m - 1
            else:
                l = m + 1

        return l


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [2, 3, 5, 9]
        k = 2
        output = 5
        self.assertEqual(Solution().minCapability(nums, k), output)

    def test_2(self):
        nums = [2, 7, 9, 3, 1]
        k = 2
        output = 2
        self.assertEqual(Solution().minCapability(nums, k), output)
