import unittest


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        i, j = 0, 0

        while i <= len(start) and j <= len(start):
            while i < len(start) and start[i] == "_":
                i += 1
            while j < len(target) and target[j] == "_":
                j += 1

            if i == len(start) or j == len(target):
                return i == j

            if start[i] != target[j]:
                return False

            if (start[i] == "L" and i < j) or (start[i] == "R" and i > j):
                return False

            i += 1
            j += 1

        return True


class TestSolution(unittest.TestCase):
    def test_0(self):
        solution = Solution()
        self.assertEqual(
            solution.canChange("_L__R__R_", "L______RR"),
            True,
        )

    def test_1(self):
        solution = Solution()
        self.assertEqual(
            solution.canChange("R_L_", "__LR"),
            False,
        )

    def test_2(self):
        solution = Solution()
        self.assertEqual(
            solution.canChange("_R", "R_"),
            False,
        )

    def test_3(self):
        solution = Solution()
        self.assertEqual(
            solution.canChange("_L", "LL"),
            False,
        )
