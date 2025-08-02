import unittest
from typing import Counter, List


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count = Counter(basket1 + basket2)

        for c in count:
            if count[c] % 2 != 0:
                return -1
            count[c] //= 2

        basket1_list = list((Counter(basket1) - count).elements())
        basket2_list = list((Counter(basket2) - count).elements())

        small = min(count)

        combined = sorted(basket1_list + basket2_list)

        return sum(min(small * 2, combined[c]) for c in range(len(basket1_list)))


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        basket1 = [4, 2, 2, 2]
        basket2 = [1, 4, 1, 2]
        expect = 1
        actual = Solution().minCost(basket1, basket2)
        self.assertEqual(actual, expect)

    def test_example_2(self):
        basket1 = [2, 3, 4, 1]
        basket2 = [3, 2, 5, 1]
        expect = -1
        actual = Solution().minCost(basket1, basket2)
        self.assertEqual(actual, expect)
