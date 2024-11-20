import unittest


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for i in range(1, m):
            currDp = [0] * n
            currDp[0] = 1

            for j in range(1, n):
                currDp[j] = currDp[j - 1] + dp[j]

            dp = currDp

        return dp[n - 1]


class TestSolution(unittest.TestCase):
    def test_1(self):
        m = 3
        n = 7
        assert Solution().uniquePaths(m, n) == 28

    def test_2(self):
        m = 3
        n = 2
        assert Solution().uniquePaths(m, n) == 3
