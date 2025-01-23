from typing import List
import unittest


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = 0
        count = 0

        for num in nums:
            if num == curr:
                count += 1
            else:
                count -= 1
            if count <= 0:
                curr = num
                count = 1

        return curr


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [3, 2, 3]
        output = 3
        self.assertEqual(Solution().majorityElement(nums), output)

    def test_2(self):
        nums = [2, 2, 1, 1, 1, 2, 2]
        output = 2
        self.assertEqual(Solution().majorityElement(nums), output)
