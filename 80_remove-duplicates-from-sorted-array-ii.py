from typing import List
import unittest


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = 2
        l, r = 0, 0

        while r < n:
            count = 1

            while r + 1 < n and nums[r] == nums[r + 1]:
                r += 1
                count += 1

            for i in range(min(k, count)):
                nums[l] = nums[r]
                l += 1

            r += 1

        return l


class TestSolution(unittest.TestCase):
    def test(self):
        input = [1, 1, 1, 2, 2, 3]
        output = [1, 1, 2, 2, 3]
        self.assertEqual(Solution().removeDuplicates(input), len(output))
        self.assertEqual(input[: len(output)], output)
        input = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        output = [0, 0, 1, 1, 2, 3, 3]
        self.assertEqual(Solution().removeDuplicates(input), len(output))
        self.assertEqual(input[: len(output)], output)
        input = [1, 1, 1]
        output = [1, 1]
        self.assertEqual(Solution().removeDuplicates(input), len(output))
        self.assertEqual(input[: len(output)], output)
        input = [1, 1, 1, 1, 1, 1, 1]
        output = [1, 1]
        self.assertEqual(Solution().removeDuplicates(input), len(output))
        self.assertEqual(input[: len(output)], output)
        input = [1, 1, 1, 1, 1, 1, 2]
        output = [1, 1, 2]
        self.assertEqual(Solution().removeDuplicates(input), len(output))
        self.assertEqual(input[: len(output)], output)
        input = [1, 1, 1, 1, 1, 1, 2, 2]
        output = [1, 1, 2, 2]
        self.assertEqual(Solution().removeDuplicates(input), len(output))
        self.assertEqual(input[: len(output)], output)
        input = [1, 1, 1, 1, 1, 1, 2, 2, 2]
        output = [1, 1, 2, 2]
        self.assertEqual(Solution().removeDuplicates(input), len(output))
        self.assertEqual(input[: len(output)], output)
        input = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2]
        output = [1, 1, 2, 2]
        self.assertEqual(Solution().removeDuplicates(input), len(output))
        self.assertEqual(input[: len(output)], output)
