from typing import List
import unittest


class Solution:
    def merge(self, a: List[int], b: List[int]) -> List[int]:
        combine = []

        i, j = 0, 0

        while i < len(a) or j < len(b):
            if i >= len(a):
                combine.append(b[j])
                j += 1
                continue
            if j >= len(b):
                combine.append(a[i])
                i += 1
                continue
            if a[i] <= b[j]:
                combine.append(a[i])
                i += 1
            else:
                combine.append(b[j])
                j += 1

        return combine

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        n = len(nums)

        a = nums[:n//2]
        b = nums[n//2:]
        m = self.merge(self.sortArray(a), self.sortArray(b))

        return m

class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [5,2,3,1]
        output = sorted(nums)
        self.assertEqual(Solution().sortArray(nums), output)

    def test_2(self):
        nums = [5,1,1,2,0,0]
        output = sorted(nums)
        self.assertEqual(Solution().sortArray(nums), output)