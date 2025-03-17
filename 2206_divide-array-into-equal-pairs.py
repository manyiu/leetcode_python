from collections import defaultdict
from typing import List
import unittest


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = defaultdict(int)

        for num in nums:
            if count[num] == 0:
                count[num] = 1
            else:
                count.pop(num)

        return len(count) == 0


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [3, 2, 3, 2, 2, 2]
        output = True
        self.assertEqual(Solution().divideArray(nums), output)

    def test_2(self):
        nums = [1, 2, 3, 4]
        output = False
        self.assertEqual(Solution().divideArray(nums), output)
