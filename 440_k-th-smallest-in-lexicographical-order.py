import unittest


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        current = 1
        k -= 1

        while k > 0:
            count = 0
            first = current
            last = current + 1

            while first <= n:
                count += min(n + 1, last) - first
                first *= 10
                last *= 10

            if count <= k:
                k -= count
                current += 1
            else:
                k -= 1
                current *= 10

        return current


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        n = 13
        k = 2
        expected = 10
        solution = Solution()
        result = solution.findKthNumber(n, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_example_2(self):
        n = 2
        k = 1
        expected = 1
        solution = Solution()
        result = solution.findKthNumber(n, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")
