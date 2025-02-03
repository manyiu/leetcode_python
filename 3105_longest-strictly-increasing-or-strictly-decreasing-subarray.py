from typing import List
import unittest


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc_count, des_count, max_count = 1, 1, 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc_count += 1
            else:
                inc_count = 1

            if nums[i] < nums[i - 1]:
                des_count += 1
            else:
                des_count = 1

            max_count = max(max_count, inc_count, des_count)

        return max_count


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1, 4, 3, 3, 2]
        output = 2
        self.assertEqual(Solution().longestMonotonicSubarray(nums), output)

    def test_2(self):
        nums = [3, 3, 3, 3]
        output = 1
        self.assertEqual(Solution().longestMonotonicSubarray(nums), output)

    def test_3(self):
        nums = [3, 2, 1]
        output = 3
        self.assertEqual(Solution().longestMonotonicSubarray(nums), output)
