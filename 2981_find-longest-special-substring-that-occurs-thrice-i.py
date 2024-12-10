import unittest


class Solution:
    def maximumLength(self, s: str) -> int:
        res = -1
        count = {}

        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i] != s[j]:
                    break

                if s[i : j + 1] not in count:
                    count[s[i : j + 1]] = 1
                else:
                    count[s[i : j + 1]] += 1

                if count[s[i : j + 1]] >= 3 and len(s[i : j + 1]) > res:
                    res = len(s[i : j + 1])

        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        s = "aaaa"
        self.assertEqual(Solution().maximumLength(s), 2)

    def test2(self):
        s = "abcdef"
        self.assertEqual(Solution().maximumLength(s), -1)

    def test3(self):
        s = "abcaba"
        self.assertEqual(Solution().maximumLength(s), 1)
