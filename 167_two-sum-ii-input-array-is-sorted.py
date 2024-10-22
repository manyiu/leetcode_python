from typing import List
import unittest


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            current_sum = numbers[l] + numbers[r]

            if current_sum == target:
                return [l+1, r+1]
            
            if current_sum > target:
                r -= 1
                continue

            if current_sum < target:
                l += 1
        
        return []

        
class TestSolution(unittest.TestCase):

    def test(self):
        numbers = [2, 7, 11, 15]
        target = 9
        self.assertEqual(Solution().twoSum(numbers, target), [1, 2])
        
        numbers = [2, 3, 4]
        target = 6
        self.assertEqual(Solution().twoSum(numbers, target), [1, 3])
        
        numbers = [-1, 0]
        target = -1
        self.assertEqual(Solution().twoSum(numbers, target), [1, 2])

        numbers = [0, 0, 3, 4]
        target = 0
        self.assertEqual(Solution().twoSum(numbers, target), [1, 2])
        
        numbers = [0, 0, 3, 4]
        target = 3
        self.assertEqual(Solution().twoSum(numbers, target), [1, 3])
        
        numbers = [0, 0, 3, 4]
        target = 4
        self.assertEqual(Solution().twoSum(numbers, target), [1, 4])
        
        numbers = [0, 0, 3, 4]
        target = 7
        self.assertEqual(Solution().twoSum(numbers, target), [3, 4])
        
        numbers = [0, 0, 3, 4]
        target = 8
        self.assertEqual(Solution().twoSum(numbers, target), [])