import heapq
from typing import List
import unittest


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while maxHeap:
            a = -heapq.heappop(maxHeap)

            if not maxHeap:
                return a

            b = -heapq.heappop(maxHeap)

            diff = a - b

            if diff > 0:
                heapq.heappush(maxHeap, -diff)

        return 0


class TestLastStoneWeight(unittest.TestCase):
    def test_example(self):
        self.assertEqual(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]), 1)
        self.assertEqual(Solution().lastStoneWeight([1, 3]), 2)
        self.assertEqual(Solution().lastStoneWeight([2, 2]), 0)
        self.assertEqual(Solution().lastStoneWeight([1]), 1)
