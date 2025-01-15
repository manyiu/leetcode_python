import unittest


class Solution:
    def bit_count(self, num: int) -> int:
        count = 0

        while num > 0:
            count += num & 1
            num >>= 1

        return count

    def minimizeXor(self, num1: int, num2: int) -> int:
        num1_bit_count = self.bit_count(num1)
        num2_bit_count = self.bit_count(num2)

        diff = num1_bit_count - num2_bit_count

        if diff == 0:
            return num1

        res = 0
        digit = 0

        if diff < 0:
            temp = num1

            while diff < 0:
                if temp & 1 == 0:
                    res += 2**digit
                    diff += 1
                temp >>= 1
                digit += 1

            res = num1 | res
        else:
            temp = num1

            while diff > 0:
                if temp & 1 == 1:
                    res += 2**digit
                    diff -= 1
                temp >>= 1
                digit += 1

            res = num1 ^ res

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        num1 = 3
        num2 = 5
        output = 3
        self.assertEqual(Solution().minimizeXor(num1, num2), output)

    def test_2(self):
        num1 = 1
        num2 = 12
        output = 3
        self.assertEqual(Solution().minimizeXor(num1, num2), output)

    def test_3(self):
        num1 = 25
        num2 = 72
        output = 24
        self.assertEqual(Solution().minimizeXor(num1, num2), output)
