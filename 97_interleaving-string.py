import unittest


class Solution:
    # def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    #     if len(s1) + len(s2) != len(s3):
    #         return False

    #     m, n = len(s1), len(s2)
    #     dp = [[False] * (n + 1) for _ in range(m + 1)]

    #     dp[m][n] = True

    #     for i in range(m, -1, -1):
    #         for j in range(n, -1, -1):
    #             if i < m and s1[i] == s3[i + j] and dp[i + 1][j]:
    #                 dp[i][j] = True
    #             if j < n and s2[j] == s3[i + j] and dp[i][j + 1]:
    #                 dp[i][j] = True

    #     return dp[0][0]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        m, n = len(s1), len(s2)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True

        for i in range(m + 1):
            for j in range(n + 1):
                if i > 0 and s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]:
                    dp[i][j] = True
                if j > 0 and s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]:
                    dp[i][j] = True

        return dp[m][n]

    # def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    #     if len(s1) + len(s2) != len(s3):
    #         return False

    #     cache = {}

    #     def dfs(i: int, j: int) -> bool:
    #         if i >= len(s1) and j >= len(s2) and i + j >= len(s3):
    #             return True

    #         if (i, j) in cache:
    #             return cache[(i, j)]

    #         res = False

    #         if i < len(s1) and s1[i] == s3[i + j]:
    #             if dfs(i + 1, j):
    #                 res = True

    #         if j < len(s2) and s2[j] == s3[i + j]:
    #             if dfs(i, j + 1):
    #                 res = True

    #         cache[(i, j)] = res

    #         return res

    #     return dfs(0, 0)


class TestSolution(unittest.TestCase):
    def test_1(self):
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbcbcac"
        assert Solution().isInterleave(s1, s2, s3) == True


[
    [True, False, False, False, False, False],
    [True, False, False, False, False, False],
    [True, True, True, True, True, False],
    [False, True, True, False, True, False],
    [False, False, True, True, True, True],
    [False, False, False, False, False, True],
]

# def test_2(self):
#     s1 = "aabcc"
#     s2 = "dbbca"
#     s3 = "aadbbbaccc"
#     assert Solution().isInterleave(s1, s2, s3) == False

# def test_3(self):
#     s1 = ""
#     s2 = ""
#     s3 = ""
#     assert Solution().isInterleave(s1, s2, s3) == True

# def test_4(self):
#     s1 = ""
#     s2 = ""
#     s3 = "a"
#     assert Solution().isInterleave(s1, s2, s3) == False

# def test_5(self):
#     s1 = "a"
#     s2 = "b"
#     s3 = "a"
#     assert Solution().isInterleave(s1, s2, s3) == False
