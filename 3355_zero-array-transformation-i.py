from typing import List
import unittest


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        prefix = [0] * (len(nums) + 1)

        for start, end in queries:
            prefix[start] += 1
            prefix[end + 1] -= 1

        curr = 0

        for i in range(len(nums)):
            curr += prefix[i]
            if curr < nums[i]:
                return False
            
        return True

    # def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
    #     prefix_start = [0] * len(nums)
    #     suffix_end = [0] * (len(nums) + 1)

    #     for start, end in queries:
    #         prefix_start[start] += 1
    #         suffix_end[end+1] += 1

    #     curr = 0

    #     for i in range(len(nums)):
    #         curr += prefix_start[i] - suffix_end[i]
    #         if curr < nums[i]:
    #             return False

    #     return True


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        nums = [1, 0, 1]
        queries = [[0, 2]]
        expected = True
        self.assertEqual(Solution().isZeroArray(nums, queries), expected)

    def test_example_2(self):
        nums = [4,3,2,1]
        queries = [[1, 3], [0,2]]
        expected = False
        self.assertEqual(Solution().isZeroArray(nums, queries), expected)