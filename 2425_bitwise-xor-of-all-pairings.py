from typing import List
import unittest


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0

        if len(nums2) % 2 == 1:
            for num1 in nums1:
                res ^= num1

        if len(nums1) % 2 == 1:
            for num2 in nums2:
                res ^= num2

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums1 = [2, 1, 3]
        nums2 = [10, 2, 5, 0]
        output = 13
        self.assertEqual(Solution().xorAllNums(nums1, nums2), output)

    def test_2(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        output = 0
        self.assertEqual(Solution().xorAllNums(nums1, nums2), output)
