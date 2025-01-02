from typing import List
import unittest


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]

        res = ""

        for i in range(len(first)):
            for str in strs:
                if i + 1 > len(str) or str[i] != first[i]:
                    return res
            res += first[i]

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        input = ["flower", "flow", "flight"]
        output = "fl"
        assert Solution().longestCommonPrefix(input) == output

    def test_2(self):
        input = ["dog", "racecar", "car"]
        output = ""
        assert Solution().longestCommonPrefix(input) == output

    def test_3(self):
        input = ["a"]
        output = "a"
        assert Solution().longestCommonPrefix(input) == output
