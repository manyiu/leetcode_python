import unittest


class Solution:
    def clearStars(self, s: str) -> str:
        count = [[] for _ in range(26)]
        arr = list(s)

        for i, c in enumerate(arr):
            if c == '*':
                for j in range(26):
                    if count[j]:
                        arr[count[j].pop()] = "*"
                        break
            else:
                count[ord(c) - ord('a')].append(i)

        return "".join(c for c in arr if c != "*")


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        s = "aaba*"
        expected = "aab"
        solution = Solution()
        result = solution.clearStars(s)
        self.assertEqual(result, expected)

    def test_example_2(self):
        s = "abc"
        expected = "abc"
        solution = Solution()
        result = solution.clearStars(s)
        self.assertEqual(result, expected)
