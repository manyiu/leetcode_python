from collections import deque
from typing import List
import unittest


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        if n == 0:
            return res

        l, r = 0, 0
        lower, upper = nums[0] - 2, nums[0] + 2

        for r in range(n):
            if lower <= nums[r] <= upper:
                lower = max(lower, nums[r] - 2)
                upper = min(upper, nums[r] + 2)
            else:
                l = r
                lower, upper = nums[r] - 2, nums[r] + 2
                while l >= 0 and nums[r] - 2 <= nums[l] <= nums[r] + 2:
                    lower = max(lower, nums[l] - 2)
                    upper = min(upper, nums[l] + 2)
                    l -= 1
                l += 1
            res += r - l + 1

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        input = [5, 4, 2, 4]
        output = 8
        self.assertEqual(Solution().continuousSubarrays(input), output)

    def test_2(self):
        input = [1, 2, 3]
        output = 6
        self.assertEqual(Solution().continuousSubarrays(input), output)
