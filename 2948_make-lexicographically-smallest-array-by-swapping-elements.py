from collections import deque
from typing import List
import unittest


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups = []
        num_to_group = {}

        for n in sorted(nums):
            if not groups or abs(n - groups[-1][-1]) > limit:
                groups.append(deque())
            groups[-1].append(n)
            num_to_group[n] = len(groups) - 1

        res = []

        for n in nums:
            j = num_to_group[n]
            res.append(groups[j].popleft())

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1, 5, 3, 9, 8]
        limit = 2
        output = [1, 3, 5, 8, 9]
        self.assertEqual(Solution().lexicographicallySmallestArray(nums, limit), output)

    def test_2(self):
        nums = [1, 7, 6, 18, 2, 1]
        limit = 3
        output = [1, 6, 7, 18, 1, 2]

    def test_3(self):
        nums = ([1, 7, 28, 19, 10],)
        limit = 3
        output = [1, 7, 28, 19, 10]
