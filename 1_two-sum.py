from typing import List
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        match_hash = dict()

        for i, num in enumerate(nums):
            if target - num in match_hash:
                return [match_hash[target-num], i]
            match_hash[num] = i

        return []



class TestSolution(unittest.TestCase):
    def test(self):
        nums = [2,7,11,15]
        target = 9
        self.assertEqual(Solution().twoSum(nums, target), [0, 1])
        nums = [3,2,4]
        target = 6
        self.assertEqual(Solution().twoSum(nums, target), [1, 2])
        nums = [3,3]
        target = 6
        self.assertEqual(Solution().twoSum(nums, target), [0, 1])