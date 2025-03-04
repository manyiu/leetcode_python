import unittest


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def backtrack(i, curr) -> bool:
            if curr == n:
                return True

            if curr > n or 3**i > n:
                return False

            if backtrack(i + 1, curr + 3**i):
                return True

            if backtrack(i + 1, curr):
                return True

            return False

        return backtrack(0, 0)

    # def checkPowersOfThree(self, n: int) -> bool:
    #     for i in range(16, -1, -1):
    #         if n >= 3**i:
    #             n -= 3**i

    #     return n == 0


class TestSolution(unittest.TestCase):
    def test_1(self):
        n = 12
        output = True
        self.assertEqual(Solution().checkPowersOfThree(n), output)

    def test_2(self):
        n = 91
        output = True
        self.assertEqual(Solution().checkPowersOfThree(n), output)

    def test_3(self):
        n = 21
        output = False
        self.assertEqual(Solution().checkPowersOfThree(n), output)

    def test_4(self):
        n = 1
        output = True
        self.assertEqual(Solution().checkPowersOfThree(n), output)

    def test_5(self):
        n = 3
        output = True
        self.assertEqual(Solution().checkPowersOfThree(n), output)
