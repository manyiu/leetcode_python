import unittest


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            res = (res << 1) + (n & 1)
            n >>= 1

        return res


class TestSolution(unittest.TestCase):
    def test_0(self):
        solution = Solution()
        self.assertEqual(solution.reverseBits(43261596), 964176192)

    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.reverseBits(4294967293), 3221225471)

    def test_2(self):
        solution = Solution()
        self.assertEqual(solution.reverseBits(0), 0)

    def test_3(self):
        solution = Solution()
        self.assertEqual(solution.reverseBits(1), 2147483648)

    def test_4(self):
        solution = Solution()
        self.assertEqual(solution.reverseBits(2147483648), 1)
