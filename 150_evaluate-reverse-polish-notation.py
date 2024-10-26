from typing import List
import unittest


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif token == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(float(a) / b))
            else:
                stack.append(int(token))

        return stack.pop()


class TestEvalRPN(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.evalRPN(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(solution.evalRPN(["4", "13", "5", "/", "+"]), 6)
        self.assertEqual(
            solution.evalRPN(
                ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
            ),
            22,
        )
