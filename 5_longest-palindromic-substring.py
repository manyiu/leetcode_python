import unittest


class Solution:
    def helper(self, s: str, l: int, r: int) -> tuple[int, int, int]:
        length = -1
        left = -1
        right = -1

        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                break

            length = r - l + 1
            left = l
            right = r
            l -= 1
            r += 1

        return (length, left, right)

    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        l = -1
        r = -1

        for i in range(len(s)):
            oddLen, oddL, oddR = self.helper(s, i, i)
            evenLen, evenL, evenR = self.helper(s, i, i + 1)

            if oddLen > maxLen:
                maxLen = oddLen
                l = oddL
                r = oddR

            if evenLen > maxLen:
                maxLen = evenLen
                l = evenL
                r = evenR

        return s[l : r + 1]


class TestSolution(unittest.TestCase):
    def test_1(self):
        assert (
            Solution().longestPalindrome("babad") == "bab"
            or Solution().longestPalindrome("babad") == "aba"
        )

    def test_2(self):
        assert Solution().longestPalindrome("cbbd") == "bb"

    def test_3(self):
        assert Solution().longestPalindrome("a") == "a"

    def test_4(self):
        assert Solution().longestPalindrome("ac") == "a"

    def test_5(self):
        assert Solution().longestPalindrome("bb") == "bb"

    def test_6(self):
        assert Solution().longestPalindrome("ccc") == "ccc"

    def test_7(self):
        assert Solution().longestPalindrome("aaaa") == "aaaa"

    def test_8(self):
        assert Solution().longestPalindrome("abacdfgdcaba") == "aba"

    def test_9(self):
        assert Solution().longestPalindrome("abacdfgdcabba") == "abba"

    def test_10(self):
        assert Solution().longestPalindrome("abacdfgdcabba") == "abba"

    def test_11(self):
        assert Solution().longestPalindrome("abacdfgdcabba") == "abba"

    def test_12(self):
        assert Solution().longestPalindrome("abacdfgdcabba") == "abba"
