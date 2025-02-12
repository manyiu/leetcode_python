from collections import defaultdict
from typing import List
import unittest


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        hash = {}
        res = -1

        for num in nums:
            currDigitSum = self.digitSum(num)

            if currDigitSum in hash:
                res = max(res, num + hash[currDigitSum])
                hash[currDigitSum] = max(hash[currDigitSum], num)
            else:
                hash[currDigitSum] = num

        return res

    # def maximumSum(self, nums: List[int]) -> int:
    #     digitSumToValue = defaultdict(list)

    #     for num in nums:
    #         digitSumToValue[self.digitSum(num)].append(num)

    #     res = -1

    #     for group in digitSumToValue.values():
    #         if len(group) > 1:
    #             a, b = sorted(group)[-2:]
    #             res = max(res, a + b)

    #     return res

    # def maximumSum(self, nums: List[int]) -> int:
    #     res = -1

    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if self.digitSum(nums[i]) == self.digitSum(nums[j]):
    #                 res = max(res, nums[i] + nums[j])

    #     return res

    def digitSum(self, num: int) -> int:
        res = 0

        while num > 0:
            res += num % 10
            num //= 10

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [18, 43, 36, 13, 7]
        output = 54
        self.assertEqual(Solution().maximumSum(nums), output)

    def test_2(self):
        nums = [10, 12, 19, 14]
        output = -1
        self.assertEqual(Solution().maximumSum(nums), output)
