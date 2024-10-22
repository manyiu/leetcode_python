from typing import List
import unittest


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = 0, 0
        volume = 0

        while l < r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])

            if maxL < maxR:
                volume += max(0,  min(maxL, maxR) - height[l])
                l += 1
            else:
                volume += max(0,  min(maxL, maxR) - height[r])
                r -= 1

        return volume

class TestSolution(unittest.TestCase):

    def test(self):
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        self.assertEqual(Solution().trap(height), 6)
        
        height = [4,2,0,3,2,5]
        self.assertEqual(Solution().trap(height), 9)
        
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        self.assertEqual(Solution().trap(height), 6)
        
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        self.assertEqual(Solution().trap(height), 6)
        
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        self.assertEqual(Solution().trap(height), 6)
        
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        self.assertEqual(Solution().trap(height), 6)