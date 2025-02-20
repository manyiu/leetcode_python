from typing import List
import unittest


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        seen = set(nums)

        def backtrack(i: int, curr: str) -> str:
            if i == len(nums):
                if curr not in seen:
                    return curr
                return ""

            return backtrack(i + 1, curr + "0") or backtrack(i + 1, curr + "1")

        return backtrack(0, "")

    # def findDifferentBinaryString(self, nums: List[str]) -> str:
    #     seen = set(nums)

    #     for i in range(2 ** len(nums)):
    #         binary = format(i, f"0{len(nums)}b")

    #         if binary not in seen:
    #             return binary


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = ["01", "10"]
        output = ["00", "11"]
        self.assertIn(Solution().findDifferentBinaryString(nums), output)

    def test_2(self):
        nums = ["00", "01"]
        output = ["10", "11"]
        self.assertIn(Solution().findDifferentBinaryString(nums), output)

    def test_3(self):
        nums = ["111", "011", "001"]
        output = ["000", "010", "100", "101", "110"]
        self.assertIn(Solution().findDifferentBinaryString(nums), output)
