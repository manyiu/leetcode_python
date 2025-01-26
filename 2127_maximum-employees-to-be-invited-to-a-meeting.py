from collections import defaultdict, deque
from typing import List
import unittest


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        N = len(favorite)

        longest_cycle = 0
        visit = set()
        length_of_2_cycles = []

        for i in range(N):
            if i in visit:
                continue

            start, curr = i, i

            curr_visit = set()

            while curr not in visit:
                visit.add(curr)
                curr_visit.add(curr)
                curr = favorite[curr]

            if curr in curr_visit:
                length = len(curr_visit)

                while start != curr:
                    length -= 1
                    start = favorite[start]

                longest_cycle = max(longest_cycle, length)

                if length == 2:
                    length_of_2_cycles.append([curr, favorite[curr]])

        inverted = defaultdict(list)

        for dst, src in enumerate(favorite):
            inverted[src].append(dst)

        def bfs(src, parent):
            q = deque([(src, 0)])
            max_length = 0

            while q:
                node, length = q.popleft()
                if node == parent:
                    continue
                max_length = max(max_length, length)
                for nei in inverted[node]:
                    q.append((nei, length + 1))

            return max_length

        chain_sum = 0

        for n1, n2 in length_of_2_cycles:
            chain_sum += bfs(n1, n2) + bfs(n2, n1) + 2

        return max(longest_cycle, chain_sum)


class TestSolution(unittest.TestCase):
    def test_1(self):
        favorite = [2, 2, 1, 2]
        output = 3
        self.assertEqual(Solution().maximumInvitations(favorite), output)

    def test_2(self):
        favorite = [1, 2, 0]
        output = 3
        self.assertEqual(Solution().maximumInvitations(favorite), output)

    def test_3(self):
        favorite = [3, 0, 1, 4, 1]
        output = 4
        self.assertEqual(Solution().maximumInvitations(favorite), output)
