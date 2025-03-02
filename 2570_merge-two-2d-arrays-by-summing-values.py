from typing import List
import unittest


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        i, j = 0, 0
        res = []

        while i < len(nums1) and j < len(nums2):
            num1_idx, num1_val = nums1[i]
            num2_idx, num2_val = nums2[j]

            if num1_idx == num2_idx:
                res.append([num1_idx, num1_val + num2_val])
                i += 1
                j += 1
            elif num1_idx < num2_idx:
                res.append([num1_idx, num1_val])
                i += 1
            else:
                res.append([num2_idx, num2_val])
                j += 1

        if i < len(nums1):
            res += nums1[i:]
        elif j < len(nums2):
            res += nums2[j:]

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums1 = [[1, 2], [2, 3], [4, 5]]
        nums2 = [[1, 4], [3, 2], [4, 1]]
        output = [[1, 6], [2, 3], [3, 2], [4, 6]]
        self.assertEqual(Solution().mergeArrays(nums1, nums2), output)

    def test_2(self):
        nums1 = [[2, 4], [3, 6], [5, 5]]
        nums2 = [[1, 3], [4, 3]]
        output = [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]]
        self.assertEqual(Solution().mergeArrays(nums1, nums2), output)
