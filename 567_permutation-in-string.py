import unittest


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = 0
        freq = dict()

        for i in s1:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
                count += 1

        for i in range(len(s2)):
            if s2[i] in freq:
                freq[s2[i]] -= 1
                if freq[s2[i]] == 0:
                    count -= 1
                if freq[s2[i]] == -1:
                    count += 1

            if i >= len(s1) and s2[i - len(s1)] in freq:
                freq[s2[i - len(s1)]] += 1
                if freq[s2[i-len(s1)]] == 0:
                    count -= 1
                if freq[s2[i-len(s1)]] == 1:
                    count += 1

            if count == 0:
                return True
        
        return False
        

class TestSolution(unittest.TestCase):
    def test(self):
        s1 = "ab"
        s2 = "eidbaooo"
        self.assertEqual(Solution().checkInclusion(s1, s2), True)
        s1 = "ab"
        s2 = "eidboaoo"
        self.assertEqual(Solution().checkInclusion(s1, s2), False)
        s1 = "adc"
        s2 = "dcda"
        self.assertEqual(Solution().checkInclusion(s1, s2), True)
        s1 = "hello"
        s2 = "ooolleoooleh"
        self.assertEqual(Solution().checkInclusion(s1, s2), False)
        s1 = "ab"
        s2 = "eidbaooo"
        self.assertEqual(Solution().checkInclusion(s1, s2), True)
        s1 = "ab"
        s2 = "eidboaoo"
        self.assertEqual(Solution().checkInclusion(s1, s2), False)
        s1 = "adc"
        s2 = "dcda"
        self.assertEqual(Solution().checkInclusion(s1, s2), True)
        s1 = "hello"
        s2 = "ooolleoooleh"
        self.assertEqual(Solution().checkInclusion(s1, s2), False)