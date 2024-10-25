import heapq
from typing import List
import unittest


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out = {}
        max_heap = []
        result = []
        l = 0

        for r in range(len(nums)):
            heapq.heappush(max_heap, -nums[r])

            if r-l+1 == k:
                result.append(-max_heap[0])
                
                if nums[l] in out:
                    out[nums[l]] += 1
                else:
                    out[nums[l]] = 1
                
                while len(max_heap) > 0 and -max_heap[0] in out and out[-max_heap[0]] > 0:
                    out[-max_heap[0]] -= 1
                    heapq.heappop(max_heap)

                l += 1

        return result

class TestSolution(unittest.TestCase):
    def test(self):
        nums = [1,3,-1,-3,5,3,6,7]
        k = 3
        self.assertEqual(Solution().maxSlidingWindow(nums, k), [3,3,5,5,6,7])
        nums = [1]
        k = 1
        self.assertEqual(Solution().maxSlidingWindow(nums, k), [1])
        nums = [1,-1]
        k = 1
        self.assertEqual(Solution().maxSlidingWindow(nums, k), [1,-1])
        nums = [9,11]
        k = 2
        self.assertEqual(Solution().maxSlidingWindow(nums, k), [11])
        nums = [4,-2]
        k = 2
        self.assertEqual(Solution().maxSlidingWindow(nums, k), [4])
        nums = [1,3,1,2,0,5]
        k = 3
        self.assertEqual(Solution().maxSlidingWindow(nums, k), [3,3,2,5])
        nums = [1,3,1,2,0,5]
        k = 1
        self.assertEqual(Solution().maxSlidingWindow(nums, k), [1,3,1,2,0,5])
        nums = [1,3,1,2,0,5]
        k = 6
        self.assertEqual(Solution().maxSlidingWindow(nums, k), [5])
        nums = [1,3,1,2,0,5]
        k = 4
        self.assertEqual(Solution().maxSlidingWindow(nums, k), [3,3,5])
        nums = [1,3,1,2,0,5]
        k = 5
        self.assertEqual(Solution().maxSlidingWindow(nums, k), [3,5])
        nums = [1,3,1,2,0,5]
        k = 2
        self.assertEqual(Solution().maxSlidingWindow(nums, k), [3,3,2,2,5])
        nums = [1,3,1,2,0,5]
        k = 3
        self.assertEqual(Solution().maxSlidingWindow(nums, k), [3,3,2,5])
