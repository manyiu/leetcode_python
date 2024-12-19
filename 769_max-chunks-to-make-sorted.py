from typing import List
import unittest


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 0
        currMax = float("-infinity")

        for i in range(len(arr)):
            currMax = max(currMax, arr[i])

            if i == currMax:
                res += 1

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        arr = [4, 3, 2, 1, 0]
        self.assertEqual(Solution().maxChunksToSorted(arr), 1)

    def test_2(self):
        arr = [1, 0, 2, 3, 4]
        self.assertEqual(Solution().maxChunksToSorted(arr), 4)
