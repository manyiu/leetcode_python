from collections import defaultdict
import unittest


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atLeastKConsonants(k: int) -> int:
            vowel = defaultdict(int)
            non_vowel = 0
            res = 0
            l = 0

            for r in range(len(word)):
                if word[r] in "aeiou":
                    vowel[word[r]] += 1
                else:
                    non_vowel += 1

                while len(vowel) == 5 and non_vowel >= k:
                    res += len(word) - r

                    if word[l] in "aeiou":
                        vowel[word[l]] -= 1

                        if vowel[word[l]] == 0:
                            vowel.pop(word[l])
                    else:
                        non_vowel -= 1

                    l += 1

            return res

        return atLeastKConsonants(k) - atLeastKConsonants(k + 1)


class TestSolution(unittest.TestCase):
    def test_1(self):
        word = "aeioqq"
        k = 1
        output = 0
        self.assertEqual(Solution().countOfSubstrings(word, k), output)

    def test_2(self):
        word = "aeiou"
        k = 0
        output = 1
        self.assertEqual(Solution().countOfSubstrings(word, k), output)

    def test_3(self):
        word = "ieaouqqieaouqq"
        k = 1
        output = 3
        self.assertEqual(Solution().countOfSubstrings(word, k), output)

    def test_4(self):
        word = "iqeaouqi"
        k = 2
        output = 3
        self.assertEqual(Solution().countOfSubstrings(word, k), output)
