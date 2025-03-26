from typing import List
import unittest


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []

        reminder = grid[0][0] % x

        for row in grid:
            for num in row:
                if num % x != reminder:
                    return -1
                nums.append(num)

        nums.sort()

        median = nums[len(nums) // 2]

        res = 0

        for num in nums:
            res += abs(num - median) // x

        return res


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        grid = [[2, 4], [6, 8]]
        x = 2
        output = 4
        self.assertEqual(Solution().minOperations(grid, x), output)

    def test_example_2(self):
        grid = [[1, 5], [2, 3]]
        x = 1
        output = 5
        self.assertEqual(Solution().minOperations(grid, x), output)

    def test_example_3(self):
        grid = [[1, 2], [3, 4]]
        x = 2
        output = -1
        self.assertEqual(Solution().minOperations(grid, x), output)
