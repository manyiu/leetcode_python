from typing import List
import unittest


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        prevIndex = 0

        for space in spaces:
            res += s[prevIndex:space] + " "
            prevIndex = space

        res += s[prevIndex:]

        return res


class TestSolution(unittest.TestCase):
    def test_0(self):
        solution = Solution()
        self.assertEqual(
            solution.addSpaces("LeetcodeHelpsMeLearn", [8, 13, 15]),
            "Leetcode Helps Me Learn",
        )

    def test_1(self):
        solution = Solution()
        self.assertEqual(
            solution.addSpaces("icodeinpython", [1, 5, 7, 9]),
            "i code in py thon",
        )

    def test_2(self):
        solution = Solution()
        self.assertEqual(
            solution.addSpaces("spacing", [0, 1, 2, 3, 4, 5, 6]),
            " s p a c i n g",
        )
