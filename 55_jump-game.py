from typing import List
import unittest


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0

    # def canJump(self, nums: List[int]) -> bool:
    #     cache = {}

    #     def dfs(i: int) -> bool:
    #         if i == len(nums) - 1:
    #             return True
    #         if i >= len(nums) or nums[i] == 0:
    #             cache[i] = False
    #             return False

    #         for j in range(1, nums[i] + 1):
    #             if dfs(i + j):
    #                 return True

    #         cache[i] = False
    #         return False

    #     return dfs(0)


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [2, 3, 1, 1, 4]
        assert Solution().canJump(nums) == True

    def test_2(self):
        nums = [3, 2, 1, 0, 4]
        assert Solution().canJump(nums) == False
