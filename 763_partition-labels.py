from typing import List
import unittest


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i in range(len(s)):
            lastIndex[s[i]] = i

        result = []
        size, end = 0, 0

        for i in range(len(s)):
            size += 1
            end = max(end, lastIndex[s[i]])

            if i == end:
                result.append(size)
                size = 0

        return result


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "ababcbacadefegdehijhklij"
        assert Solution().partitionLabels(s) == [9, 7, 8]

    def test_2(self):
        s = "eccbbbbdec"
        assert Solution().partitionLabels(s) == [10]
