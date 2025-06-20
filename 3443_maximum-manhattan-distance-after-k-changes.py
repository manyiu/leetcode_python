from collections import defaultdict
import unittest


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = 0

        for c in s:
            count[c] += 1

            x_diff = abs(count["N"] - count["S"])
            y_diff = abs(count["W"] - count["E"])

            x_min = min(count["N"], count["S"])
            y_min = min(count["W"], count["E"])

            extra = min(k, x_min + y_min)

            res = max(res, x_diff + y_diff + 2 * extra)

        return res


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        s = "NWSE"
        k = 1
        expected = 3
        actual = Solution().maxDistance(s, k)
        self.assertEqual(actual, expected)

    def test_example_2(self):
        s = "NSWWEW"
        k = 3
        expected = 6
        actual = Solution().maxDistance(s, k)
        self.assertEqual(actual, expected)
