from collections import defaultdict
from typing import List
import unittest


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        curr = 0
        count = defaultdict(int)

        for i in range(len(A)):
            if count[A[i]] > 0:
                curr += 1
            count[A[i]] -= 1
            if count[B[i]] < 0:
                curr += 1
            count[B[i]] += 1
            res.append(curr)

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        A = [1, 3, 2, 4]
        B = [3, 1, 2, 4]
        output = [0, 2, 3, 4]
        self.assertEqual(output, Solution().findThePrefixCommonArray(A, B))

    def test_2(self):
        A = [2, 3, 1]
        B = [3, 1, 2]
        output = [0, 1, 3]
        self.assertEqual(output, Solution().findThePrefixCommonArray(A, B))
