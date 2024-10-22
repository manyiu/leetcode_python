from typing import List
import unittest


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = []

        for i in range(len(sorted_nums) - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            
            l, r = i + 1, len(sorted_nums) - 1

            while l < r:
                current_sum = sorted_nums[i] + sorted_nums[l] + sorted_nums[r]

                if current_sum == 0:
                    result.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    r -= 1
                    l += 1

                    while l < len(sorted_nums) - 1 and sorted_nums[l-1] == sorted_nums[l]:
                        l += 1
                elif current_sum > 0:
                    r -= 1
                else:
                    l += 1

        return result

        
class TestSolution(unittest.TestCase):

    def test(self):
        nums = [-1, 0, 1, 2, -1, -4]
        self.assertEqual(Solution().threeSum(nums), [[-1, -1, 2], [-1, 0, 1]])

        nums = [0, 1, 1]
        self.assertEqual(Solution().threeSum(nums), [])
        
        nums = []
        self.assertEqual(Solution().threeSum(nums), [])
        
        nums = [0]
        self.assertEqual(Solution().threeSum(nums), [])
        
        nums = [0, 0, 0]
        self.assertEqual(Solution().threeSum(nums), [[0, 0, 0]])
        
        nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(Solution().threeSum(nums), [[0, 0, 0]])
        