from typing import List
import unittest


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return True if sum(derived) % 2 == 0 else False

    # def doesValidArrayExist(self, derived: List[int]) -> bool:
    #     temp = 0

    #     for i in range(len(derived)):
    #         temp ^= derived[i]

    #     return True if temp == 0 else False


class TestSolution(unittest.TestCase):
    def test_1(self):
        derived = [1, 1, 0]
        output = True
        self.assertEqual(Solution().doesValidArrayExist(derived), output)

    def test_2(self):
        derived = [1, 1]
        output = True
        self.assertEqual(Solution().doesValidArrayExist(derived), output)

    def test_3(self):
        derived = [1, 0]
        output = False
        self.assertEqual(Solution().doesValidArrayExist(derived), output)
