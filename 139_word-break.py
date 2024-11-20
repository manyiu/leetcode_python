from typing import List
import unittest


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(dp)):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[len(dp) - 1]

    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     def dfs(currWord: str) -> bool:
    #         if currWord == s:
    #             return True
    #         if len(currWord) >= len(s) or currWord != s[: len(currWord)]:
    #             return False

    #         for word in wordDict:
    #             if dfs(currWord + word):
    #                 return True

    #         return False

    #     return dfs("")


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "leetcode"
        wordDict = ["leet", "code"]
        assert Solution().wordBreak(s, wordDict) == True

    def test_2(self):
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        assert Solution().wordBreak(s, wordDict) == True

    def test_3(self):
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        assert Solution().wordBreak(s, wordDict) == False

    def test_4(self):
        s = "cars"
        wordDict = ["car", "ca", "rs"]
        assert Solution().wordBreak(s, wordDict) == True

    def test_5(self):
        s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
        wordDict = [
            "a",
            "aa",
            "aaa",
            "aaaa",
            "aaaaa",
            "aaaaaa",
            "aaaaaaa",
            "aaaaaaaa",
            "aaaaaaaaa",
            "aaaaaaaaaa",
        ]
        assert Solution().wordBreak(s, wordDict) == False
