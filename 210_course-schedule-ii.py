from typing import List
import unittest


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]

        for post, pre in prerequisites:
            adj[post].append(pre)

        path = set()
        visit = set()

        res = []

        def dfs(node: int) -> bool:
            if node in path:
                return False
            if node in visit:
                return True

            path.add(node)
            visit.add(node)

            for pre in adj[node]:
                if not dfs(pre):
                    return False

            path.remove(node)
            res.append(node)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res


class TestFindOrder(unittest.TestCase):
    def test_1(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        self.assertEqual(Solution().findOrder(numCourses, prerequisites), [0, 1])

    def test_2(self):
        numCourses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        self.assertEqual(Solution().findOrder(numCourses, prerequisites), [0, 1, 2, 3])

    def test_3(self):
        numCourses = 1
        prerequisites = []
        self.assertEqual(Solution().findOrder(numCourses, prerequisites), [0])

    def test_4(self):
        numCourses = 2
        prerequisites = [[0, 1], [1, 0]]
        self.assertEqual(Solution().findOrder(numCourses, prerequisites), [])

    def test_5(self):
        numCourses = 3
        prerequisites = [[0, 1], [0, 2], [1, 2]]
        self.assertEqual(Solution().findOrder(numCourses, prerequisites), [2, 1, 0])

    def test_6(self):
        numCourses = 3
        prerequisites = [[0, 1], [1, 2], [2, 0]]
        self.assertEqual(Solution().findOrder(numCourses, prerequisites), [])

    def test_7(self):
        numCourses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [0, 3]]
        self.assertEqual(Solution().findOrder(numCourses, prerequisites), [])

    def test_8(self):
        numCourses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [0, 3], [2, 3]]
        self.assertEqual(Solution().findOrder(numCourses, prerequisites), [])

    def test_9(self):
        numCourses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [0, 3], [2, 3], [1, 3]]
        self.assertEqual(Solution().findOrder(numCourses, prerequisites), [])
