from typing import List
import unittest


class Solution:
    def binarySearch(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums)

        while l <= r:
            m = (l + r) // 2

            if nums[m] >= val:
                r = m - 1
            else:
                l = m + 1

        return l

    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []

        for num in nums:
            if len(sub) == 0 or num > sub[-1]:
                sub.append(num)
            else:
                idx = self.binarySearch(sub, num)
                sub[idx] = num

        return len(sub)

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     dp = [1] * len(nums)

    #     for i in range(len(nums)):
    #         for j in range(i):
    #             if nums[j] < nums[i]:
    #                 dp[i] = max(dp[i], dp[j] + 1)

    #     return max(dp)


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        assert Solution().lengthOfLIS(nums) == 4

    def test_2(self):
        nums = [0, 1, 0, 3, 2, 3]
        assert Solution().lengthOfLIS(nums) == 4

    def test_3(self):
        nums = [7, 7, 7, 7, 7, 7, 7]
        assert Solution().lengthOfLIS(nums) == 1
