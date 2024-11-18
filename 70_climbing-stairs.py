import unittest


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [1, 2]

        for _ in range(3, n + 1):
            dp[0], dp[1] = dp[1], dp[0] + dp[1]

        return dp[1]

    # def climbStairs(self, n: int) -> int:
    #     dp = [0] * (n + 1)
    #     dp[1], dp[2] = 1, 2

    #     for i in range(3, n + 1):
    #         dp[i] = dp[i - 1] + dp[i - 2]

    #     return dp[n]

    # def climbStairs(self, n: int) -> int:
    #     cache = [-1] * n

    #     def dfs(i):
    #         if i <= 2:
    #             return i

    #         if cache[i - 1] != -1:
    #             return cache[i - 1]

    #         cache[i - 1] = self.climbStairs(i - 1) + self.climbStairs(i - 2)
    #         return cache[i - 1]

    #     return dfs(n)

    # def climbStairs(self, n: int) -> int:
    #     if n <= 2:
    #         return n

    #     return self.climbStairs(n - 2) + self.climbStairs(n - 1)


class TestSolution(unittest.TestCase):
    def test(self):
        assert Solution().climbStairs(2) == 2
        assert Solution().climbStairs(3) == 3
        assert Solution().climbStairs(4) == 5
        assert Solution().climbStairs(5) == 8
        assert Solution().climbStairs(6) == 13
        assert Solution().climbStairs(7) == 21
        assert Solution().climbStairs(8) == 34
        assert Solution().climbStairs(9) == 55
        assert Solution().climbStairs(10) == 89
        assert Solution().climbStairs(11) == 144
        assert Solution().climbStairs(12) == 233
        assert Solution().climbStairs(13) == 377
        assert Solution().climbStairs(14) == 610
        assert Solution().climbStairs(15) == 987
        assert Solution().climbStairs(16) == 1597
        assert Solution().climbStairs(17) == 2584
        assert Solution().climbStairs(18) == 4181
        assert Solution().climbStairs(19) == 6765
        assert Solution().climbStairs(20) == 10946
        assert Solution().climbStairs(21) == 17711
        assert Solution().climbStairs(22) == 28657
        assert Solution().climbStairs(23) == 46368
        assert Solution().climbStairs(24) == 75025
        assert Solution().climbStairs(25) == 121393
        assert Solution().climbStairs(26) == 196418
        assert Solution().climbStairs(27) == 317811
        assert Solution().climbStairs(28) == 514229
        assert Solution().climbStairs(29) == 832040
        assert Solution().climbStairs(30) == 1346269
