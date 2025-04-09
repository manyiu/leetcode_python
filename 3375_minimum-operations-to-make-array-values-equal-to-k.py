from typing import List
import unittest

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = set()
        
        for num in nums:
            if num < k:
                return -1
            if num in seen or num == k:
                continue
            seen.add(num)

        return len(seen)

class TestSoltuion(unittest.TestCase):
    def test_example_1(self):
        nums = [5,2,5,4,5]
        k = 2
        expected = 2
        self.assertEqual(Solution().minOperations(nums, k), expected)

    def test_example_2(self):
        nums = [2,1,2]
        k = 2
        expected = -1
        self.assertEqual(Solution().minOperations(nums, k), expected)

    def test_example_3(self):
        nums = [9,7,5,3]
        k = 1
        expected = 4
        self.assertEqual(Solution().minOperations(nums, k), expected)