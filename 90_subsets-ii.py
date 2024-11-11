from typing import List
import unittest


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        def backtrack(currSubset: List[int], i: int):
            if i == len(nums):
                res.append(currSubset.copy())
                return

            currSubset.append(nums[i])
            backtrack(currSubset, i + 1)
            currSubset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            backtrack(currSubset, i + 1)

        backtrack([], 0)

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1, 2, 2]
        res = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
        self.assertEqual(Solution().subsetsWithDup(nums), res)

    def test_2(self):
        nums = [0]
        res = [[], [0]]
        self.assertEqual(Solution().subsetsWithDup(nums), res)
