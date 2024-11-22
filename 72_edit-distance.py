import unittest


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = [[float("-infinity")] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i

        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        return dp[m][n]

    # def minDistance(self, word1: str, word2: str) -> int:
    #     m, n = len(word1), len(word2)

    #     cache = {}

    #     def dfs(i: int, j: int) -> int:
    #         if i == m:
    #             return n - j
    #         if j == n:
    #             return m - i

    #         if (i, j) in cache:
    #             return cache[(i, j)]

    #         if word1[i] == word2[j]:
    #             res = dfs(i + 1, j + 1)
    #             cache[(i, j)] = res
    #             return res

    #         res = 1 + min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))

    #         cache[(i, j)] = res

    #         return res

    #     return dfs(0, 0)

    # def minDistance(self, word1: str, word2: str) -> int:
    #     m, n = len(word1), len(word2)

    #     def dfs(i: int, j: int) -> int:
    #         if i == m:
    #             return n - j
    #         if j == n:
    #             return m - i

    #         if word1[i] == word2[j]:
    #             return dfs(i + 1, j + 1)

    #         res = 1 + min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))

    #         return res

    #     return dfs(0, 0)


class TestSolution(unittest.TestCase):
    def test_1(self):
        word1 = "horse"
        word2 = "ros"
        assert Solution().minDistance(word1, word2) == 3

    def test_2(self):
        word1 = "intention"
        word2 = "execution"
        assert Solution().minDistance(word1, word2) == 5

    def test_3(self):
        word1 = ""
        word2 = ""
        assert Solution().minDistance(word1, word2) == 0

    def test_4(self):
        word1 = "a"
        word2 = "a"
        assert Solution().minDistance(word1, word2) == 0

    def test_5(self):
        word1 = "a"
        word2 = "b"
        assert Solution().minDistance(word1, word2) == 1

    def test_6(self):
        word1 = "a"
        word2 = ""
        assert Solution().minDistance(word1, word2) == 1

    def test_7(self):
        word1 = ""
        word2 = "a"
        assert Solution().minDistance(word1, word2) == 1

    def test_8(self):
        word1 = "a"
        word2 = "ab"
        assert Solution().minDistance(word1, word2) == 1

    def test_9(self):
        word1 = "ab"
        word2 = "a"
        assert Solution().minDistance(word1, word2) == 1

    def test_10(self):
        word1 = "ab"
        word2 = "ac"
        assert Solution().minDistance(word1, word2) == 1

    def test_11(self):
        word1 = "ab"
        word2 = "bc"
        assert Solution().minDistance(word1, word2) == 2

    def test_12(self):
        word1 = "abc"
        word2 = "bc"
        assert Solution().minDistance(word1, word2) == 1

    def test_13(self):
        word1 = "abc"
        word2 = "bcd"
        assert Solution().minDistance(word1, word2) == 2
