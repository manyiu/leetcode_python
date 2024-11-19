import unittest


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {-1: 1}

        for i in range(len(s)):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i - 1]

            if i >= 1 and (s[i - 1] == "1" or (s[i - 1] == "2" and s[i] in "0123456")):
                dp[i] += dp[i - 2]

        return dp[len(s) - 1]

    # def numDecodings(self, s: str) -> int:
    #     def dfs(i: int) -> int:
    #         if i >= len(s):
    #             return 1

    #         if s[i] == "0":
    #             return 0

    #         res = dfs(i + 1)

    #         if i + 1 < len(s) and (
    #             s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")
    #         ):
    #             res += dfs(i + 2)

    #         return res

    #     return dfs(0)


class TestSolution(unittest.TestCase):
    def test_1(self):
        assert Solution().numDecodings("12") == 2

    def test_2(self):
        assert Solution().numDecodings("226") == 3

    def test_3(self):
        assert Solution().numDecodings("06") == 0
