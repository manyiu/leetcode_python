from collections import defaultdict
from typing import List
import unittest


class UnionFind:
    def __init__(self, n: int):
        self.parent = [0] * n
        self.rank = [0] * n

        for i in range(n):
            self.parent[i] = i

    def find(self, n: int) -> int:
        curr = n

        while curr != self.parent[curr]:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]

        return curr

    def union(self, a: int, b: int) -> bool:
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        if self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
        elif self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1

        return True


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        uf = UnionFind(n)
        num_to_index = dict()

        for i, num in enumerate(nums):
            if num in num_to_index:
                continue
            num_to_index[num] = i
            if num - 1 in num_to_index:
                uf.union(i, num_to_index[num - 1])
            if num + 1 in num_to_index:
                uf.union(i, num_to_index[num + 1])

        res = 0
        group_count = defaultdict(int)

        for i in range(n):
            root = uf.find(i)
            group_count[root] += 1
            res = max(res, group_count[root])

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [100, 4, 200, 1, 3, 2]
        output = 4
        self.assertEqual(Solution().longestConsecutive(nums), output)

    def test_2(self):
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        output = 9
        self.assertEqual(Solution().longestConsecutive(nums), output)

    def test_3(self):
        nums = [1, 2, 0, 1]
        output = 3
        self.assertEqual(Solution().longestConsecutive(nums), output)
