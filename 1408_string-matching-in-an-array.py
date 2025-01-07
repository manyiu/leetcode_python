from typing import List
import unittest


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    res.append(words[i])
                    break

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        input = ["mass", "as", "hero", "superhero"]
        output = ["as", "hero"]
        self.assertEqual(Solution().stringMatching(input), output)

    def test_2(self):
        input = ["leetcode", "et", "code"]
        output = ["et", "code"]
        self.assertEqual(Solution().stringMatching(input), output)

    def test_3(self):
        input = ["blue", "green", "bu"]
        output = []
        self.assertEqual(Solution().stringMatching(input), output)

    def test_4(self):
        input = ["leetcoder", "leetcode", "od", "hamlet", "am"]
        output = ["leetcode", "od", "am"]
        self.assertEqual(Solution().stringMatching(input), output)
