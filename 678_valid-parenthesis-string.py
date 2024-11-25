import unittest


class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == ")":
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0

        return leftMin == 0


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "()"
        assert Solution().checkValidString(s) == True

    def test_2(self):
        s = "(*)"
        assert Solution().checkValidString(s) == True

    def test_3(self):
        s = "(*))"
        assert Solution().checkValidString(s) == True

    def test_4(self):
        s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
        assert Solution().checkValidString(s) == False
