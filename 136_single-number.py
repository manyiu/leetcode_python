from typing import List
import unittest


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            res ^= num

        return res

    # def singleNumber(self, nums: List[int]) -> int:
    #     numberSet = set()

    #     for num in nums:
    #         if num in numberSet:
    #             numberSet.remove(num)
    #         else:
    #             numberSet.add(num)

    #     return numberSet.pop()


class TestSolution(unittest.TestCase):
    def test_0(self):
        solution = Solution()
        self.assertEqual(solution.singleNumber([2, 2, 1]), 1)

    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.singleNumber([4, 1, 2, 1, 2]), 4)

    def test_2(self):
        solution = Solution()
        self.assertEqual(solution.singleNumber([1]), 1)
