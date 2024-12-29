from collections import defaultdict
from typing import List
import unittest


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10**9 + 7

        count = defaultdict(int)

        for word in words:
            for i, char in enumerate(word):
                count[(i, char)] += 1

        cache = {}

        def dfs(i, j):
            if i == len(target):
                return 1

            if j == len(words[0]):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            cache[(i, j)] = dfs(i, j + 1)
            cache[(i, j)] += count[(j, target[i])] * dfs(i + 1, j + 1)

            return cache[(i, j)] % mod

        return dfs(0, 0)

    # def numWays(self, words: List[str], target: str) -> int:
    #     mod = 10**9 + 7

    #     n = len(target)
    #     m = len(words[0])
    #     cache = {}

    #     def helper(i: int, j: int) -> int:
    #         if j >= n:
    #             return 1
    #         if i >= m:
    #             return 0

    #         if (i, j) in cache:
    #             return cache[(i, j)]

    #         res = 0

    #         for k in range(len(words)):
    #             if words[k][i] == target[j]:
    #                 res += helper(i + 1, j + 1)

    #         res += helper(i + 1, j)

    #         cache[(i, j)] = res

    #         return res % mod

    #     return helper(0, 0)


class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().numWays(["acca", "bbbb", "caca"], "aba"), 6)

    def test_2(self):
        self.assertEqual(Solution().numWays(["abba", "baab"], "bab"), 4)

    def test_3(self):
        self.assertEqual(Solution().numWays(["abcd"], "abcd"), 1)

    def test_4(self):
        self.assertEqual(
            Solution().numWays(
                [
                    "cbabddddbc",
                    "addbaacbbd",
                    "cccbacdccd",
                    "cdcaccacac",
                    "dddbacabbd",
                    "bdbdadbccb",
                    "ddadbacddd",
                    "bbccdddadd",
                    "dcabaccbbd",
                    "ddddcddadc",
                    "bdcaaaabdd",
                    "adacdcdcdd",
                    "cbaaadbdbb",
                    "bccbabcbab",
                    "accbdccadd",
                    "dcccaaddbc",
                    "cccccacabd",
                    "acacdbcbbc",
                    "dbbdbaccca",
                    "bdbddbddda",
                    "daabadbacb",
                    "baccdbaada",
                    "ccbabaabcb",
                    "dcaabccbbb",
                    "bcadddaacc",
                    "acddbbdccb",
                    "adbddbadab",
                    "dbbcdcbcdd",
                    "ddbabbadbb",
                    "bccbcbbbab",
                    "dabbbdbbcb",
                    "dacdabadbb",
                    "addcbbabab",
                    "bcbbccadda",
                    "abbcacadac",
                    "ccdadcaada",
                    "bcacdbccdb",
                ],
                "bcbbcccc",
            ),
            677452090,
        )
