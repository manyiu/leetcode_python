from typing import List
import unittest


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        curr_odd = set()

        for i in range(len(arr)):
            if arr[i] % 2 == 1:
                curr_odd.add(i)
                if len(curr_odd) >= 3:
                    return True
            curr_odd.discard(i-2)

        return False
    

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        arr = [2,6,4,1]
        expected = False
        self.assertEqual(Solution().threeConsecutiveOdds(arr), expected)

    def test_example_2(self):
        arr = [1,2,34,3,4,5,7,23,12]
        expected = True
        self.assertEqual(Solution().threeConsecutiveOdds(arr), expected)