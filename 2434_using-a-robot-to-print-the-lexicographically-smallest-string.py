from typing import Counter
import unittest


class Solution:
    def robotWithString(self, s: str) -> str:
        counter = Counter(s)
        stack = []
        res = []

        min_char = 0

        for c in s:
            stack.append(c)
            counter[c] -= 1

            while min_char < 25 and counter[chr(min_char + ord("a"))] == 0:
                min_char += 1
            while stack and ord(stack[-1]) - ord("a") <= min_char:
                res.append(stack.pop())

        return "".join(res)

        

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        s = "zza"
        expected = "azz"
        solution = Solution()
        result = solution.robotWithString(s)
        self.assertEqual(result, expected)

    def test_example_2(self):
        s = "bac"
        expected = "abc"
        solution = Solution()
        result = solution.robotWithString(s)
        self.assertEqual(result, expected)

    def test_example_3(self):
        s = "bdda"
        expected = "addb"
        solution = Solution()
        result = solution.robotWithString(s)
        self.assertEqual(result, expected)