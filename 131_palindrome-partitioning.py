from typing import List
import unittest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i: int):
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s[i : j + 1]):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)

        return res


class TestSolution(unittest.TestCase):

    def test_solution(self):
        sol = Solution()

        self.assertListEqual(
            sol.partition("aab"),
            [["a", "a", "b"], ["aa", "b"]],
        )
        self.assertListEqual(
            sol.partition("a"),
            [["a"]],
        )
        self.assertListEqual(
            sol.partition("cdd"),
            [["c", "d", "d"], ["c", "dd"]],
        )
