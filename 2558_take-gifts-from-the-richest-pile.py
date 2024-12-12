import heapq
from typing import List
import unittest


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = [-gift for gift in gifts]
        heapq.heapify(maxHeap)

        prev = 0

        while k > 0 and maxHeap and -maxHeap[0] >= prev:
            curr = int((-heapq.heappop(maxHeap)) ** (0.5))
            heapq.heappush(maxHeap, -curr)
            prev = curr
            k -= 1

        res = 0

        for gift in maxHeap:
            res -= gift

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        input = [25, 64, 9, 4, 100]
        k = 4
        output = 29
        self.assertEqual(Solution().pickGifts(input, k), output)

    def test_2(self):
        input = [1, 1, 1, 1]
        k = 4
        output = 4
        self.assertEqual(Solution().pickGifts(input, k), output)

    def test_3(self):
        input = [17, 2, 52, 54, 41, 1]
        k = 14
        output = 6
        self.assertEqual(Solution().pickGifts(input, k), output)
