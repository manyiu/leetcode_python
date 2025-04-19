from typing import List
import unittest


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def count_pairs(nums: List[int], target: int) -> int:
            res = 0

            left, right = 0, len(nums) - 1

            while left < right:
                if nums[left] + nums[right] > target:
                    right -= 1
                else:
                    res += right - left
                    left += 1

            return res

        nums.sort()

        return count_pairs(nums, upper) - count_pairs(nums, lower - 1)

    # def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
    #     nums.sort()
    #     n = len(nums)
    #     res = 0

    #     for i in range(n):
    #         min_left = i + 1
    #         min_right = n - 1

    #         while min_left <= min_right:
    #             m = min_left + (min_right - min_left) // 2

    #             if nums[i] + nums[m] < lower:
    #                 min_left = m + 1
    #             else:
    #                 min_right = m - 1

    #         max_left = i + 1
    #         max_right = n - 1

    #         while max_left <= max_right:
    #             m = max_left + (max_right - max_left) // 2

    #             if nums[i] + nums[m] > upper:
    #                 max_right = m - 1
    #             else:
    #                 max_left = m + 1

    #         res += max_right - min_left + 1
    #     return res

    # def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
    #     res = 0

    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if lower <= nums[i] + nums[j] <= upper:
    #                 res += 1

    #     return res


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        nums = [0, 1, 7, 4, 4, 5]
        lower = 3
        upper = 6
        expected = 6
        self.assertEqual(Solution().countFairPairs(nums, lower, upper), expected)

    def test_example_2(self):
        nums = [1, 7, 9, 2, 5]
        lower = 11
        upper = 11
        expected = 1
        self.assertEqual(Solution().countFairPairs(nums, lower, upper), expected)
