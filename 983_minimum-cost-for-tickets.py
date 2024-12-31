from typing import List
import unittest


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 366

        for i in range(1, 366):
            if i == days[0]:
                dp[i] = min(
                    dp[i - 1] + costs[0],
                    dp[i - 7] + costs[1] if i >= 7 else costs[1],
                    dp[i - 30] + costs[2] if i >= 30 else costs[2],
                )

                days.pop(0)

                if len(days) == 0:
                    dp[365] = dp[i]
                    break
            else:
                dp[i] = dp[i - 1]

        return dp[365]

    # def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    #     dp = [0] * (len(days) + 1)

    #     for i in range(len(days)):
    #         dp[i + 1] = dp[i] + costs[0]

    #         for j in range(i, -1, -1):
    #             if days[i] - days[j] <= 7 - 1:
    #                 dp[i + 1] = min(dp[i + 1], dp[j] + costs[1])
    #             if days[i] - days[j] <= 30 - 1:
    #                 dp[i + 1] = min(dp[i + 1], dp[j] + costs[2])
    #             if days[i] - days[j] > 30 - 1:
    #                 break

    #     return dp[len(days)]


class TestSolution(unittest.TestCase):
    def test_1(self):
        days = [1, 4, 6, 7, 8, 20]
        costs = [2, 7, 15]
        output = 11
        self.assertEqual(Solution().mincostTickets(days, costs), output)

    def test_2(self):
        days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
        costs = [2, 7, 15]
        output = 17
        self.assertEqual(Solution().mincostTickets(days, costs), output)
