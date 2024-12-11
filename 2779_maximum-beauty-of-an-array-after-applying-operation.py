from typing import List
import unittest


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()

        res = 0
        l = 0

        for r in range(len(nums)):
            while nums[r] - nums[l] > 2 * k:
                l += 1
            res = max(res, r - l + 1)

        return res

    # def maximumBeauty(self, nums: List[int], k: int) -> int:
    #     l, r = min(nums), max(nums)
    #     res = 0

    #     for i in range(l, r + 1):
    #         count = 0
    #         for num in nums:
    #             if i - k <= num <= i + k:
    #                 count += 1
    #         res = max(res, count)

    #     return res


class TestSolution(unittest.TestCase):
    def test1(self):
        nums = [4, 6, 1, 2]
        k = 2
        self.assertEqual(Solution().maximumBeauty(nums, k), 3)

    def test2(self):
        nums = [1, 1, 1, 1]
        k = 10
        self.assertEqual(Solution().maximumBeauty(nums, k), 4)
