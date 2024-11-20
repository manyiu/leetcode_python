import unittest


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2) + 1)

        for i in range(1, len(text1) + 1):
            working = [0] * (len(dp))

            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    working[j] = dp[j - 1] + 1
                else:
                    working[j] = max(working[j - 1], dp[j])

            dp = working

        return dp[-1]


class TestSolution(unittest.TestCase):
    def test_1(self):
        text1 = "abcde"
        text2 = "ace"
        assert Solution().longestCommonSubsequence(text1, text2) == 3

    def test_2(self):
        text1 = "abc"
        text2 = "abc"
        assert Solution().longestCommonSubsequence(text1, text2) == 3

    def test_3(self):
        text1 = "abc"
        text2 = "def"
        assert Solution().longestCommonSubsequence(text1, text2) == 0
