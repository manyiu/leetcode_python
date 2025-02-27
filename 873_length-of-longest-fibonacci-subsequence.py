from collections import defaultdict
from typing import List
import unittest


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        dp = defaultdict(int)
        s = set(arr)

        for i in range(len(arr)):
            for j in range(i):
                if arr[i] - arr[j] < arr[j] and arr[i] - arr[j] in s:
                    dp[arr[j], arr[i]] = dp.get((arr[i] - arr[j], arr[j]), 2) + 1

        return max(dp.values() or [0])

    # def lenLongestFibSubseq(self, arr: List[int]) -> int:
    #     s = set(arr)
    #     res = 2

    #     for i in range(len(arr)):
    #         for j in range(i):
    #             a, b = arr[j], arr[i]
    #             count = 2

    #             while a + b in s:
    #                 a, b = b, a + b
    #                 count += 1

    #             res = max(res, count)

    #     return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        output = 5
        self.assertEqual(Solution().lenLongestFibSubseq(arr), output)

    def test_2(self):
        arr = [1, 3, 7, 11, 12, 14, 18]
        output = 3
        self.assertEqual(Solution().lenLongestFibSubseq(arr), output)
