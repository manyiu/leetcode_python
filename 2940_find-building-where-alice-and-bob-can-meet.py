import heapq
from typing import List
import unittest


class Solution:
    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        groups = {}

        res = [-1] * len(queries)

        for i, query in enumerate(queries):
            l, r = sorted(query)
            if l == r or heights[r] > heights[l]:
                res[i] = r
            else:
                if r not in groups:
                    groups[r] = []

                h = max(heights[l], heights[r])

                groups[r].append((h, i))

        minHeap = []

        for i in range(len(heights)):
            if i in groups:
                for h, queryIndex in groups[i]:
                    heapq.heappush(minHeap, (h, queryIndex))

            while minHeap and heights[i] > minHeap[0][0]:
                h, queryIndex = heapq.heappop(minHeap)
                res[queryIndex] = i

        return res

    # def leftmostBuildingQueries(
    #     self, heights: List[int], queries: List[List[int]]
    # ) -> List[int]:
    #     n = len(heights)
    #     res = []

    #     for a, b in queries:
    #         if a == b:
    #             res.append(a)
    #             continue

    #         pos = -1
    #         start = max(a, b)

    #         for i in range(start, n):
    #             if (heights[a] < heights[i] or a == i) and (
    #                 heights[b] < heights[i] or b == i
    #             ):
    #                 pos = i
    #                 break

    #         res.append(pos)

    #     return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        heights = [6, 4, 8, 5, 2, 7]
        queries = [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]
        output = [2, 5, -1, 5, 2]
        self.assertEqual(Solution().leftmostBuildingQueries(heights, queries), output)

    def test_2(self):
        heights = [5, 3, 8, 2, 6, 1, 4, 6]
        queries = [[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]]
        output = [7, 6, -1, 4, 6]
        self.assertEqual(Solution().leftmostBuildingQueries(heights, queries), output)
