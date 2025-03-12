from typing import List
import unittest


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        N = len(nums)
        l, r = 0, N - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] < 0:
                l = m + 1
            else:
                r = m - 1

        last_neg_index = r

        l = last_neg_index + 1
        r = N - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] > 0:
                r = m - 1
            else:
                l = m + 1

        first_pos_index = l

        return max(last_neg_index + 1, N - first_pos_index)

    # def maximumCount(self, nums: List[int]) -> int:
    #     neg = 0
    #     pos = 0

    #     for num in nums:
    #         if num < 0:
    #             neg += 1
    #         elif num > 0:
    #             pos += 1

    #     return max(neg, pos)


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [-2, -1, -1, 1, 2, 3]
        output = 3
        self.assertEqual(Solution().maximumCount(nums), output)

    def test_2(self):
        nums = [-3, -2, -1, 0, 0, 1, 2]
        output = 3
        self.assertEqual(Solution().maximumCount(nums), output)

    def test_3(self):
        nums = [5, 20, 66, 1314]
        output = 4
        self.assertEqual(Solution().maximumCount(nums), output)

    def test_3(self):
        nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        output = 0
        self.assertEqual(Solution().maximumCount(nums), output)

    def test_4(self):
        nums = [-1]
        output = 1
        self.assertEqual(Solution().maximumCount(nums), output)
