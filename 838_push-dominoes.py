import unittest


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        l = r = 0
        res = list(dominoes)

        symbols = [(i, v) for i, v in enumerate(dominoes) if v != "."]
        symbols = [(-1, "L")] + symbols + [(len(dominoes), "R")]

        for (l, x), (r, y) in zip(symbols, symbols[1:]):
            if x == y:
                for i in range(l+1, r):
                    res[i] = x
            elif x == "R" and y =="L":
                m = l + (r - l) / 2
                for i in range(l+1, r):
                    if i < m:
                        res[i] = "R"
                    elif i > m:
                        res[i] = "L"
        
        return "".join(res)

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        dominoes = "RR.L"
        expected = "RR.L"
        self.assertEqual(Solution().pushDominoes(dominoes), expected)

    def test_example_2(self):
        dominoes = ".L.R...LR..L.."
        expected = "LL.RR.LLRRLL.."
        self.assertEqual(Solution().pushDominoes(dominoes), expected)