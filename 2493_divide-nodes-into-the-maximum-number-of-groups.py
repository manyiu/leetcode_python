from collections import defaultdict, deque
from typing import List
import unittest


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = set()
        res = 0

        def get_connected_component(src):
            q = deque([src])
            component = set([src])

            while q:
                node = q.popleft()

                for nei in adj[node]:
                    if nei in component:
                        continue

                    q.append(nei)
                    component.add(nei)
                    visit.add(nei)

            return component

        def longest_path(src):
            q = deque([(src, 1)])
            dist = {src: 1}

            while q:
                node, length = q.popleft()

                for nei in adj[node]:
                    if nei in dist:
                        if dist[nei] == length:
                            return -1
                        continue
                    q.append((nei, length + 1))
                    dist[nei] = length + 1

            return max(dist.values())

        for i in range(1, n + 1):
            if i in visit:
                continue

            visit.add(i)
            component = get_connected_component(i)

            max_count = 0

            for src in component:
                length = longest_path(src)

                if length == -1:
                    return -1

                max_count = max(max_count, length)

            res += max_count

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        n = 6
        edges = [[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]]
        output = 4
        self.assertEqual(Solution().magnificentSets(n, edges), output)

    def test_2(self):
        n = 3
        edges = [[1, 2], [2, 3], [3, 1]]
        output = -1
        self.assertEqual(Solution().magnificentSets(n, edges), output)
