import unittest


class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch.isdigit() and stack:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "abc"
        output = "abc"
        self.assertEqual(Solution().clearDigits(s), output)

    def test_2(self):
        s = "cb34"
        output = ""
        self.assertEqual(Solution().clearDigits(s), output)
