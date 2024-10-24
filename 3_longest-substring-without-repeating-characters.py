import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        lastPos = dict()
        l, r = 0, 0
        
        while r < len(s):
            if s[r] in lastPos and lastPos[s[r]] >= l:
                l = lastPos[s[r]] + 1

            lastPos[s[r]] = r   

            maxLen = max(maxLen, r - l + 1)

            r += 1
            
        return maxLen

class TestSolution(unittest.TestCase):
    def test(self):
        s = "abcabcbb"
        self.assertEqual(Solution().lengthOfLongestSubstring(s), 3)
        s = "bbbbb"
        self.assertEqual(Solution().lengthOfLongestSubstring(s), 1)
        s = "pwwkew"
        self.assertEqual(Solution().lengthOfLongestSubstring(s), 3)
        s = ""
        self.assertEqual(Solution().lengthOfLongestSubstring(s), 0)
        s = " "
        self.assertEqual(Solution().lengthOfLongestSubstring(s), 1)
        s = "au"
        self.assertEqual(Solution().lengthOfLongestSubstring(s), 2)
        s = "aab"
        self.assertEqual(Solution().lengthOfLongestSubstring(s), 2)
        s = "dvdf"
        self.assertEqual(Solution().lengthOfLongestSubstring(s), 3)
        s = "tmmzuxt"
        self.assertEqual(Solution().lengthOfLongestSubstring(s), 5)
        s = "abba"
        self.assertEqual(Solution().lengthOfLongestSubstring(s), 2)
        s = "abcabcbb"
        self.assertEqual(Solution().lengthOfLongestSubstring(s), 3)
        s = "bbbbb"
        self.assertEqual(Solution().lengthOfLongestSubstring(s), 1)
        s = "pwwkew"
        self.assertEqual(Solution().lengthOfLongestSubstring(s), 3)
        s = ""
        self.assertEqual(Solution().lengthOfLongestSubstring(s), 0)
        s = " "
        self.assertEqual(Solution().lengthOfLongestSubstring(s), 1)
        s = "au"
        self.assertEqual(Solution().lengthOfLongestSubstring(s), 2)
        s = "aab"
        self.assertEqual(Solution().lengthOfLongestSubstring(s), 2)
        s = "dvdf"
        self.assertEqual(Solution().lengthOfLongestSubstring(s), 3)
        s = "tmmzuxt"
        self.assertEqual(Solution().lengthOfLongestSubstring(s), 5)
        s = "abba"
        self.assertEqual(Solution().lengthOfLongestSubstring(s), 2)
        s = "abcabcbb"
        self.assertEqual(Solution().lengthOfLongestSubstring(s), 3)
