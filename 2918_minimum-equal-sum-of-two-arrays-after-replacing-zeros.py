from typing import Counter, List
import unittest


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum_1 = 0
        sum_2 = 0
        count_zero_1 = 0
        count_zero_2 = 0

        for num in nums1:
            sum_1 += num
            if num == 0:
                sum_1 += 1
                count_zero_1 += 1

        for num in nums2:
            sum_2 += num
            if num == 0:
                sum_2 += 1
                count_zero_2 += 1

        if (count_zero_1 == 0 and sum_1 < sum_2) or (count_zero_2 == 0 and sum_2 < sum_1):
            return -1
        
        return max(sum_1, sum_2)

    # def minSum(self, nums1: List[int], nums2: List[int]) -> int:
    #     sum_1 = sum(nums1)
    #     sum_2 = sum(nums2)
        
    #     if sum_1 < sum_2:
    #         nums1, nums2 = nums2, nums1
    #         sum_1, sum_2 = sum_2, sum_1
        
    #     count_1 = Counter(nums1)
    #     count_2 = Counter(nums2)

    #     sum_diff = sum_1 - sum_2
        
    #     if sum_diff == 0 and count_1[0] == 0 and count_2[0] == 0:
    #         return sum_1

    #     if count_2[0] == 0 or (sum_diff < count_2[0] and count_1[0] == 0):
    #         return -1
        
    #     return max(sum_1 + count_1[0], sum_2 + count_2[0])


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        nums1 = [3,2,0,1,0]
        nums2 = [6,5,0]
        expected = 12
        self.assertEqual(Solution().minSum(nums1, nums2), expected)

    def test_example_2(self):
        nums1 = [2,0,2,0]
        nums2 = [1,4]
        expected = -1
        self.assertEqual(Solution().minSum(nums1, nums2), expected)