import unittest


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) == 0:
            return True
        if len(str1) == 0:
            return False

        i, j = 0, 0

        while i < len(str1) and j < len(str2):
            if (
                str1[i] == str2[j]
                or ord(str1[i]) + 1 == ord(str2[j])
                or ord(str1[i]) - 25 == ord(str2[j])
            ):
                i += 1
                j += 1
            else:
                i += 1

        if j == len(str2):
            return True

        return False


class TestSolution(unittest.TestCase):
    def test_0(self):
        solution = Solution()
        self.assertEqual(
            solution.canMakeSubsequence("abc", "ad"),
            True,
        )

    def test_1(self):
        solution = Solution()
        self.assertEqual(
            solution.canMakeSubsequence("zc", "ad"),
            True,
        )

    def test_2(self):
        solution = Solution()
        self.assertEqual(
            solution.canMakeSubsequence("ab", "d"),
            False,
        )
