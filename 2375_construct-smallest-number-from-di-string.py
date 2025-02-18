import unittest


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = []
        used = set()

        def backtrack(idx: int, num: int):
            if num <= 0 or num >= 10 or num in used:
                return False

            res.append(num)
            used.add(num)

            if len(res) == len(pattern) + 1:
                return True

            if pattern[idx] == "I":
                for i in range(num + 1, 10):
                    if backtrack(idx + 1, i):
                        return True
            else:
                for j in range(num - 1, 0, -1):
                    if backtrack(idx + 1, j):
                        return True

            res.pop()
            used.remove(num)

            return False

        for num in range(1, 10):
            if backtrack(0, num):
                return "".join(str(x) for x in res)


class TestSolution(unittest.TestCase):
    def test_1(self):
        pattern = "IIIDIDDD"
        output = "123549876"
        self.assertEqual(Solution().smallestNumber(pattern), output)

    def test_2(self):
        pattern = "DDD"
        output = "4321"
        self.assertEqual(Solution().smallestNumber(pattern), output)
