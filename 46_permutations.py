from typing import List
import unittest


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for num in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    perm_copy = perm.copy()
                    perm_copy.insert(i, num)
                    new_perms.append(perm_copy)
            perms = new_perms

        return perms

    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     if len(nums) == 0:
    #         return [[]]

    #     perms = self.permute(nums[1:])

    #     res = []

    #     for perm in perms:
    #         for i in range(len(perm) + 1):
    #             perm_copy = perm.copy()
    #             perm_copy.insert(i, nums[0])
    #             res.append(perm_copy)

    #     return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1, 2, 3]
        res = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(Solution().permute(nums), res)

    def test_2(self):
        nums = [0, 1]
        res = [[0, 1], [1, 0]]
        self.assertEqual(Solution().permute(nums), res)

    def test_3(self):
        nums = [1]
        res = [[1]]
        self.assertEqual(Solution().permute(nums), res)
