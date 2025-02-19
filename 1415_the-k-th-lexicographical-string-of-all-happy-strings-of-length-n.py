from math import ceil
import unittest


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        partition = 2 ** (n - 1)

        if k > 3 * partition:
            return ""

        result = ["a", "b", "c"][ceil(k / partition) - 1]

        while partition > 1:
            k = (k - 1) % partition + 1
            partition //= 2

            if result[-1] == "a":
                result += ["b", "c"][ceil(k / partition) - 1]
            elif result[-1] == "b":
                result += ["a", "c"][ceil(k / partition) - 1]
            else:
                result += ["a", "b"][ceil(k / partition) - 1]

        return result

    # def getHappyString(self, n: int, k: int) -> str:
    #     comb = []

    #     def helper(i: int, curr: str) -> None:
    #         if i == n:
    #             comb.append(curr)
    #             return

    #         for ch in ["a", "b", "c"]:
    #             if i != 0 and ch == curr[-1]:
    #                 continue
    #             helper(i + 1, curr + ch)

    #     helper(0, "")

    #     return comb[k - 1] if len(comb) >= k else ""


class TestSolution(unittest.TestCase):
    def test_1(self):
        n = 1
        k = 3
        output = "c"
        self.assertEqual(Solution().getHappyString(n, k), output)

    def test_2(self):
        n = 1
        k = 4
        output = ""
        self.assertEqual(Solution().getHappyString(n, k), output)

    def test_3(self):
        n = 3
        k = 9
        output = "cab"
        self.assertEqual(Solution().getHappyString(n, k), output)

    def test_4(self):
        n = 2
        k = 7
        output = ""
        self.assertEqual(Solution().getHappyString(n, k), output)

    def test_5(self):
        n = 10
        k = 100
        output = "abacbabacb"
        self.assertEqual(Solution().getHappyString(n, k), output)
