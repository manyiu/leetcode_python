from collections import defaultdict
from typing import List
import unittest


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = [False] * n

        def dfs(node: int, member: list[int]) -> None:
            if visited[node]:
                return

            visited[node] = True
            member.append(node)

            for nei in adj[node]:
                dfs(nei, member)

            return member

        res = 0

        for i in range(n):
            if visited[i]:
                continue

            member = dfs(i, [])

            if all(len(member) - 1 == len(adj[node]) for node in member):
                res += 1

        return res


# class UnionFind:
#     def __init__(self, n):
#         self.parent = list(range(n))
#         self.rank = [0] * n

#     def find(self, x) -> int:
#         while x != self.parent[x]:
#             self.parent[x] = self.parent[self.parent[x]]
#             x = self.parent[x]

#         return x

#     def union(self, a, b) -> bool:
#         root_a = self.find(a)
#         root_b = self.find(b)

#         if root_a == root_b:
#             return False

#         if self.rank[root_a] > self.rank[root_b]:
#             self.parent[root_b] = root_a
#         elif self.rank[root_a] < self.rank[root_b]:
#             self.parent[root_a] = root_b
#         else:
#             self.parent[root_b] = root_a
#             self.rank[root_a] += 1

#         return True


# class Solution:
#     def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
#         uf = UnionFind(n)

#         for a, b in edges:
#             uf.union(a, b)

#         group = defaultdict(list)

#         for i in range(n):
#             root = uf.find(i)

#             group[root].append(i)

#         group_edge_count = defaultdict(int)

#         for a, b in edges:
#             root_a = uf.find(a)
#             group_edge_count[root_a] += 1

#         res = 0

#         for k in group.keys():
#             node_count = len(group[k])
#             edge_count = group_edge_count[k]

#             print(node_count, edge_count)

#             if node_count * (node_count - 1) == 2 * edge_count:
#                 res += 1

#         return res


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        n = 6
        edges = [[0, 1], [0, 2], [1, 2], [3, 4]]
        output = 3
        self.assertEqual(Solution().countCompleteComponents(n, edges), output)

    # def test_example_2(self):
    #     n = 6
    #     edges = [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]
    #     output = 2
    #     self.assertEqual(Solution().countCompleteComponents(n, edges), output)
