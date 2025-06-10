from collections import defaultdict
import unittest


class Solution:
    def maxDifference(self, s: str) -> int:
        max_odd_freq = -float("inf")
        min_even_freq = float("inf")

        ch_freq = defaultdict(int)

        for ch in s:
            ch_freq[ch] += 1

        for freq in ch_freq.values():
            if freq % 2 == 0:
                min_even_freq = min(min_even_freq, freq)
            else:
                max_odd_freq = max(max_odd_freq, freq)

        if max_odd_freq == -float("inf") and min_even_freq == float("inf"):
            return 0
        elif max_odd_freq == -float("inf"):
            return -int(min_even_freq)
        elif min_even_freq == float("inf"):
            return int(max_odd_freq)

        return int(max_odd_freq - min_even_freq)


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        s = "aaaaabbc"
        expected = 3
        solution = Solution()
        result = solution.maxDifference(s)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_example_2(self):
        s = "abcabcab"
        expected = 1
        solution = Solution()
        result = solution.maxDifference(s)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")
