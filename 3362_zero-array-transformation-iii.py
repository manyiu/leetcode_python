import heapq
from typing import List
import unittest


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda x: x[0])
        max_heap = []
        prefix = [0] * (len(nums) + 1)
        operations = 0
        query_index = 0

        for i, num in enumerate(nums):
            operations += prefix[i]

            while query_index < len(queries) and queries[query_index][0] <= i:
                heapq.heappush(max_heap, -queries[query_index][1])
                query_index += 1

            while operations < num and max_heap and -max_heap[0] >= i:
                operations += 1
                prefix[-heapq.heappop(max_heap) + 1] -= 1

            if operations < num:
                return -1
        
        return len(max_heap)


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        nums = [2,0,2]
        queries = [[0,2],[0,2],[0,2]]
        expected = 1
        result = Solution().maxRemoval(nums, queries)
        self.assertEqual(result, expected)

    def test_example_2(self):
        nums = [1,1,1,1]
        queries = [[1,3],[0,2],[1,3],[1,2]]
        expected = 2
        result = Solution().maxRemoval(nums, queries)
        self.assertEqual(result, expected)

    def test_example_3(self):
        nums = [1,2,3,4]
        queries = [[0,3]]
        expected = -1
        result = Solution().maxRemoval(nums, queries)
        self.assertEqual(result, expected)