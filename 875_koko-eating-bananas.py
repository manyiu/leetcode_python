import math
from typing import List
import unittest


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = 0

        for pile in piles:
            max_pile = max(max_pile, pile)

        l, r = 1, max_pile

        def get_hour_to_eat(eat_per_hour: int) -> int:
            count = 0

            for pile in piles:
                count += math.ceil(pile / eat_per_hour)

            return count

        while l <= r:
            m = (l + r) // 2

            hour_to_eat = get_hour_to_eat(m)

            if hour_to_eat <= h:
                r = m - 1
            else:
                l = m + 1

        return l


class TestMinEatingSpeed(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual(
            solution.minEatingSpeed([3, 6, 7, 11], 8),
            4,
        )
        self.assertEqual(
            solution.minEatingSpeed([30, 11, 23, 4, 20], 5),
            30,
        )
        self.assertEqual(
            solution.minEatingSpeed([30, 11, 23, 4, 20], 6),
            23,
        )
        self.assertEqual(
            solution.minEatingSpeed([312884470], 312884469),
            2,
        )
        self.assertEqual(
            solution.minEatingSpeed([1, 1, 1, 999999999], 10),
            142857143,
        )
