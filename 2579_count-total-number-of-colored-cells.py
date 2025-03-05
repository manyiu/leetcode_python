import unittest


class Solution:
    def coloredCells(self, n: int) -> int:
        return n * n + (n - 1) * (n - 1)

    # def coloredCells(self, n: int) -> int:
    #     if n <= 1:
    #         return n

    #     res = 1

    #     for i in range(2, n + 1):
    #         res += 4 * (i - 1)

    #     return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        n = 1
        output = 1
        self.assertEqual(Solution().coloredCells(n), output)

    def test_2(self):
        n = 2
        output = 5
        self.assertEqual(Solution().coloredCells(n), output)

    def test_3(self):
        n = 3
        output = 13
        self.assertEqual(Solution().coloredCells(n), output)
