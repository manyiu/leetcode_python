import unittest


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

        for i in range(len(str1)):
            for j in range(len(str2)):
                if str1[i] == str2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        i, j = len(str1) - 1, len(str2) - 1

        res = ""

        while i >= 0 and j >= 0:
            if str1[i] == str2[j]:
                res = str1[i] + res

                i -= 1
                j -= 1

                continue

            if dp[i + 1][j] > dp[i][j + 1]:
                res = str2[j] + res
                j -= 1
            else:
                res = str1[i] + res
                i -= 1

        while i >= 0:
            res = str1[i] + res
            i -= 1

        while j >= 0:
            res = str2[j] + res
            j -= 1

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        str1 = "abac"
        str2 = "cab"
        output = "cabac"
        self.assertEqual(Solution().shortestCommonSupersequence(str1, str2), output)

    def test_2(self):
        str1 = "abac"
        str2 = "cab"
        output = "cabac"
        self.assertEqual(Solution().shortestCommonSupersequence(str1, str2), output)
