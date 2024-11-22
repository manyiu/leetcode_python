import unittest


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = 1

        for i in range(m + 1):
            for j in range(n + 1):
                if i > 0:
                    dp[i][j] = dp[i - 1][j]
                if i > 0 and j > 0 and s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[m][n]

    # def numDistinct(self, s: str, t: str) -> int:
    #     cache = {}

    #     def dfs(i: int, j: int) -> int:
    #         if j >= len(t):
    #             return 1

    #         if i >= len(s):
    #             return 0

    #         if (i, j) in cache:
    #             return cache[(i, j)]

    #         res = dfs(i + 1, j)

    #         if s[i] == t[j]:
    #             res += dfs(i + 1, j + 1)

    #         cache[(i, j)] = res

    #         return res

    #     return dfs(0, 0)


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "rabbbit"
        t = "rabbit"
        assert Solution().numDistinct(s, t) == 3

    def test_2(self):
        s = "babgbag"
        t = "bag"
        assert Solution().numDistinct(s, t) == 5

    def test_3(self):
        s = "a"
        t = "a"
        assert Solution().numDistinct(s, t) == 1

    def test_4(self):
        s = "a"
        t = "b"
        assert Solution().numDistinct(s, t) == 0

    def test_5(self):
        s = "a"
        t = ""
        assert Solution().numDistinct(s, t) == 1

    def test_6(self):
        s = ""
        t = "a"
        assert Solution().numDistinct(s, t) == 0

    def test_7(self):
        s = ""
        t = ""
        assert Solution().numDistinct(s, t) == 1
