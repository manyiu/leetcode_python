from typing import List
import unittest


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.insert(0, [0, 0, 0])

        def can_reduce_to_zero(k: int) -> bool:
            pref = [0] * len(nums)

            for l, r, val in queries[: k + 1]:
                pref[l] += val
                if r + 1 < len(nums):
                    pref[r + 1] -= val

            for i in range(len(nums)):
                if i > 0:
                    pref[i] += pref[i - 1]

                if nums[i] > pref[i]:
                    return False

            return True

        l, r = 0, len(queries) - 1

        while l <= r:
            m = l + (r - l) // 2

            if can_reduce_to_zero(m):
                r = m - 1
            else:
                l = m + 1

        return l if l < len(queries) else -1

    # def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
    #     remain_values = dict()

    #     for i in range(len(nums)):
    #         if nums[i] != 0:
    #             remain_values[i] = nums[i]

    #     res = 0

    #     for l, r, val in queries:
    #         if len(remain_values) == 0:
    #             return res

    #         for i in range(l, r + 1):
    #             if i in remain_values:
    #                 remain_values[i] -= val
    #                 if remain_values[i] <= 0:
    #                     remain_values.pop(i)

    #         res += 1

    #     if len(remain_values) == 0:
    #         return res

    #     return -1


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [2, 0, 2]
        queries = [[0, 2, 1], [0, 2, 1], [1, 1, 3]]
        output = 2
        self.assertEqual(Solution().minZeroArray(nums, queries), output)

    def test_2(self):
        nums = [4, 3, 2, 1]
        queries = [[1, 3, 2], [0, 2, 1]]
        output = -1
        self.assertEqual(Solution().minZeroArray(nums, queries), output)

    def test_3(self):
        nums = [0]
        queries = [[0, 0, 2], [0, 0, 4], [0, 0, 4], [0, 0, 3], [0, 0, 5]]
        output = 0
        self.assertEqual(Solution().minZeroArray(nums, queries), output)
