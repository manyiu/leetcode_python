from typing import List
import unittest


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        curr_sum = 0
        odd_count = 0
        event_count = 0
        res = 0
        MOD = 10**9 + 7

        for num in arr:
            curr_sum += num

            if curr_sum % 2 == 0:
                event_count += 1
                res = (res + odd_count) % MOD
            else:
                odd_count += 1
                res = (res + 1 + event_count) % MOD

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        arr = [1,3,5]
        output = 4
        self.assertEqual(Solution().numOfSubarrays(arr), output)

    def test_2(self):
        arr = [2,4,6]
        output = 0
        self.assertEqual(Solution().numOfSubarrays(arr), output)

    def test_3(self):
        arr = [1,2,3,4,5,6,7]
        output = 16
        self.assertEqual(Solution().numOfSubarrays(arr), output)