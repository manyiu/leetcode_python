import unittest


class Solution:
    def punishmentNumber(self, n: int) -> int:
        def partition(i: int, cur: int, target: int, string: str) -> bool:
            if i == len(string) and cur == target:
                return True

            for j in range(i, len(string)):
                if partition(j + 1, cur + int(string[i : j + 1]), target, string):
                    return True

            return False

        res = 0

        for i in range(1, n + 1):
            if partition(0, 0, i, str(i * i)):
                res += i * i

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        n = 10
        output = 182
        self.assertEqual(solution.punishmentNumber(n), output)

    def test_2(self):
        solution = Solution()
        n = 37
        output = 1478
        self.assertEqual(solution.punishmentNumber(n), output)
