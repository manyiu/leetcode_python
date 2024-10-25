import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if len(stack) == 0 or bracket_map[c] != stack.pop():
                    return False
                
        return True if len(stack) == 0 else False
                
        
class TestSolution(unittest.TestCase):
    def test(self):
        s = "()"
        self.assertEqual(Solution().isValid(s), True)
        s = "()[]{}"
        self.assertEqual(Solution().isValid(s), True)
        s = "(]"
        self.assertEqual(Solution().isValid(s), False)
        s = "([)]"
        self.assertEqual(Solution().isValid(s), False)
        s = "{[]}"
        self.assertEqual(Solution().isValid(s), True)
        s = "}"
        self.assertEqual(Solution().isValid(s), False)
        s = ""
        self.assertEqual(Solution().isValid(s), True)
        s = "(("
        self.assertEqual(Solution().isValid(s), False)
        s = "))"
        self.assertEqual(Solution().isValid(s), False)
        