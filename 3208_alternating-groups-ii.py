from typing import List
import unittest


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        l = 0
        res = 0

        for r in range(1, n + k - 1):
            if colors[r % n] == colors[(r - 1) % n]:
                l = r

            if r - l + 1 > k:
                l += 1

            if r - l + 1 == k:
                res += 1

        return res

    # def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
    #     n = len(colors)

    #     if k > n:
    #         return 0

    #     res = 0

    #     for i in range(n):
    #         count = 1

    #         prev = colors[i]

    #         for j in range(i + 1, i + k):
    #             if colors[j % n] != prev:
    #                 count += 1
    #                 prev = colors[j % n]
    #             else:
    #                 print(j)
    #                 print(count)
    #                 break

    #         if count == k:
    #             res += 1

    #     return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        colors = [0, 1, 0, 1, 0]
        k = 3
        output = 3
        self.assertEqual(Solution().numberOfAlternatingGroups(colors, k), output)

    def test_2(self):
        colors = [0, 1, 0, 0, 1, 0, 1]
        k = 6
        output = 2
        self.assertEqual(Solution().numberOfAlternatingGroups(colors, k), output)

    def test_3(self):
        colors = [1, 1, 0, 1]
        k = 4
        output = 0
        self.assertEqual(Solution().numberOfAlternatingGroups(colors, k), output)

    def test_4(self):
        colors = [0, 1, 0, 1]
        k = 3
        output = 4
        self.assertEqual(Solution().numberOfAlternatingGroups(colors, k), output)
