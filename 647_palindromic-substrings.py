import unittest


class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                count += 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                count += 1
                l -= 1
                r += 1

        return count


class TestSolution(unittest.TestCase):
    def test_1(self):
        assert Solution().countSubstrings("abc") == 3

    def test_2(self):
        assert Solution().countSubstrings("aaa") == 6

    def test_3(self):
        assert Solution().countSubstrings("abccba") == 9

    def test_4(self):
        assert Solution().countSubstrings("a") == 1

    def test_5(self):
        assert Solution().countSubstrings("ac") == 2
