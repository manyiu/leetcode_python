from typing import List
import unittest


class Solution:
    def validStep(self, a: str, b: str) -> bool:
        count = 0

        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1

        return count == 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visit = set()

        queue = [beginWord]
        count = 1

        while queue:
            nextQueue = []
            count += 1

            for currWord in queue:
                for nextWord in wordList:
                    if nextWord not in visit and self.validStep(currWord, nextWord):
                        if nextWord == endWord:
                            return count
                        visit.add(nextWord)
                        nextQueue.append(nextWord)

            queue = nextQueue

        return 0


class TestSolution(unittest.TestCase):
    def test_0(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        res = 5
        self.assertEqual(Solution().ladderLength(beginWord, endWord, wordList), res)

    def test_1(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log"]
        res = 0
        self.assertEqual(Solution().ladderLength(beginWord, endWord, wordList), res)

    def test_2(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        res = 5
        self.assertEqual(Solution().ladderLength(beginWord, endWord, wordList), res)

    def test_3(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog", "hog"]
        res = 4
        self.assertEqual(Solution().ladderLength(beginWord, endWord, wordList), res)

    def test_4(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog", "hog", "hig"]
        res = 4
        self.assertEqual(Solution().ladderLength(beginWord, endWord, wordList), res)

    def test_5(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog", "hog", "hig", "cig"]
        res = 4
        self.assertEqual(Solution().ladderLength(beginWord, endWord, wordList), res)

    def test_6(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = [
            "hot",
            "dot",
            "dog",
            "lot",
            "log",
            "cog",
            "hog",
            "hig",
            "cig",
            "cag",
        ]
        res = 4
        self.assertEqual(Solution().ladderLength(beginWord, endWord, wordList), res)
