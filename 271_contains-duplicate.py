from typing import List
import unittest

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        existed = set()

        for num in nums:
            if num in existed:
                return True
            existed.add(num)
        
        return False

class TestSolution(unittest.TestCase):
    def test(self):
        nums = [1,2,3,1]
        self.assertEqual(Solution().containsDuplicate(nums), True)
        nums = [1,2,3,4]
        self.assertEqual(Solution().containsDuplicate(nums), False)
        nums = [1,1,1,3,3,4,3,2,4,2]
        self.assertEqual(Solution().containsDuplicate(nums), True)

if __name__ == '__main__':
    unittest.main()