import unittest

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True

class TestSolution(unittest.TestCase):

    def test(self):
        s = "A man, a plan, a canal: Panama"
        self.assertEqual(Solution().isPalindrome(s), True)
        
        s = "race a car"
        self.assertEqual(Solution().isPalindrome(s), False)

        s = " "
        self.assertEqual(Solution().isPalindrome(s), True)

        s = "0P"
        self.assertEqual(Solution().isPalindrome(s), False)