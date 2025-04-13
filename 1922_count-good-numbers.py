import unittest


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        num_even = (n + 1) // 2
        num_odd = n - num_even

        count = pow(5, num_even, MOD) * pow(4, num_odd, MOD)

        return count % MOD


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        n = 1
        expected = 5
        self.assertEqual(Solution().countGoodNumbers(n), expected)

    def test_example_2(self):
        n = 4
        expected = 400
        self.assertEqual(Solution().countGoodNumbers(n), expected)

    def test_example_3(self):
        n = 50
        expected = 564908303
        self.assertEqual(Solution().countGoodNumbers(n), expected)
