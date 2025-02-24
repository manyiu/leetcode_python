from collections import defaultdict
from typing import List
import unittest


class Solution:
    def mostProfitablePath(
        self, edges: List[List[int]], bob: int, amount: List[int]
    ) -> int:
        node_count = defaultdict(int)
        non_edge_node = set()
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            node_count[a] += 1
            if node_count[a] >= 2:
                non_edge_node.add(a)
            adj[b].append(a)
            node_count[b] += 1
            if node_count[b] >= 2:
                non_edge_node.add(b)

        bob_path = [bob]

        def bob_path_bfs(visit: set) -> bool:
            curr = bob_path[-1]

            if curr in visit:
                return False

            if curr == 0:
                return True

            visit.add(curr)

            for next_node in adj[curr]:
                if next_node not in visit:
                    bob_path.append(next_node)
                    if bob_path_bfs(visit):
                        return True
                    bob_path.pop()

        bob_path_bfs(set())

        bob_time = {}

        for i, node in enumerate(bob_path):
            bob_time[node] = i

        res = float("-inf")

        q = [(0, 0, -1, amount[0])]  # (node, time, parent, reward)

        while q:
            node, time, parent, reward = q.pop(0)

            for nei in adj[node]:
                if nei == parent:
                    continue

                node_reward = amount[nei]
                nei_time = time + 1
                if nei in bob_time:
                    if bob_time[nei] < nei_time:
                        node_reward = 0
                    elif bob_time[nei] == nei_time:
                        node_reward //= 2

                q.append((nei, nei_time, node, reward + node_reward))

                if nei not in non_edge_node:
                    res = max(res, reward + node_reward)

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
        bob = 3
        amount = [-2, 4, 2, -4, 6]
        output = 6
        self.assertEqual(Solution().mostProfitablePath(edges, bob, amount), output)

    def test_2(self):
        edges = [[0, 1]]
        bob = 1
        amount = [-7280, 2350]
        output = -7280
        self.assertEqual(Solution().mostProfitablePath(edges, bob, amount), output)
