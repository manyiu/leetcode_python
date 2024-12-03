from typing import List
import unittest


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res ^= i ^ nums[i]

        return res

    # def missingNumber(self, nums: List[int]) -> int:
    #     n = len(nums)

    #     res = (n * (n + 1)) // 2

    #     for num in nums:
    #         res -= num

    #     return res


class TestSolution(unittest.TestCase):
    def test_0(self):
        solution = Solution()
        self.assertEqual(solution.missingNumber([3, 0, 1]), 2)

    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)

    def test_2(self):
        solution = Solution()
        self.assertEqual(solution.missingNumber([0]), 1)

    def test_3(self):
        solution = Solution()
        self.assertEqual(solution.missingNumber([1]), 0)

    def test_4(self):
        solution = Solution()
        self.assertEqual(solution.missingNumber([0, 1]), 2)

    def test_5(self):
        solution = Solution()
        self.assertEqual(solution.missingNumber([1, 2]), 0)

    def test_6(self):
        solution = Solution()
        self.assertEqual(solution.missingNumber([0, 1, 2, 3, 4, 5, 6, 7, 9]), 8)

    def test_7(self):
        solution = Solution()
        self.assertEqual(solution.missingNumber([0, 1, 2, 3, 4, 5, 6, 7, 8]), 9)

    def test_8(self):
        solution = Solution()
        self.assertEqual(solution.missingNumber([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 10)

    def test_9(self):
        solution = Solution()
        self.assertEqual(solution.missingNumber([0, 1, 2, 3, 4, 5, 6, 7, 8, 10]), 9)

    def test_10(self):
        solution = Solution()
        self.assertEqual(solution.missingNumber([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 11)
