from typing import List
import unittest


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        prefix = [0] * n

        for i in range(1, n):
            if nums[i - 1] % 2 == nums[i] % 2:
                prefix[i] = prefix[i - 1] + 1
            else:
                prefix[i] = prefix[i - 1]

        res = []

        for query in queries:
            start, end = query
            if prefix[start] == prefix[end]:
                res.append(True)
            else:
                res.append(False)

        return res

    # def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
    #     res = []

    #     for query in queries:
    #         a, b = query
    #         curr = True
    #         for i in range(a, b):
    #             if nums[i] % 2 == nums[i + 1] % 2:
    #                 curr = False
    #                 break
    #         res.append(curr)

    #     return res


class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [3, 4, 1, 2, 6]
        queries = [[0, 4]]
        assert Solution().isArraySpecial(nums, queries) == [False]

    def test_1(self):
        nums = [4, 3, 1, 6]
        queries = [[0, 2], [2, 3]]
        assert Solution().isArraySpecial(nums, queries) == [False, True]
