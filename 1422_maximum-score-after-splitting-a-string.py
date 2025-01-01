import unittest


class Solution:
    def maxScore(self, s: str) -> int:
        presum_zero = [0] * len(s)
        postSum_one = [0] * len(s)

        for i in range(len(s)):
            if i > 0:
                presum_zero[i] = presum_zero[i - 1]
            else:
                presum_zero[i] = 0

            if s[i] == "0":
                presum_zero[i] += 1

        for i in range(len(s) - 1, -1, -1):
            if i < len(s) - 1:
                postSum_one[i] = postSum_one[i + 1]
            else:
                postSum_one[i] = 0

            if s[i] == "1":
                postSum_one[i] += 1

        res = 0

        for i in range(len(s) - 1):
            res = max(res, presum_zero[i] + postSum_one[i + 1])

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "011101"
        output = 5
        self.assertEqual(Solution().maxScore(s), output)

    def test_2(self):
        s = "00111"
        output = 5
        self.assertEqual(Solution().maxScore(s), output)

    def test_3(self):
        s = "1111"
        output = 3
        self.assertEqual(Solution().maxScore(s), output)

    def test_4(self):
        s = "00"
        output = 1
        self.assertEqual(Solution().maxScore(s), output)
