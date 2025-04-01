from typing import List
import unittest


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * len(questions)

        for i in range(len(questions) - 1, -1, -1):
            points, brainpower = questions[i]

            next_index = i + brainpower + 1

            take = points + (dp[next_index] if next_index < len(questions) else 0)
            skip = dp[i + 1] if i + 1 < len(questions) else 0

            dp[i] = max(take, skip)

        return dp[0]

    # def mostPoints(self, questions: List[List[int]]) -> int:
    #     cache = [0] * len(questions)

    #     def backtrack(i: int) -> int:
    #         if i >= len(questions):
    #             return 0

    #         if cache[i]:
    #             return cache[i]

    #         points, brainpower = questions[i]

    #         take = points + backtrack(i + brainpower + 1)
    #         skip = backtrack(i + 1)

    #         cache[i] = max(take, skip)

    #         return cache[i]

    #     return backtrack(0)


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
        expected = 5
        self.assertEqual(Solution().mostPoints(questions), expected)

    def test_example_2(self):
        questions = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
        expected = 7
        self.assertEqual(Solution().mostPoints(questions), expected)
