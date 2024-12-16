import heapq
from typing import List
import unittest


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)
        minHeap = [(nums[i], i) for i in range(n)]
        heapq.heapify(minHeap)

        for _ in range(k):
            _, i = heapq.heappop(minHeap)
            nums[i] *= multiplier
            heapq.heappush(minHeap, (nums[i], i))

        return nums

    # def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
    #     for _ in range(k):
    #         minIndex = -1
    #         minValue = float("infinity")

    #         for i in range(len(nums)):
    #             if nums[i] < minValue:
    #                 minIndex = i
    #                 minValue = nums[i]

    #         nums[minIndex] *= multiplier

    #     return nums


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [2, 1, 3, 5, 6]
        k = 5
        multiplier = 2
        assert Solution().getFinalState(nums, k, multiplier) == [8, 4, 6, 5, 6]

    def test_2(self):
        nums = [1, 2]
        k = 3
        multiplier = 4
        assert Solution().getFinalState(nums, k, multiplier) == [16, 8]
