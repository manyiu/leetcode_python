import unittest


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        cache = {}

        def dfs(i: int, j: int) -> bool:

            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if j + 1 < len(p) and p[j + 1] == "*":
                cache[(i, j)] = (match and dfs(i + 1, j)) or dfs(i, j + 2)
                return cache[(i, j)]

            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            cache[(i, j)] = False
            return False

        return dfs(0, 0)


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "aa"
        p = "a"
        assert Solution().isMatch(s, p) == False

    def test_2(self):
        s = "aa"
        p = "a*"
        assert Solution().isMatch(s, p) == True

    def test_3(self):
        s = "ab"
        p = ".*"
        assert Solution().isMatch(s, p) == True

    def test_4(self):
        s = "aab"
        p = "c*a*b"
        assert Solution().isMatch(s, p) == True

    def test_5(self):
        s = "mississippi"
        p = "mis*is*p*."
        assert Solution().isMatch(s, p) == False
