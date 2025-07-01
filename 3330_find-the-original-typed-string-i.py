import unittest


class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1

        for i in range(1, len(word)):
            if word[i - 1] == word[i]:
                res += 1

        return res


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        word = "abbcccc"
        expected = 5
        actual = Solution().possibleStringCount(word)
        self.assertEqual(actual, expected)

    def test_example_2(self):
        word = "abcd"
        expected = 1
        actual = Solution().possibleStringCount(word)
        self.assertEqual(actual, expected)

    def test_example_3(self):
        word = "aaaa"
        expected = 4
        actual = Solution().possibleStringCount(word)
        self.assertEqual(actual, expected)
