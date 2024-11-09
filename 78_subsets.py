from typing import List
import unittest


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(currSet: List[int], i: int):
            if i >= len(nums):
                res.append(currSet.copy())
                return

            dfs(currSet, i + 1)
            currSet.append(nums[i])
            dfs(currSet, i + 1)
            currSet.pop()

        dfs([], 0)

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1, 2, 3]
        res = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        self.assertEqual(Solution().subsets(nums), res)

    def test_2(self):
        nums = [0]
        res = [[], [0]]
        self.assertEqual(Solution().subsets(nums), res)
