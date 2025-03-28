import heapq
from typing import List
import unittest


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        min_heap = [(grid[0][0], 0, 0)]

        visited = set()

        sorted_queries = [(q, i) for i, q in enumerate(queries)]
        sorted_queries.sort()

        accum = 0

        res = [0] * len(queries)

        for q, i in sorted_queries:
            while min_heap and min_heap[0][0] < q:
                _, r, c = heapq.heappop(min_heap)

                if (r, c) in visited:
                    continue

                visited.add((r, c))

                accum += 1

                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (
                        nr < 0
                        or nr >= len(grid)
                        or nc < 0
                        or nc >= len(grid[r])
                        or (nr, nc) in visited
                    ):
                        continue

                    heapq.heappush(min_heap, (grid[nr][nc], nr, nc))

            res[i] = accum

        return res

    # def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
    #     def dfs(r: int, c: int, q: int, visited: set) -> int:
    #         if (
    #             r < 0
    #             or r >= len(grid)
    #             or c < 0
    #             or c >= len(grid[r])
    #             or grid[r][c] >= q
    #             or (r, c) in visited
    #         ):
    #             return 0

    #         visited.add((r, c))

    #         directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    #         point = 1

    #         for dr, dc in directions:
    #             point += dfs(r + dr, c + dc, q, visited)

    #         return point

    #     res = []

    #     for query in queries:
    #         res.append(dfs(0, 0, query, set()))

    #     return res


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        grid = [[1, 2, 3], [2, 5, 7], [3, 5, 1]]
        queries = [5, 6, 2]
        output = [5, 8, 1]
        self.assertEqual(Solution().maxPoints(grid, queries), output)

    def test_example_2(self):
        grid = [[5, 2, 1], [1, 1, 2]]
        queries = [3]
        output = [0]
        self.assertEqual(Solution().maxPoints(grid, queries), output)
