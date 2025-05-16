from typing import List
import unittest


class Solution:
    def isValid(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False
        
        diff_count = 0

        for i in range(len(a)):
            if a[i] != b[i]:
                diff_count += 1
                if diff_count > 1:
                    return False
                
        return diff_count == 1
    
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        N = len(words)

        if N == 0:
            return []

        dp = [0] * N
        parent = [-1] * N

        for i in range(N):
            for j in range(i):
                if groups[i] != groups[j] and self.isValid(words[i], words[j]):
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j

        max_length = dp[0]
        max_index = 0

        for i in range(1, N):
            if dp[i] >= max_length:
                max_length = dp[i]
                max_index = i

        curr_index = max_index

        res = []

        while curr_index >= 0:
            res.append(words[curr_index])
            curr_index = parent[curr_index]

        return res[::-1]


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        words = ["bab","dab","cab"]
        groups = [1,2,2]
        expected=  ["bab","cab"]
        result = Solution().getWordsInLongestSubsequence(words, groups)
        self.assertEqual(result, expected)

    def test_example_2(self):
        words = ["a","b","c","d"]
        groups = [1,2,3,4]
        expected=  ["a","b","c","d"]
        result = Solution().getWordsInLongestSubsequence(words, groups)
        self.assertEqual(result, expected)