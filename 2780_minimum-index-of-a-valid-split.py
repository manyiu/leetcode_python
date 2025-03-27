from collections import defaultdict
from typing import Counter, List
import unittest


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        left = defaultdict(int)
        right = Counter(nums)

        for i in range(len(nums) - 1):
            left[nums[i]] += 1
            right[nums[i]] -= 1

            left_len = i + 1
            right_len = len(nums) - (i + 1)

            if (
                left[nums[i]] >= left_len // 2 + 1
                and right[nums[i]] >= right_len // 2 + 1
            ):
                return i

        return -1

    # def minimumIndex(self, nums: List[int]) -> int:
    #     curr_dominant = nums[0]
    #     curr_count = 1

    #     for i in range(1, len(nums)):
    #         if nums[i] == curr_dominant:
    #             curr_count += 1
    #         else:
    #             curr_count -= 1

    #         if curr_count < 0:
    #             curr_dominant = nums[i]
    #             curr_count = 1

    #     prefix_sum = [0] * len(nums)

    #     if nums[0] == curr_dominant:
    #         prefix_sum[0] = 1

    #     for i in range(1, len(nums)):
    #         if nums[i] == curr_dominant:
    #             prefix_sum[i] = prefix_sum[i - 1] + 1
    #         else:
    #             prefix_sum[i] = prefix_sum[i - 1]

    #     for i in range(len(nums) - 1):
    #         first_half = prefix_sum[i]
    #         second_half = prefix_sum[-1] - prefix_sum[i]

    #         first_len = i + 1
    #         second_len = len(nums) - (i + 1)

    #         if first_half >= first_len // 2 + 1 and second_half >= second_len // 2 + 1:
    #             return i

    #     return -1


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        nums = [1, 2, 2, 2]
        output = 2
        self.assertEqual(Solution().minimumIndex(nums), output)

    def test_example_2(self):
        nums = [2, 1, 3, 1, 1, 1, 7, 1, 2, 1]
        output = 4
        self.assertEqual(Solution().minimumIndex(nums), output)

    def test_example_3(self):
        nums = [3, 3, 3, 3, 7, 2, 2]
        output = -1
        self.assertEqual(Solution().minimumIndex(nums), output)
