import math
import unittest


class Solution:
    def reverse(self, x: int) -> int:
        MIN = -(2**31)
        MAX = 2**31 - 1

        res = 0

        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if (
                (res > MAX // 10)
                or (res < MIN // 10)
                or (res == MAX // 10 and digit > MAX % 10)
                or (res == MIN // 10 and digit < MIN % 10)
            ):
                return 0

            res = (res * 10) + digit

        return res


class TestSolution(unittest.TestCase):
    def test_0(self):
        solution = Solution()
        self.assertEqual(solution.reverse(123), 321)

    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.reverse(-123), -321)

    def test_2(self):
        solution = Solution()
        self.assertEqual(solution.reverse(120), 21)

    def test_3(self):
        solution = Solution()
        self.assertEqual(solution.reverse(0), 0)

    def test_4(self):
        solution = Solution()
        self.assertEqual(solution.reverse(1), 1)

    def test_5(self):
        solution = Solution()
        self.assertEqual(solution.reverse(-1), -1)

    def test_6(self):
        solution = Solution()
        self.assertEqual(solution.reverse(10), 1)

    def test_7(self):
        solution = Solution()
        self.assertEqual(solution.reverse(-10), -1)

    def test_8(self):
        solution = Solution()
        self.assertEqual(solution.reverse(1000000003), 0)

    def test_9(self):
        solution = Solution()
        self.assertEqual(solution.reverse(-1000000003), 0)

    def test_10(self):
        solution = Solution()
        self.assertEqual(solution.reverse(1534236469), 0)

    def test_11(self):
        solution = Solution()
        self.assertEqual(solution.reverse(-2147483648), 0)

    def test_12(self):
        solution = Solution()
        self.assertEqual(solution.reverse(2147483647), 0)

    def test_13(self):
        solution = Solution()
        self.assertEqual(solution.reverse(-2147483647), 0)

    def test_14(self):
        solution = Solution()
        self.assertEqual(solution.reverse(1563847412), 0)

    def test_15(self):
        solution = Solution()
        self.assertEqual(solution.reverse(-1563847412), 0)
