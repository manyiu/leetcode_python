import unittest


class Solution:
    def runLengthEncode(self, s: str) -> str:
        res = ""
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                res += str(count) + s[i - 1]
                count = 1

        res += str(count) + s[-1]

        return res

    def countAndSay(self, n: int) -> str:
        rle = "1"

        for _ in range(1, n):
            rle = self.runLengthEncode(rle)

        return rle


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        n = 4
        expected = "1211"
        self.assertEqual(Solution().countAndSay(n), expected)

    def test_example_2(self):
        n = 1
        expected = "1"
        self.assertEqual(Solution().countAndSay(n), expected)
