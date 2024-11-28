import unittest


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x: float, n: int) -> float:
            if n == 0:
                return 1

            if x == 0:
                return 0

            res = helper(x, n // 2)
            res *= res
            res = res if n % 2 == 0 else res * x

            return res

        res = helper(x, abs(n))

        return 1 / res if n < 0 else res

    # def myPow(self, x: float, n: int) -> float:
    #     if n == 0:
    #         return 1

    #     res = x

    #     for _ in range(1, abs(n)):
    #         res *= x

    #     if n < 0:
    #         return 1 / res

    #     return res


class TestSolution(unittest.TestCase):
    def test_0(self):
        x = 2.00000
        n = 10
        self.assertEqual(Solution().myPow(x, n), 1024.00000)

    def test_1(self):
        x = 2.10000
        n = 3
        self.assertEqual(Solution().myPow(x, n), 9.26100)

    def test_2(self):
        x = 2.00000
        n = -2
        self.assertEqual(Solution().myPow(x, n), 0.25000)

    def test_3(self):
        x = 2.00000
        n = 0
        self.assertEqual(Solution().myPow(x, n), 1.00000)

    def test_4(self):
        x = 0.00001
        n = 2147483647
        self.assertEqual(Solution().myPow(x, n), 0.00000)

    def test_5(self):
        x = 1.00000
        n = 2147483647
        self.assertEqual(Solution().myPow(x, n), 1.00000)

    def test_6(self):
        x = 2.00000
        n = -2147483648
        self.assertEqual(Solution().myPow(x, n), 0.00000)
