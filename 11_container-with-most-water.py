from typing import List
import unittest


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_volume = 0
        l, r = 0, len(height) - 1

        while l < r:
            curr_volume = min(height[l], height[r]) * (r-l)

            if curr_volume > max_volume:
                max_volume = curr_volume

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return max_volume
        

class TestSolution(unittest.TestCase):

    def test(self):
        height = [1,8,6,2,5,4,8,3,7]
        self.assertEqual(Solution().maxArea(height), 49)
        
        height = [1,1]
        self.assertEqual(Solution().maxArea(height), 1)
        
        height = [4,3,2,1,4]
        self.assertEqual(Solution().maxArea(height), 16)
        
        height = [1,2,1]
        self.assertEqual(Solution().maxArea(height), 2)
        
        height = [1,2,4,3]
        self.assertEqual(Solution().maxArea(height), 4)
        
        height = [1,2,4,3,1]
        self.assertEqual(Solution().maxArea(height), 4)
