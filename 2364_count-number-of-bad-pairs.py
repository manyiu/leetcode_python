from collections import defaultdict
from typing import List
import unittest


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        total_pairs = 0
        count = defaultdict(int)

        for i in range(len(nums)):
            total_pairs += i
            good_pairs += count[nums[i] - i]
            count[nums[i] - i] += 1

        return total_pairs - good_pairs


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [4, 1, 3, 3]
        output = 5
        self.assertEqual(Solution().countBadPairs(nums), output)

    def test_2(self):
        nums = [1, 2, 3, 4, 5]
        output = 0
        self.assertEqual(Solution().countBadPairs(nums), output)
