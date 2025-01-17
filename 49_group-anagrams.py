from collections import defaultdict
from typing import List
import unittest


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for str in strs:
            sorted_str = "".join(sorted(str))
            groups[sorted_str].append(str)

        return list(groups.values())


class TestSolution(unittest.TestCase):
    def test_1(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        output = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        self.assertEqual(Solution().groupAnagrams(strs), output)

    def test_2(self):
        strs = [""]
        output = [[""]]
        self.assertEqual(Solution().groupAnagrams(strs), output)

    def test_3(self):
        strs = ["a"]
        output = [["a"]]
        self.assertEqual(Solution().groupAnagrams(strs), output)
