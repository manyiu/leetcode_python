import unittest
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        curr_counter = {}
        res = 0
        l = 0

        for r in range(n):
            if fruits[r] not in curr_counter:
                curr_counter[fruits[r]] = 0
            curr_counter[fruits[r]] += 1

            while len(curr_counter) > 2:
                curr_counter[fruits[l]] -= 1
                if curr_counter[fruits[l]] == 0:
                    del curr_counter[fruits[l]]
                l += 1

            res = max(res, r - l + 1)

        return res


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        fruits = [1, 2, 1]
        expected = 3
        actual = Solution().totalFruit(fruits)
        self.assertEqual(actual, expected)

    def test_example_2(self):
        fruits = [0, 1, 2, 2]
        expected = 3
        actual = Solution().totalFruit(fruits)
        self.assertEqual(actual, expected)

    def test_example_3(self):
        fruits = [1, 2, 3, 2, 2]
        expected = 4
        actual = Solution().totalFruit(fruits)
        self.assertEqual(actual, expected)
