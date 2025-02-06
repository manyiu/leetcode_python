from collections import defaultdict
from typing import List
import unittest


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int)
        pair_count = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]

                pair_count[product] += product_count[product]
                product_count[product] += 1

        res = 0

        for count in pair_count.values():
            res += count * 8

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [2, 3, 4, 6]
        output = 8
        self.assertEqual(Solution().tupleSameProduct(nums), output)

    def test_2(self):
        nums = [1, 2, 4, 5, 10]
        output = 16
        self.assertEqual(Solution().tupleSameProduct(nums), output)

    def test_3(self):
        nums = [2, 3, 4, 6, 8, 12]
        output = 40
        self.assertEqual(Solution().tupleSameProduct(nums), output)
