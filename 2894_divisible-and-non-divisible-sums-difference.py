import unittest


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1, num2 = 0, 0

        for i in range(1, n + 1):
            if i % m == 0:
                num2 += i
            else:
                num1 += i

        return num1 - num2

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        n = 10
        m = 3
        expected = 19
        result = Solution().differenceOfSums(n, m)
        self.assertEqual(result, expected)

    def test_example_2(self):
        n = 5
        m = 6
        expected = 15
        result = Solution().differenceOfSums(n, m)
        self.assertEqual(result, expected)

    def test_example_3(self):
        n = 5
        m = 1
        expected = -15
        result = Solution().differenceOfSums(n, m)
        self.assertEqual(result, expected)