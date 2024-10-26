from typing import List
import unittest


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(open: int, close: int, s: str):
            if open == close == n:
                result.append(s)

            if open < n:
                backtrack(open + 1, close, s + "(")

            if close < open:
                backtrack(open, close + 1, s + ")")

        backtrack(0, 0, "")

        return result


class TestGenerateParenthesis(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual(
            solution.generateParenthesis(3),
            ["((()))", "(()())", "(())()", "()(())", "()()()"],
        )
        self.assertEqual(solution.generateParenthesis(1), ["()"])
        self.assertEqual(solution.generateParenthesis(2), ["(())", "()()"])
        self.assertEqual(
            solution.generateParenthesis(4),
            [
                "(((())))",
                "((()()))",
                "((())())",
                "((()))()",
                "(()(()))",
                "(()()())",
                "(()())()",
                "(())(())",
                "(())()()",
                "()((()))",
                "()(()())",
                "()(())()",
                "()()(())",
                "()()()()",
            ],
        )
