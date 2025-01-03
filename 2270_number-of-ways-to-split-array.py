from typing import List
import unittest


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * n

        for i in range(n):
            if i == 0:
                prefix_sum[0] = nums[0]
            else:
                prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        res = 0

        for i in range(n - 1):
            if prefix_sum[i] >= prefix_sum[n - 1] - prefix_sum[i]:
                res += 1

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        input = [10, 4, -8, 7]
        output = 2
        assert Solution().waysToSplitArray(input) == output

    def test_2(self):
        input = [2, 3, 1, 0]
        output = 2
        assert Solution().waysToSplitArray(input) == output
