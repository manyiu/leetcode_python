from typing import List
import unittest


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        res = 0
        total = 0

        bannedHash = set()

        for num in banned:
            if 1 <= num <= n:
                bannedHash.add(num)

        for i in range(1, n + 1):
            if i not in bannedHash:
                total += i
                if total <= maxSum:
                    res += 1
                else:
                    break

        return res


class TestSolution(unittest.TestCase):
    def test_0(self):
        solution = Solution()
        self.assertEqual(
            solution.maxCount([1, 6, 5], 5, 6),
            2,
        )

    def test_1(self):
        solution = Solution()
        self.assertEqual(
            solution.maxCount([1, 2, 3, 4, 5, 6, 7], 8, 1),
            0,
        )

    def test_2(self):
        solution = Solution()
        self.assertEqual(
            solution.maxCount([11], 7, 50),
            7,
        )
