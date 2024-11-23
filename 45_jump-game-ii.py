from typing import List
import unittest


class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0

        while r < len(nums) - 1:
            farest = r
            for i in range(l, r + 1):
                farest = max(farest, i + nums[i])
            l = r + 1
            r = farest
            res += 1

        return res

    # def jump(self, nums: List[int]) -> int:
    #     curr = len(nums) - 1
    #     count = 0

    #     while curr > 0:
    #         farest = curr
    #         for i in range(curr - 1, -1, -1):
    #             if i + nums[i] >= curr:
    #                 farest = i
    #         curr = farest
    #         count += 1

    #     return count


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [2, 3, 1, 1, 4]
        assert Solution().jump(nums) == 2

    def test_2(self):
        nums = [2, 3, 0, 1, 4]
        assert Solution().jump(nums) == 2
