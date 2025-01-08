from typing import List
import unittest


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if (
                    words[j][: len(words[i])] == words[i]
                    and words[j][-len(words[i]) :] == words[i]
                ):
                    res += 1

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        input = ["a", "aba", "ababa", "aa"]
        output = 4
        self.assertEqual(Solution().countPrefixSuffixPairs(input), output)

    def test_2(self):
        input = ["pa", "papa", "ma", "mama"]
        output = 2
        self.assertEqual(Solution().countPrefixSuffixPairs(input), output)

    def test_3(self):
        input = ["abab", "ab"]
        output = 0
        self.assertEqual(Solution().countPrefixSuffixPairs(input), output)
