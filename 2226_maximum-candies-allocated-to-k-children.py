from typing import List
import unittest


class Solution:
    def canAllocate(self, candies, k, n):
        curr = 0

        for candy in candies:
            curr += candy // n
            if curr >= k:
                return True

        return False

    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 1, max(candies)

        while l <= r:
            m = l + (r - l) // 2

            if self.canAllocate(candies, k, m):
                l = m + 1
            else:
                r = m - 1

        return r


class TestSolution(unittest.TestCase):
    def test_1(self):
        candies = [5, 8, 6]
        k = 3
        output = 5
        self.assertEqual(Solution().maximumCandies(candies, k), output)

    def test_2(self):
        candies = [2, 5]
        k = 11
        output = 0
        self.assertEqual(Solution().maximumCandies(candies, k), output)
