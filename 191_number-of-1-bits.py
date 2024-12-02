import unittest


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n > 0:
            res += n & 1
            n >>= 1

        return res


class TestSolution(unittest.TestCase):
    def test_0(self):
        solution = Solution()
        self.assertEqual(solution.hammingWeight(11), 3)

    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.hammingWeight(128), 1)

    def test_2(self):
        solution = Solution()
        self.assertEqual(solution.hammingWeight(4294967293), 31)
