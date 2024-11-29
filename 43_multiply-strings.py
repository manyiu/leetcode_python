import unittest


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                prod = int(num1[i1]) * int(num2[i2])

                res[i1 + i2] += prod
                res[i1 + i2 + 1] += (res[i1 + i2]) // 10
                res[i1 + i2] = res[i1 + i2] % 10

        res, beg = res[::-1], 0

        while beg < len(res) and res[beg] == 0:
            beg += 1

        res = map(str, res[beg:])

        return "".join(res)


class TestSolution(unittest.TestCase):
    def test_0(self):
        num1 = "2"
        num2 = "3"
        self.assertEqual(Solution().multiply(num1, num2), "6")

    def test_1(self):
        num1 = "123"
        num2 = "456"
        self.assertEqual(Solution().multiply(num1, num2), "56088")

    def test_2(self):
        num1 = "0"
        num2 = "0"
        self.assertEqual(Solution().multiply(num1, num2), "0")

    def test_3(self):
        num1 = "123456789"
        num2 = "987654321"
        self.assertEqual(Solution().multiply(num1, num2), "121932631112635269")
