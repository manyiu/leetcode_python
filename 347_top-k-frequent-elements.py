import heapq
from typing import List
import unittest


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        max_heap = []

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
            heapq.heappush(max_heap, (-freq[num], num))

        num_popped = set()
        result = []

        while len(result) < k and len(max_heap) > 0:
            _, num = heapq.heappop(max_heap)
            if num not in num_popped:
                result.append(num)
                num_popped.add(num)

        return result


        
        

class TestSolution(unittest.TestCase):
    def test(self):
        nums = [1,1,1,2,2,3]
        k = 2
        self.assertEqual(Solution().topKFrequent(nums, k), [1,2])
        nums = [1]
        k = 1
        self.assertEqual(Solution().topKFrequent(nums, k), [1])