import unittest


class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def count(upper: int) -> int:
            m = len(str(upper))
            n = len(s)
            d = m - n

            if d < 0:
                return 0

            # dp[i][tight],
            # i : index of prefix
            # tight: 0 - not tight, 1 - tight
            dp = [[0] * 2 for _ in range(d + 1)]

            dp[d][0] = 1
            dp[d][1] = int(str(upper)[d:] >= s)

            for i in range(d - 1, -1, -1):
                digit = int(str(upper)[i])

                dp[i][0] = dp[i + 1][0] * (limit + 1)

                if digit <= limit:
                    dp[i][1] = dp[i + 1][0] * digit + dp[i + 1][1]
                else:
                    dp[i][1] = dp[i + 1][0] * (limit + 1)

            return dp[0][1]

        return count(finish) - count(start - 1)


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        start = 1
        finish = 6000
        limit = 4
        s = "124"
        expected = 5
        self.assertEqual(
            Solution().numberOfPowerfulInt(start, finish, limit, s), expected
        )

    def test_example_2(self):
        start = 15
        finish = 215
        limit = 6
        s = "10"
        expected = 2
        self.assertEqual(
            Solution().numberOfPowerfulInt(start, finish, limit, s), expected
        )

    def test_example_3(self):
        start = 1000
        finish = 2000
        limit = 4
        s = "3000"
        expected = 0
        self.assertEqual(
            Solution().numberOfPowerfulInt(start, finish, limit, s), expected
        )
