from typing import List
import unittest


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        temp = []

        for num in nums:
            temp.append(num)

        for i in range(n):
            nums[(i + k) % n] = temp[i]


class TestSolution(unittest.TestCase):
    def test(self):
        input = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        output = [5, 6, 7, 1, 2, 3, 4]
        Solution().rotate(input, k)
        self.assertEqual(input, output)
        input = [-1, -100, 3, 99]
        k = 2
        output = [3, 99, -1, -100]
        Solution().rotate(input, k)
        self.assertEqual(input, output)
        input = [1, 2, 3, 4, 5, 6]
        k = 1
        output = [6, 1, 2, 3, 4, 5]
        Solution().rotate(input, k)
        self.assertEqual(input, output)
        input = [1, 2, 3, 4, 5, 6]
        k = 2
        output = [5, 6, 1, 2, 3, 4]
        Solution().rotate(input, k)
        self.assertEqual(input, output)
        input = [1, 2, 3, 4, 5, 6]
        k = 3
        output = [4, 5, 6, 1, 2, 3]
        Solution().rotate(input, k)
        self.assertEqual(input, output)
        input = [1, 2, 3, 4, 5, 6]
        k = 4
        output = [3, 4, 5, 6, 1, 2]
        Solution().rotate(input, k)
        self.assertEqual(input, output)
        input = [1, 2, 3, 4, 5, 6]
        k = 5
        output = [2, 3, 4, 5, 6, 1]
        Solution().rotate(input, k)
        self.assertEqual(input, output)
