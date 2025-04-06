from typing import List
import unittest


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        dp = [[num] for num in nums]
        res = []

        for i in reversed(range(len(nums))):
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    tmp = [nums[i]] + dp[j]
                    if len(tmp) > len(dp[i]):
                        dp[i] = tmp
            if len(dp[i]) > len(res):
                res = dp[i]

        return res

    # def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    #     nums.sort()

    #     cache = {}

    #     def dfs(idx: int) -> List[int]:
    #         if idx >= len(nums):
    #             return []

    #         if idx in cache:
    #             return cache[idx]

    #         res = [nums[idx]]

    #         for i in range(idx + 1, len(nums)):
    #             if nums[i] % nums[idx] == 0:
    #                 temp = [nums[idx]] + dfs(i)
    #                 if len(temp) > len(res):
    #                     res = temp

    #         cache[idx] = res

    #         return res

    #     res = []

    #     for i in range(len(nums)):
    #         curr = dfs(i)
    #         if len(curr) > len(res):
    #             res = curr

    #     return res

    # def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    #     nums.sort()
    #     cache = {}

    #     def dfs(idx: int, prev: int) -> List[int]:
    #         if idx >= len(nums):
    #             return []

    #         if (idx, prev) in cache:
    #             return cache[(idx, prev)]

    #         skip = dfs(idx + 1, prev)

    #         if nums[idx] % prev == 0:
    #             take = [nums[idx]] + dfs(idx + 1, nums[idx])
    #             return take if len(take) > len(skip) else skip

    #         cache[(idx, prev)] = skip

    #         return skip

    #     return dfs(0, 1)


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        nums = [1, 2, 3]
        expected = [1, 2]
        self.assertEqual(Solution().largestDivisibleSubset(nums), expected)

    def test_example_2(self):
        nums = [1, 2, 4, 8]
        expected = [1, 2, 4, 8]
        self.assertEqual(Solution().largestDivisibleSubset(nums), expected)

    def test_testcase_21(self):
        nums = [4, 8, 10, 240]
        expected = [4, 8, 240]
        self.assertEqual(Solution().largestDivisibleSubset(nums), expected)
