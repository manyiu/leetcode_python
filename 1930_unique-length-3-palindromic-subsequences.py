from typing import Counter
import unittest


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = set()
        right = Counter(s)
        res = set()

        for m in s:
            right[m] -= 1

            for l in left:
                if right[l] > 0:
                    res.add((l, m))

            left.add(m)

        return len(res)


class TestSolution(unittest.TestCase):
    def test_1(self):
        input = "aabca"
        output = 3
        assert Solution().countPalindromicSubsequence(input) == output

    def test_2(self):
        input = "adc"
        output = 0
        assert Solution().countPalindromicSubsequence(input) == output

    def test_3(self):
        input = "bbcbaba"
        output = 4
        assert Solution().countPalindromicSubsequence(input) == output
