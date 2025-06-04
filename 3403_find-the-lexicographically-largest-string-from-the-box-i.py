import unittest


class Solution:
    def lexicographicallyLarger(self, a: str, b: str) -> bool:
        min_length = min(len(a), len(b))

        for i in range(min_length):
            if a[i] > b[i]:
                return True
            elif a[i] < b[i]:
                return False
            
        return len(a) > len(b)

    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        
        n = len(word)
        
        box_width = n - numFriends + 1

        res = ""

        for i in range(n):
            curr_substring = word[i: min(i + box_width, n + 1)]

            if self.lexicographicallyLarger(curr_substring, res):
                res = curr_substring

        return res

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        word = "dbca"
        numFriends = 2
        expected = "dbc"
        actual = Solution().answerString(word, numFriends)
        self.assertEqual(actual, expected)

    def test_example_2(self):
        word = "gggg"
        numFriends = 4
        expected = "g"
        actual = Solution().answerString(word, numFriends)
        self.assertEqual(actual, expected)

    def test_case_358(self):
        word = "b"
        numFriends = 1
        expected = "b"
        actual = Solution().answerString(word, numFriends)
        self.assertEqual(actual, expected)

    def test_case_566(self):
        word = "aann"
        numFriends = 2
        expected = "nn"
        actual = Solution().answerString(word, numFriends)
        self.assertEqual(actual, expected)

    def test_case_695(self):
        word = "gh"
        numFriends = 1
        expected = "gh"
        actual = Solution().answerString(word, numFriends)
        self.assertEqual(actual, expected)
