from typing import List
import unittest


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        current = 1

        for _ in range(n):
            result.append(current)
            if current * 10 <= n:
                current *= 10
            else:
                while current % 10 == 9 or current + 1 > n:
                    current //= 10
                current += 1

        return result


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        n = 13
        expected = [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
        solution = Solution()
        result = solution.lexicalOrder(n)
        self.assertEqual(result, expected)

    def test_example_2(self):
        n = 2
        expected = [1, 2]
        solution = Solution()
        result = solution.lexicalOrder(n)
        self.assertEqual(result, expected)
