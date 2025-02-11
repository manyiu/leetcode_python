import unittest


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []

        for ch in s:
            stack.append(ch)
            if len(stack) >= len(part) and "".join(stack[-len(part) :]) == part:
                stack = stack[: -len(part)]

        return "".join(stack)

    # def removeOccurrences(self, s: str, part: str) -> str:
    #     while len(s) != len(s.replace(part, "")):
    #         s = s.replace(part, "", 1)

    #     return s


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "daabcbaabcbc"
        part = "abc"
        output = "dab"
        self.assertEqual(Solution().removeOccurrences(s, part), output)

    def test_2(self):
        s = "axxxxyyyyb"
        part = "xy"
        output = "ab"
        self.assertEqual(Solution().removeOccurrences(s, part), output)
