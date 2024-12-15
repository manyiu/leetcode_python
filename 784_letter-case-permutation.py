from typing import List
import unittest


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = [""]

        for ch in s:
            if ord("0") <= ord(ch) <= ord("9"):
                for i in range(len(res)):
                    res[i] += ch
            else:
                temp = []
                for i in range(len(res)):
                    temp.append(res[i] + ch.lower())
                    temp.append(res[i] + ch.upper())
                res = temp

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "a1b2"
        res = ["a1b2", "a1B2", "A1b2", "A1B2"]
        self.assertCountEqual(Solution().letterCasePermutation(s), res)

    def test_2(self):
        s = "3z4"
        res = ["3z4", "3Z4"]
        self.assertCountEqual(Solution().letterCasePermutation(s), res)

    def test_3(self):
        s = "12345"
        res = ["12345"]
        self.assertCountEqual(Solution().letterCasePermutation(s), res)

    def test_4(self):
        s = "0"
        res = ["0"]
        self.assertCountEqual(Solution().letterCasePermutation(s), res)
