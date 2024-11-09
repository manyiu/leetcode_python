from typing import List
import unittest


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(comb: List[int], i: int, target: int):
            if target == 0:
                res.append(comb.copy())
                return

            if target < 0 or i >= len(candidates):
                return

            comb.append(candidates[i])
            dfs(comb, i, target - candidates[i])
            comb.pop()
            dfs(comb, i + 1, target)

        dfs([], 0, target)

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        candidates = [2, 3, 6, 7]
        target = 7
        res = [[2, 2, 3], [7]]
        self.assertEqual(Solution().combinationSum(candidates, target), res)

    def test_2(self):
        candidates = [2, 3, 5]
        target = 8
        res = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        self.assertEqual(Solution().combinationSum(candidates, target), res)
