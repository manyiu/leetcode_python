from typing import List
import unittest


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        adj = [[] for _ in range(numCourses)]

        for pre, post in prerequisites:
            adj[pre].append(post)

        full_prerequisites = {}

        def dfs(course):
            if course not in full_prerequisites:
                full_prerequisites[course] = set()
                for pre in adj[course]:
                    full_prerequisites[course] |= dfs(pre)
                full_prerequisites[course].add(course)
            return full_prerequisites[course]

        for i in range(numCourses):
            dfs(i)

        res = []

        for pre, post in queries:
            res.append(post in full_prerequisites[pre])

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        queries = [[0, 1], [1, 0]]
        output = [False, True]
        self.assertEqual(
            Solution().checkIfPrerequisite(numCourses, prerequisites, queries), output
        )

    def test_2(self):
        numCourses = 2
        prerequisites = []
        queries = [[1, 0], [0, 1]]
        output = [False, False]
        self.assertEqual(
            Solution().checkIfPrerequisite(numCourses, prerequisites, queries), output
        )

    def test_3(self):
        numCourses = 3
        prerequisites = [[1, 2], [1, 0], [2, 0]]
        queries = [[1, 0], [1, 2]]
        output = [True, True]
        self.assertEqual(
            Solution().checkIfPrerequisite(numCourses, prerequisites, queries), output
        )
