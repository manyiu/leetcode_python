from typing import List
import unittest


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = dict()

        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str in group:
                group[sorted_str].append(str)
            else:
                group[sorted_str] = [str]

        return list(group.values())

        

class TestSolution(unittest.TestCase):
    def test(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        self.assertEqual(Solution().groupAnagrams(strs), [["eat","tea","ate"],["tan","nat"],["bat"]])