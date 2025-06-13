from typing import List
import unittest


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        l, r = 0, nums[-1]

        while l <= r:
            m = l + (r - l) // 2
            pair_count = 0
            i = 1
            while i < len(nums):
                if nums[i] - nums[i - 1] <= m:
                    pair_count += 1
                    i += 1
                i += 1
            if pair_count >= p:
                r = m - 1
            else:
                l = m + 1

        return l


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        nums = [10, 1, 2, 7, 1, 3]
        p = 2
        expected = 1
        solution = Solution()
        result = solution.minimizeMax(nums, p)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_example_2(self):
        nums = [4, 2, 1, 2]
        p = 1
        expected = 0
        solution = Solution()
        result = solution.minimizeMax(nums, p)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")
