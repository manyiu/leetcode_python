from typing import List
import unittest


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)

        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)

        return res

    # def countBits(self, n: int) -> List[int]:
    #     res = []

    #     for i in range(n + 1):
    #         count = 0
    #         while i > 0:
    #             count += i & 1
    #             i >>= 1
    #         res.append(count)

    #     return res


class TestSolution(unittest.TestCase):
    def test_0(self):
        solution = Solution()
        self.assertEqual(solution.countBits(2), [0, 1, 1])

    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.countBits(5), [0, 1, 1, 2, 1, 2])

    def test_2(self):
        solution = Solution()
        self.assertEqual(solution.countBits(0), [0])
