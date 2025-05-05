import unittest


class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n

        MOD = 10**9+7
        
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = (2 * dp[i-1] + dp[i-3]) % MOD

        return dp[n]

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        n = 3
        expected = 5
        self.assertEqual(Solution().numTilings(n), expected)
    
    def test_example_2(self):
        n = 1
        expected = 1
        self.assertEqual(Solution().numTilings(n), expected)