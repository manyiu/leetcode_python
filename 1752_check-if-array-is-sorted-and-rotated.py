from typing import List
import unittest


class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        count = 1

        for i in range(1, 2 * N):
            if nums[(i - 1) % N] <= nums[i % N]:
                count += 1
            else:
                count = 1
            if count == N:
                return True

        return N == 1


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [3, 4, 5, 1, 2]
        output = True
        self.assertEqual(Solution().check(nums), output)

    def test_2(self):
        nums = [2, 1, 3, 4]
        output = False
        self.assertEqual(Solution().check(nums), output)

    def test_3(self):
        nums = [1, 2, 3]
        output = True
        self.assertEqual(Solution().check(nums), output)

    def test_4(self):
        nums = [1, 1, 1]
        output = True
        self.assertEqual(Solution().check(nums), output)

    def test_5(self):
        nums = [2, 1]
        output = True
        self.assertEqual(Solution().check(nums), output)

    def test_6(self):
        nums = [3, 4, 5, 1, 2]
        output = True
        self.assertEqual(Solution().check(nums), output)

    def test_7(self):
        nums = [1, 2, 3, 4]
        output = True
        self.assertEqual(Solution().check(nums), output)

    def test_8(self):
        nums = [3, 6, 10, 1, 8, 9, 9, 8, 9]
        output = False
        self.assertEqual(Solution().check(nums), output)
