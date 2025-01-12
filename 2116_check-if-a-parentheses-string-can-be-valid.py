import unittest


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        locked_stack = []
        unlocked_stack = []

        for i, c in enumerate(s):
            if locked[i] == "0":
                unlocked_stack.append(i)
            elif c == "(":
                locked_stack.append(i)
            else:
                if locked_stack:
                    locked_stack.pop()
                elif unlocked_stack:
                    unlocked_stack.pop()
                else:
                    return False

        while locked_stack and unlocked_stack and locked_stack[-1] < unlocked_stack[-1]:
            locked_stack.pop()
            unlocked_stack.pop()

        if locked_stack:
            return False

        if len(unlocked_stack) % 2 != 0:
            return False

        return True


class TestSolution(unittest.TestCase):
    def test_1(self):
        input = "))()))"
        locked = "010100"
        output = True
        self.assertEqual(Solution().canBeValid(input, locked), output)

    def test_2(self):
        input = "()()"
        locked = "0000"
        output = True
        self.assertEqual(Solution().canBeValid(input, locked), output)

    def test_3(self):
        input = ")"
        locked = "0"
        output = False
        self.assertEqual(Solution().canBeValid(input, locked), output)

    def test_207(self):
        s = "())(()(()(())()())(())((())(()())((())))))(((((((())(()))))("
        locked = "100011110110011011010111100111011101111110000101001101001111"
        output = False
        self.assertEqual(Solution().canBeValid(s, locked), output)
