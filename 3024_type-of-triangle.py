from collections import defaultdict
from typing import List
import unittest


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()

        if nums[0] + nums[1] <= nums[2]:
            return "none"
        
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        
        if nums[0] != nums[1] and nums[1] != nums[2]:
            return "scalene"
        
        return "isosceles"

    # def triangleType(self, nums: List[int]) -> str:
    #     N = len(nums)
    #     same_length_count = 0
    #     length_count = defaultdict(int)

    #     for i in range(N):
    #         if nums[i] == 0:
    #             return "none"
    #         length_count[nums[i]] += 1
    #         same_length_count = max(same_length_count, length_count[nums[i]])

    #         for j in range(i, i+3):
    #             if nums[j%3] >= nums[(j+1)%3] + nums[(j+2)%3]:
    #                 return "none"
                
    #     if same_length_count == 3:
    #         return "equilateral"
        
    #     if same_length_count == 2:
    #         return "isosceles"
        
    #     return "scalene"
    
class TestSolution(unittest.TestCase):
    def test_example_1(self):
        nums = [3, 3, 3]
        expected = "equilateral"
        self.assertEqual(Solution().triangleType(nums), expected)

    def test_example_2(self):
        nums = [3, 4, 5]
        expected = "scalene"
        self.assertEqual(Solution().triangleType(nums), expected)