import unittest


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b & mask:
            a, b = a ^ b, (a & b) << 1

        return a & mask if b > mask else a

    # def getSum(self, a: int, b: int) -> int:
    #     while b:
    #         a, b = a ^ b, (a & b) << 1

    #     return a


class TestSolution(unittest.TestCase):
    def test_0(self):
        solution = Solution()
        self.assertEqual(solution.getSum(1, 2), 3)

    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.getSum(2, 3), 5)

    def test_2(self):
        solution = Solution()
        self.assertEqual(solution.getSum(3, 4), 7)

    def test_3(self):
        solution = Solution()
        self.assertEqual(solution.getSum(4, 5), 9)

    def test_4(self):
        solution = Solution()
        self.assertEqual(solution.getSum(5, 6), 11)

    def test_5(self):
        solution = Solution()
        self.assertEqual(solution.getSum(6, 7), 13)

    def test_6(self):
        solution = Solution()
        self.assertEqual(solution.getSum(7, 8), 15)

    def test_7(self):
        solution = Solution()
        self.assertEqual(solution.getSum(8, 9), 17)

    def test_8(self):
        solution = Solution()
        self.assertEqual(solution.getSum(9, 10), 19)

    def test_9(self):
        solution = Solution()
        self.assertEqual(solution.getSum(10, 11), 21)

    def test_10(self):
        solution = Solution()
        self.assertEqual(solution.getSum(11, 12), 23)

    def test_11(self):
        solution = Solution()
        self.assertEqual(solution.getSum(12, 13), 25)

    def test_12(self):
        solution = Solution()
        self.assertEqual(solution.getSum(13, 14), 27)

    def test_13(self):
        solution = Solution()
        self.assertEqual(solution.getSum(14, 15), 29)

    def test_14(self):
        solution = Solution()
        self.assertEqual(solution.getSum(15, 16), 31)

    def test_15(self):
        solution = Solution()
        self.assertEqual(solution.getSum(16, 17), 33)

    def test_16(self):
        solution = Solution()
        self.assertEqual(solution.getSum(17, 18), 35)

    def test_17(self):
        solution = Solution()
        self.assertEqual(solution.getSum(18, 19), 37)
