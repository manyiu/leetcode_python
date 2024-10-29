import unittest


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x + 1

        while l <= r:
            m = (l + r) // 2

            if m * m > x:
                r = m - 1
            else:
                l = m + 1

        return r


class TestSolution(unittest.TestCase):
    def test(self):
        x = 4
        self.assertEqual(Solution().mySqrt(x), 2)
        x = 8
        self.assertEqual(Solution().mySqrt(x), 2)
        x = 1
        self.assertEqual(Solution().mySqrt(x), 1)
        x = 0
        self.assertEqual(Solution().mySqrt(x), 0)
        x = 2
        self.assertEqual(Solution().mySqrt(x), 1)
        x = 2147395599
        self.assertEqual(Solution().mySqrt(x), 46339)
