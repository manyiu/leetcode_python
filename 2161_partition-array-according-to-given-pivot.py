from typing import List
import unittest


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = [0] * len(nums)

        for i in range(len(nums)):
            j = len(nums) - 1 - i

            if nums[i] < pivot:
                res[left] = nums[i]
                left += 1

            if nums[j] > pivot:
                res[right] = nums[j]
                right -= 1

        while left <= right:
            res[left] = pivot
            left += 1

        return res

    # def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
    #     less = []
    #     equal = []
    #     greater = []

    #     for num in nums:
    #         if num < pivot:
    #             less.append(num)
    #         elif num == pivot:
    #             equal.append(num)
    #         else:
    #             greater.append(num)

    #     return less + equal + greater


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [9, 12, 5, 10, 14, 3, 10]
        pivot = 10
        output = [9, 5, 3, 10, 10, 12, 14]
        self.assertEqual(Solution().pivotArray(nums, pivot), output)

    def test_2(self):
        nums = [-3, 4, 3, 2]
        pivot = 2
        output = [-3, 2, 4, 3]
        self.assertEqual(Solution().pivotArray(nums, pivot), output)
