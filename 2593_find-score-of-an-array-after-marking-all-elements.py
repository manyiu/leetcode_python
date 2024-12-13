import heapq
from typing import List
import unittest


class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        marked = set()
        minHeap = []

        for i in range(n):
            minHeap.append((nums[i], i))

        heapq.heapify(minHeap)

        res = 0

        while minHeap:
            val, index = heapq.heappop(minHeap)

            if index not in marked:
                res += val
                marked.add(index - 1)
                marked.add(index + 1)

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        input = [2, 1, 3, 4, 5, 2]
        output = 7
        self.assertEqual(Solution().findScore(input), output)

    def test_2(self):
        input = [2, 3, 5, 1, 3, 2]
        output = 5
        self.assertEqual(Solution().findScore(input), output)
