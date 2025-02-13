import heapq
from typing import List
import unittest


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0

        heapq.heapify(nums)

        while nums:
            if nums[0] >= k:
                return res

            if len(nums) <= 1:
                return float("inf")

            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            z = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, z)

            res += 1


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [2, 11, 10, 1, 3]
        k = 10
        output = 2
        self.assertEqual(Solution().minOperations(nums, k), output)

    def test_2(self):
        nums = [1, 1, 2, 4, 9]
        k = 20
        output = 4
        self.assertEqual(Solution().minOperations(nums, k), output)
