from collections import defaultdict
import unittest


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l, r = 0, 0
        count = defaultdict(int)
        res = 0

        for r in range(len(s)):
            count[s[r]] += 1

            while len(count) == 3:
                res += len(s) - r

                count[s[l]] -= 1

                if count[s[l]] == 0:
                    count.pop(s[l])

                l += 1

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "abcabc"
        output = 10
        self.assertEqual(Solution().numberOfSubstrings(s), output)

    def test_2(self):
        s = "aaacb"
        output = 3
        self.assertEqual(Solution().numberOfSubstrings(s), output)

    def test_3(self):
        s = "abc"
        output = 1
        self.assertEqual(Solution().numberOfSubstrings(s), output)
