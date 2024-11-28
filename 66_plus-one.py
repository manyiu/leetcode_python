from typing import List
import unittest


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            sum = carry + digits[i]

            carry = sum // 10
            digits[i] = sum % 10

        if carry > 0:
            digits.insert(0, carry)

        return digits


class TestSolution(unittest.TestCase):
    def test_0(self):
        digits = [1, 2, 3]
        self.assertEqual(Solution().plusOne(digits), [1, 2, 4])

    def test_1(self):
        digits = [4, 3, 2, 1]
        self.assertEqual(Solution().plusOne(digits), [4, 3, 2, 2])

    def test_2(self):
        digits = [0]
        self.assertEqual(Solution().plusOne(digits), [1])

    def test_3(self):
        digits = [9]
        self.assertEqual(Solution().plusOne(digits), [1, 0])
