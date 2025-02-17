from typing import Counter
import unittest


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)

        def backtrack():
            res = 0

            for c in count:
                if count[c] > 0:
                    count[c] -= 1
                    res += 1
                    res += backtrack()
                    count[c] += 1

            return res

        return backtrack()


class TestSolution(unittest.TestCase):
    def test_1(self):
        tiles = "AAB"
        output = 8
        self.assertEqual(Solution().numTilePossibilities(tiles), output)

    def test_2(self):
        tiles = "AAABBC"
        output = 188
        self.assertEqual(Solution().numTilePossibilities(tiles), output)

    def test_3(self):
        tiles = "V"
        output = 1
        self.assertEqual(Solution().numTilePossibilities(tiles), output)
