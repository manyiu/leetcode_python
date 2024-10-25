import unittest

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = dict()

        for c in t:
            t_freq[c] = 1 + t_freq.get(c, 0)

        have, need = 0, len(t)
        l = 0
        shortest = float("infinity")
        start, end = 0, 0

        for r in range(len(s)):
            c = s[r]

            if c in t_freq:
                t_freq[c] -= 1
                if t_freq[c] >= 0:
                    have += 1
            
            while have == need:
                if r-l+1 < shortest:
                    start, end = l, r
                    shortest = r-l+1

                if s[l] in t_freq:
                    t_freq[s[l]] += 1
                    if t_freq[s[l]] >= 1:
                        have -= 1

                l += 1

        if shortest == float("infinity"):
            return ""

        return s[start: end+1]
        
class TestSolution(unittest.TestCase):
    def test(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        self.assertEqual(Solution().minWindow(s, t), "BANC")
        s = "a"
        t = "a"
        self.assertEqual(Solution().minWindow(s, t), "a")
        s = "a"
        t = "aa"
        self.assertEqual(Solution().minWindow(s, t), "")
        s = "a"
        t = "b"
        self.assertEqual(Solution().minWindow(s, t), "")
