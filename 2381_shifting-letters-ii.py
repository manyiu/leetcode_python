from typing import List
import unittest


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_diff = [0] * (len(s) + 1)

        for start, end, shift in shifts:
            prefix_diff[start] += -1 if shift == 0 else 1
            prefix_diff[end + 1] += 1 if shift == 0 else -1

        diff = 0

        res = [ord(c) - ord("a") for c in s]

        for i in range(len(s)):
            diff += prefix_diff[i]
            res[i] = (res[i] + diff) % 26

        s = [chr(ord("a") + n) for n in res]

        return "".join(s)

    # def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
    #     ch_codes = [ord(ch) - ord("a") for ch in s]

    #     for start, end, shift in shifts:
    #         dir = -1 if shift == 0 else 1

    #         for i in range(start, end + 1):
    #             ch_codes[i] += dir
    #             ch_codes[i] %= 26

    #     res = ""

    #     for ch_code in ch_codes:
    #         res += chr(ch_code + ord("a"))

    #     return res

    # def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
    #     offsets = [0] * len(s)

    #     for start, end, direction in shifts:
    #         for i in range(start, end + 1):
    #             step = -1 if direction == 0 else 1
    #             offsets[i] += step

    #     res = ""

    #     for i, ch in enumerate(s):
    #         offset = offsets[i] % 26

    #         curr = ""

    #         if ord(ch) + offset < ord("a"):
    #             curr = chr(ord("z") - (ord(ch) + offset - ord("a") + 1))
    #         elif ord(ch) + offset > ord("z"):
    #             curr = chr(ord("a") + (ord(ch) + offset - ord("z") - 1))
    #         else:
    #             curr = chr(ord(ch) + offset)

    #         res += curr

    #     return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "abc"
        shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
        output = "ace"
        assert Solution().shiftingLetters(s, shifts) == output

    def test_2(self):
        s = "dztz"
        shifts = [[0, 0, 0], [1, 1, 1]]
        output = "catz"
        assert Solution().shiftingLetters(s, shifts) == output
