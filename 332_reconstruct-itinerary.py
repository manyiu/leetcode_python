from typing import List
import unittest


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}

        for src, dist in sorted(tickets):
            if src not in adj:
                adj[src] = []
            adj[src].append(dist)

        res = []

        def dfs(curr: str) -> None:
            while curr in adj and adj[curr]:
                dfs(adj[curr].pop(0))
            res.append(curr)

        dfs("JFK")

        return res[::-1]

    # def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    #     adj = {}

    #     for src, dist in sorted(tickets):
    #         if src not in adj:
    #             adj[src] = []
    #         adj[src].append(dist)

    #     res = ["JFK"]
    #     curr = "JFK"

    #     def dfs(curr: str) -> bool:
    #         if curr not in adj or not adj[curr]:
    #             if len(res) == 1 + len(tickets):
    #                 return True
    #             else:
    #                 return False

    #         for i in range(len(adj[curr])):
    #             next = adj[curr].pop(i)
    #             res.append(next)
    #             if dfs(next):
    #                 return True
    #             adj[curr].insert(i, next)
    #             res.pop()

    #         return False

    #     dfs(curr)

    #     return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        res = ["JFK", "MUC", "LHR", "SFO", "SJC"]
        self.assertEqual(Solution().findItinerary(tickets), res)

    def test_2(self):
        tickets = [
            ["JFK", "SFO"],
            ["JFK", "ATL"],
            ["SFO", "ATL"],
            ["ATL", "JFK"],
            ["ATL", "SFO"],
        ]
        res = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
        self.assertEqual(Solution().findItinerary(tickets), res)

    def test_3(self):
        tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
        res = ["JFK", "NRT", "JFK", "KUL"]
        self.assertEqual(Solution().findItinerary(tickets), res)
