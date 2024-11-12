from typing import List
import unittest


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def backtrack(currLetters: str, i: int):
            if i >= len(digits):
                res.append(currLetters)
                return

            for letter in digitToLetters[digits[i]]:
                backtrack(currLetters + letter, i + 1)

        if digits:
            backtrack("", 0)

        return res


class TestSolution(unittest.TestCase):

    def test_solution(self):
        sol = Solution()

        self.assertListEqual(
            sol.letterCombinations("23"),
            ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
        )
        self.assertListEqual(
            sol.letterCombinations(""),
            [],
        )
        self.assertListEqual(
            sol.letterCombinations("2"),
            ["a", "b", "c"],
        )
        self.assertListEqual(
            sol.letterCombinations("7"),
            ["p", "q", "r", "s"],
        )
