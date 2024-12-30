import unittest


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7

        dp = [0] * (high + 1)

        dp[0] = 1

        for i in range(1, high + 1):
            if i - zero >= 0:
                dp[i] += dp[i - zero]
            if i - one >= 0:
                dp[i] += dp[i - one]

        return sum(dp[low : high + 1]) % mod

    # def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
    #     mod = 10**9 + 7

    #     cache = {}

    #     def dfs(length: int) -> int:
    #         if length > high:
    #             return 0
    #         if length in cache:
    #             return cache[length]

    #         cache[length] = 0

    #         if length >= low:
    #             cache[length] += 1

    #         cache[length] += dfs(length + zero) + dfs(length + one)

    #         return cache[length] % mod

    #     return dfs(0)


class TestSolution(unittest.TestCase):
    def test_1(self):
        low = 3
        high = 3
        zero = 1
        one = 1
        output = 8
        self.assertEqual(Solution().countGoodStrings(low, high, zero, one), output)

    def test_2(self):
        low = 2
        high = 3
        zero = 1
        one = 2
        output = 5
        self.assertEqual(Solution().countGoodStrings(low, high, zero, one), output)
