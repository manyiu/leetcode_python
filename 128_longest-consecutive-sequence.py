from typing import List
import unittest

class UnionFind:
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}

        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, x: int):
        curr = x

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

        for i in range(n):
            num_to_index[nums[i]] = i
            if nums[i] - 1 in num_to_index:
                uf.union(i, num_to_index[nums[i] - 1])
            if nums[i] + 1 in num_to_index:
                uf.union(i, num_to_index[nums[i] +1])

        group_count = dict()
        result = 0

        for i in num_to_index.values():
            root = uf.find(i)

            if root in group_count:
                group_count[root] += 1
            else:
                group_count[root] = 1

            if group_count[root] > result:
                result = group_count[root]

        return result

class TestSolution(unittest.TestCase):
    def test(self):
        nums = [100, 4, 200, 1, 3, 2]
        self.assertEqual(Solution().longestConsecutive(nums), 4)
        nums = [0,3,7,2,5,8,4,6,0,1]
        self.assertEqual(Solution().longestConsecutive(nums), 9)
        nums = [1,2,0,1]
        self.assertEqual(Solution().longestConsecutive(nums), 3)
