from typing import List
import unittest


# class SegementTree:
#     def __init__(self, total, L, R):
#         self.sum = total
#         self.left = None
#         self.right = None
#         self.L = L
#         self.R = R

#     def build(nums: List[int], L: int, R: int):
#         if L == R:
#             return SegementTree(nums[L], L, R)

#         M = (L + R) // 2

#         root = SegementTree(0, L, R)
#         root.left = SegementTree.build(nums, L, M)
#         root.right = SegementTree.build(nums, M + 1, R)
#         root.sum = root.left.sum + root.right.sum

#         return root

#     def rangeQuery(self, L: int, R: int) -> int:
#         if L == self.L and R == self.R:
#             return self.sum

#         M = (self.L + self.R) // 2

#         if L > M:
#             return self.right.rangeQuery(L, R)
#         if R <= M:
#             return self.left.rangeQuery(L, R)
#         else:
#             return self.left.rangeQuery(L, M) + self.right.rangeQuery(M + 1, R)


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ["a", "e", "i", "o", "u"]

        prefixSum = [0] * len(words)

        for i, word in enumerate(words):
            if i > 0:
                prefixSum[i] = prefixSum[i - 1]

            if word[0] in vowels and word[-1] in vowels:
                prefixSum[i] += 1

        res = []

        for l, r in queries:
            ans = prefixSum[r] - prefixSum[l - 1] if l > 0 else prefixSum[r]

            res.append(ans)

        return res

    # def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
    #     wordsVowel = []

    #     voewls = ["a", "e", "i", "o", "u"]

    #     for word in words:
    #         if word[0] in voewls and word[-1] in voewls:
    #             wordsVowel.append(1)
    #         else:
    #             wordsVowel.append(0)

    #     st = SegementTree.build(wordsVowel, 0, len(words) - 1)

    #     res = []

    #     for l, r in queries:
    #         res.append(st.rangeQuery(l, r))

    #     return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        words = ["aba", "bcb", "ece", "aa", "e"]
        queries = [[0, 2], [1, 4], [1, 1]]
        output = [2, 3, 0]
        assert Solution().vowelStrings(words, queries) == output

    def test_2(self):
        words = ["a", "e", "i"]
        queries = [[0, 2], [0, 1], [2, 2]]
        output = [3, 2, 1]
        assert Solution().vowelStrings(words, queries) == output

    def test_3(self):
        words = [
            "bzmxvzjxfddcuznspdcbwiojiqf",
            "mwguoaskvramwgiweogzulcinycosovozppl",
            "uigevazgbrddbcsvrvnngfrvkhmqszjicpieahs",
            "uivcdsboxnraqpokjzaayedf",
            "yalc",
            "bbhlbmpskgxmxosft",
            "vigplemkoni",
            "krdrlctodtmprpxwditvcps",
            "gqjwokkskrb",
            "bslxxpabivbvzkozzvdaykaatzrpe",
            "qwhzcwkchluwdnqjwhabroyyxbtsrsxqjnfpadi",
            "siqbezhkohmgbenbkikcxmvz",
            "ddmaireeouzcvffkcohxus",
            "kjzguljbwsxlrd",
            "gqzuqcljvcpmoqlnrxvzqwoyas",
            "vadguvpsubcwbfbaviedr",
            "nxnorutztxfnpvmukpwuraen",
            "imgvujjeygsiymdxp",
            "rdzkpk",
            "cuap",
            "qcojjumwp",
            "pyqzshwykhtyzdwzakjejqyxbganow",
            "cvxuskhcloxykcu",
            "ul",
            "axzscbjajazvbxffrydajapweci",
        ]
        queries = [
            [4, 4],
            [6, 17],
            [10, 17],
            [9, 18],
            [17, 22],
            [5, 23],
            [2, 5],
            [17, 21],
            [5, 17],
            [4, 8],
            [7, 17],
            [16, 19],
            [7, 12],
            [9, 20],
            [13, 23],
            [1, 5],
            [19, 19],
        ]
        output = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        assert Solution().vowelStrings(words, queries) == output
