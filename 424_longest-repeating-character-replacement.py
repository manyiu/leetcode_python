import unittest


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        freq = dict()
        longest = 0

        while r < len(s):
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1

            if r - l + 1 <= max(freq.values()) + k:
                longest = max(longest, r-l+1)
            else:
                freq[s[l]] -=1
                l += 1

            r += 1

        return longest
        


class TestSolution(unittest.TestCase):
    def test(self):
        s = "ABAB"
        k = 2
        self.assertEqual(Solution().characterReplacement(s, k), 4)
        s = "AABABBA"
        k = 1
        self.assertEqual(Solution().characterReplacement(s, k), 4)
        s = "ABBB"
        k = 2
        self.assertEqual(Solution().characterReplacement(s, k), 4)