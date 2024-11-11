from typing import List
import unittest


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def backtrack(currComb: List[int], i, target):
            if target == 0:
                res.append(currComb.copy())
                return
            if target < 0 or i >= len(candidates):
                return

            currComb.append(candidates[i])
            backtrack(currComb, i + 1, target - candidates[i])
            currComb.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            backtrack(currComb, i + 1, target)

        backtrack([], 0, target)

        return res


class TestSolution(unittest.TestCase):

    def test_solution(self):
        sol = Solution()

        self.assertListEqual(
            sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8),
            [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]],
        )
        self.assertListEqual(sol.combinationSum2([2, 5, 2, 1, 2], 5), [[1, 2, 2], [5]])
