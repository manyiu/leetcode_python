from typing import List
import unittest


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        visit = set()
        path = set()

        for a, b in prerequisites:
            if a not in adj:
                adj[a] = []
            adj[a].append(b)

        def dfs(course: int) -> bool:
            if course in path:
                return False
            if course in visit:
                return True

            path.add(course)
            visit.add(course)

            if course in adj:
                for post in adj[course]:
                    if not dfs(post):
                        return False

            path.remove(course)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


class TestCanFinish(unittest.TestCase):
    def test_1(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        self.assertEqual(Solution().canFinish(numCourses, prerequisites), True)

    def test_2(self):
        numCourses = 2
        prerequisites = [[1, 0], [0, 1]]
        self.assertEqual(Solution().canFinish(numCourses, prerequisites), False)

    def test_3(self):
        numCourses = 3
        prerequisites = [[1, 0], [2, 1]]
        self.assertEqual(Solution().canFinish(numCourses, prerequisites), True)

    def test_4(self):
        numCourses = 3
        prerequisites = [[1, 0], [2, 1], [0, 2]]
        self.assertEqual(Solution().canFinish(numCourses, prerequisites), False)
