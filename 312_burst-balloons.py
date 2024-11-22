from typing import List
import unittest


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}

        def dfs(l: int, r: int) -> int:
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]

            res = 0

            for i in range(l, r + 1):
                currCoins = nums[l - 1] * nums[i] * nums[r + 1]
                leftCoins = dfs(l, i - 1)
                rightCoins = dfs(i + 1, r)
                allCoins = currCoins + leftCoins + rightCoins

                res = max(res, allCoins)

            dp[(l, r)] = res

            return res

        return dfs(1, len(nums) - 2)

    # def maxCoins(self, nums: List[int]) -> int:
    #     nums = [1] + nums + [1]

    #     def dfs(nums: List[int]) -> int:
    #         if len(nums) == 2:
    #             return 0

    #         res = 0

    #         for i in range(1, len(nums) - 1):
    #             currCoins = nums[i - 1] * nums[i] * nums[i + 1]
    #             nextCoins = dfs(nums[:i] + nums[i + 1 :])
    #             res = max(res, currCoins + nextCoins)

    #         return res

    #     return dfs(nums)


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [3, 1, 5, 8]
        assert Solution().maxCoins(nums) == 167

    def test_2(self):
        nums = [1, 5]
        assert Solution().maxCoins(nums) == 10
