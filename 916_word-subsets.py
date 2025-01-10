from collections import defaultdict
from typing import List
import unittest


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []

        words2_max_freq = defaultdict(int)

        for word2 in words2:
            word2_freq = defaultdict(int)
            for ch2 in word2:
                word2_freq[ch2] += 1
                words2_max_freq[ch2] = max(words2_max_freq[ch2], word2_freq[ch2])

        for word1 in words1:
            word1_freq = defaultdict(int)

            for ch1 in word1:
                word1_freq[ch1] += 1

            is_subset = True

            for ch2 in words2_max_freq:
                if word1_freq[ch2] < words2_max_freq[ch2]:
                    is_subset = False
                    break

            if is_subset:
                res.append(word1)

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
        words2 = ["e", "o"]
        output = ["facebook", "google", "leetcode"]
        self.assertEqual(Solution().wordSubsets(words1, words2), output)

    def test_2(self):
        words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
        words2 = ["l", "e"]
        output = ["apple", "google", "leetcode"]
        self.assertEqual(Solution().wordSubsets(words1, words2), output)

    def test_3(self):
        words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
        words2 = ["e", "oo"]
        output = ["facebook", "google"]
        self.assertEqual(Solution().wordSubsets(words1, words2), output)

    def test_4(self):
        words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
        words2 = ["lo", "eo"]
        output = ["google", "leetcode"]
        self.assertEqual(Solution().wordSubsets(words1, words2), output)
