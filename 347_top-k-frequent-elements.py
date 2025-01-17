from collections import defaultdict
import heapq
from typing import List
import unittest


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        freq = [[] for _ in range(len(nums) + 1)]

        for n, c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     freq = defaultdict(int)

    #     for num in nums:
    #         freq[num] += 1

    #     max_heap = [(-freq[f], f) for f in freq]

    #     heapq.heapify(max_heap)

    #     res = []

    #     for _ in range(k):
    #         _, num = heapq.heappop(max_heap)
    #         res.append(num)

    #     return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        output = [1, 2]
        self.assertEqual(Solution().topKFrequent(nums, k), output)

    def test_2(self):
        nums = [1]
        k = 1
        output = [1]
        self.assertEqual(Solution().topKFrequent(nums, k), output)
