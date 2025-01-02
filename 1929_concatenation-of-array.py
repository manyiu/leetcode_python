from typing import List
import unittest


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [0] * (len(nums) * 2)

        for i, num in enumerate(nums):
            res[i], res[len(nums) + i] = num, num

        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        nums = [1, 2, 1]
        self.assertEqual(Solution().getConcatenation(nums), [1, 2, 1, 1, 2, 1])

    def test2(self):
        nums = [1, 3, 2, 1]
        self.assertEqual(Solution().getConcatenation(nums), [1, 3, 2, 1, 1, 3, 2, 1])

    def test3(self):
        nums = [1]
        self.assertEqual(Solution().getConcatenation(nums), [1, 1])
