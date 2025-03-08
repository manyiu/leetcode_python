import unittest


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w_count = 0

        for i in range(k):
            if blocks[i] == "W":
                w_count += 1

        res = w_count

        for i in range(k, len(blocks)):
            if blocks[i] == "W":
                w_count += 1

            if blocks[i - k] == "W":
                w_count -= 1

            res = min(res, w_count)

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        blocks = "WBBWWBBWBW"
        k = 7
        output = 3
        self.assertEqual(Solution().minimumRecolors(blocks, k), output)

    def test_2(self):
        blocks = "WBWBBBW"
        k = 2
        output = 0
        self.assertEqual(Solution().minimumRecolors(blocks, k), output)
