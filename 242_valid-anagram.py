import unittest

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = dict()
        count = 0

        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
                count += 1

        for c in t:
            if c in freq:
                freq[c] -= 1
                if freq[c] == 0:
                    count -= 1
                    if count < 0:
                        return False
                elif freq[c] < 0:
                    return False
            else:
                return False
            
        if count != 0:
            return False

        return True
            
class TestSolution(unittest.TestCase):
    def test(self):
        s = "anagram"
        t = "nagaram"
        self.assertEqual(Solution().isAnagram(s, t), True)
        s = "rat"
        t = "car"
        self.assertEqual(Solution().isAnagram(s, t), False)