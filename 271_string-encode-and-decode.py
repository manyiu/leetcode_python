from typing import List
import unittest


class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for str_value in strs:
            encoded_str = str(len(str_value)) + ":" + str_value
            result += encoded_str
        
        return result

    def decode(self, s: str) -> List[str]:
        i, j = 0, 0
        result = []

        while j < len(s):
            if s[i] == ":":
                numberStr = s[j:i]
                number = int(numberStr)
                itemStr = s[i+1: i+1+number]
                result.append(itemStr)
                j = i + 1 + number
                i = j
            else:
                i += 1

        return result

class TestSolution(unittest.TestCase):

    def test(self):
        strs = ["Hello", "World"]
        self.assertEqual(Solution().decode(Solution().encode(strs)), strs)
        strs = ["Hello", "World", "Hello", "World"]
        self.assertEqual(Solution().decode(Solution().encode(strs)), strs)
        strs = []
        self.assertEqual(Solution().decode(Solution().encode(strs)), strs)
        strs = [""]
        self.assertEqual(Solution().decode(Solution().encode(strs)), strs)
        strs = ["Hello"]
        self.assertEqual(Solution().decode(Solution().encode(strs)), strs)
        strs = ["Hello", "World", "Hello", "World", "Hello", "World"]
        self.assertEqual(Solution().decode(Solution().encode(strs)), strs)
        strs = ["Hello", "World", "Hello", "World", "Hello", "World", "Hello", "World"]
        self.assertEqual(Solution().decode(Solution().encode(strs)), strs)
        strs = ["Hello", "World", "Hello", "World", "Hello", "World", "Hello", "World", "Hello", "World"]
        self.assertEqual(Solution().decode(Solution().encode(strs)), strs)
        strs = ["Hello", "World", "Hello", "World", "Hello", "World", "Hello", "World", "Hello", "World", "Hello", "World"]
        self.assertEqual(Solution().decode(Solution().encode(strs)), strs)