import unittest


class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while True:
            if n == 1:
                return True

            if n in visit:
                return False

            visit.add(n)

            temp = n
            sum = 0

            while temp > 0:
                sum += (temp % 10) ** 2
                temp //= 10

            n = sum


class TestSolution(unittest.TestCase):
    def test_0(self):
        n = 19
        self.assertEqual(Solution().isHappy(n), True)

    def test_1(self):
        n = 2
        self.assertEqual(Solution().isHappy(n), False)

    def test_2(self):
        n = 7
        self.assertEqual(Solution().isHappy(n), True)

    def test_3(self):
        n = 1111111
        self.assertEqual(Solution().isHappy(n), True)

    def test_4(self):
        n = 1111112
        self.assertEqual(Solution().isHappy(n), False)
