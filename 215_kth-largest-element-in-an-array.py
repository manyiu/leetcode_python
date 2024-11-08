import heapq
from typing import List
import unittest


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)

        for _ in range(1, k):
            heapq.heappop(maxHeap)

        return -maxHeap[0]

    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     heapq.heapify(nums)

    #     print(nums)

    #     while len(nums) > k:
    #         heapq.heappop(nums)

    #     return nums[0]


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        res = 5
        self.assertEqual(Solution().findKthLargest(nums, k), res)

    def test_2(self):
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        res = 4
        self.assertEqual(Solution().findKthLargest(nums, k), res)
