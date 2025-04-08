from typing import List
import unittest


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        visited = set()

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in visited:
                # return (i+1) // 3 + (1 if (i+1)%3 != 0 else 0)
                return i // 3 + 1
            visited.add(nums[i])
        
        return 0

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        nums = [1,2,3,4,2,3,3,5,7]
        expected = 2
        self.assertEqual(Solution().minimumOperations(nums), expected)

    def test_example_2(self):
        nums = [4,5,6,4,4]
        expected = 2
        self.assertEqual(Solution().minimumOperations(nums), expected)

    def test_example_3(self):
        nums = [6,7,8,9]
        expected = 0
        self.assertEqual(Solution().minimumOperations(nums), expected)