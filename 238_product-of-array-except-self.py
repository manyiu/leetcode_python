from typing import List
import unittest


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        result = [1] * n

        for i in range(1,n):
            left[i] = left[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        for i in range(n):
            result[i] = left[i] * right[i]

        return result


class TestSolution(unittest.TestCase):

    def test(self):
        nums = [1, 2, 3, 4]
        self.assertEqual(Solution().productExceptSelf(nums), [24, 12, 8, 6])
        nums = [-1, 1, 0, -3, 3]
        self.assertEqual(Solution().productExceptSelf(nums), [0, 0, 9, 0, 0])
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(Solution().productExceptSelf(nums), [120, 60, 40, 30, 24])
        nums = [1, 2, 3, 4, 5, 6]
        self.assertEqual(Solution().productExceptSelf(nums), [720, 360, 240, 180, 144, 120])
        nums = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(Solution().productExceptSelf(nums), [5040, 2520, 1680, 1260, 1008, 840, 720])
        nums = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(Solution().productExceptSelf(nums), [40320, 20160, 13440, 10080, 8064, 6720, 5760, 5040])
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(Solution().productExceptSelf(nums), [362880, 181440, 120960, 90720, 72576, 60480, 51840, 45360, 40320])
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(Solution().productExceptSelf(nums), [3628800, 1814400, 1209600, 907200, 725760, 604800, 518400, 453600, 403200, 362880])
        