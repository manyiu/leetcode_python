from typing import List
import unittest


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if len(stack) == 0 or temperatures[i] <= stack[len(stack) - 1][1]:
                stack.append((i, temperatures[i]))
                continue
            if temperatures[i] > stack[len(stack) - 1][1]:
                while len(stack) > 0 and temperatures[i] > stack[len(stack) - 1][1]:
                    (popped_index, _) = stack.pop()
                    result[popped_index] = i - popped_index
                stack.append((i, temperatures[i]))

        return result


class TestDailyTemperatures(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual(
            solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]),
            [1, 1, 4, 2, 1, 1, 0, 0],
        )
        self.assertEqual(
            solution.dailyTemperatures([30, 40, 50, 60]),
            [1, 1, 1, 0],
        )
        self.assertEqual(
            solution.dailyTemperatures([30, 60, 90]),
            [1, 1, 0],
        )
        self.assertEqual(
            solution.dailyTemperatures([30, 30, 30, 30]),
            [0, 0, 0, 0],
        )
        self.assertEqual(
            solution.dailyTemperatures([30, 30, 60, 30]),
            [2, 1, 0, 0],
        )
