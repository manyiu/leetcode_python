import unittest


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [""] * numRows
        pos = 0
        step = 1

        for ch in s:
            res[pos] += ch

            if step + pos < 0 or step + pos > numRows - 1:
                step *= -1

            pos += step

        return "".join(res)


class TestSolution(unittest.TestCase):
    def test_1(self):
        input = "PAYPALISHIRING"
        numRows = 3
        output = "PAHNAPLSIIGYIR"
        self.assertEqual(Solution().convert(input, numRows), output)

    def test_2(self):
        input = "PAYPALISHIRING"
        numRows = 4
        output = "PINALSIGYAHRPI"
        self.assertEqual(Solution().convert(input, numRows), output)

    def test_3(self):
        input = "A"
        numRows = 1
        output = "A"
        self.assertEqual(Solution().convert(input, numRows), output)

    def test_4(self):
        input = "AB"
        numRows = 1
        output = "AB"
        self.assertEqual(Solution().convert(input, numRows), output)

    def test_5(self):
        input = "ABC"
        numRows = 1
        output = "ABC"
        self.assertEqual(Solution().convert(input, numRows), output)

    def test_6(self):
        input = "ABC"
        numRows = 2
        output = "ACB"
        self.assertEqual(Solution().convert(input, numRows), output)

    def test_7(self):
        input = "ABC"
        numRows = 3
        output = "ABC"
        self.assertEqual(Solution().convert(input, numRows), output)

    def test_8(self):
        input = "ABC"
        numRows = 4
        output = "ABC"
        self.assertEqual(Solution().convert(input, numRows), output)

    def test_9(self):
        input = "ABC"
        numRows = 5
        output = "ABC"
        self.assertEqual(Solution().convert(input, numRows), output)

    def test_10(self):
        input = "ABC"
        numRows = 6
        output = "ABC"
        self.assertEqual(Solution().convert(input, numRows), output)

    def test_11(self):
        input = "ABC"
        numRows = 7
        output = "ABC"
        self.assertEqual(Solution().convert(input, numRows), output)

    def test_12(self):
        input = "ABC"
        numRows = 8
        output = "ABC"
        self.assertEqual(Solution().convert(input, numRows), output)
