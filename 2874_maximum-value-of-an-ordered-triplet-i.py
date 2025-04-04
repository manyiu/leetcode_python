from typing import List
import unittest


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        i_max = 0
        diff_max = 0
        res = 0

        for k in range(len(nums)):
            res = max(res, diff_max * nums[k])
            i_max = max(i_max, nums[k])
            diff_max = max(diff_max, i_max - nums[k])

        return res

    # def maximumTripletValue(self, nums: List[int]) -> int:
    #     prefix_max = [0] * len(nums)
    #     suffix_max = [0] * len(nums)

    #     prefix_max[0] = nums[0]
    #     suffix_max[-1] = nums[-1]

    #     for i in range(1, len(nums)):
    #         prefix_max[i] = max(prefix_max[i - 1], nums[i])
    #         suffix_max[-(i + 1)] = max(suffix_max[-i], nums[-(i + 1)])

    #     res = 0

    #     for i in range(1, len(nums) - 1):
    #         res = max(res, (prefix_max[i - 1] - nums[i]) * (suffix_max[i + 1]))

    #     return res or 0


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        nums = [12, 6, 1, 2, 7]
        expected = 77
        self.assertEqual(Solution().maximumTripletValue(nums), expected)

    def test_example_2(self):
        nums = [1, 10, 3, 4, 19]
        expected = 133
        self.assertEqual(Solution().maximumTripletValue(nums), expected)

    def test_example_3(self):
        nums = [1, 2, 3]
        expected = 0
        self.assertEqual(Solution().maximumTripletValue(nums), expected)
