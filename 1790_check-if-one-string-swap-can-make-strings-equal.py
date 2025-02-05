from collections import defaultdict
import unittest


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff_indexes = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_indexes.append(i)

                if len(diff_indexes) > 2:
                    return False

        if len(diff_indexes) == 2:
            i, j = diff_indexes

            return s1[i] == s2[j] and s1[j] == s2[i]

        return len(diff_indexes) == 0

    # def areAlmostEqual(self, s1: str, s2: str) -> bool:
    #     if s1 == s2:
    #         return True

    #     diff_count = defaultdict(int)
    #     mismatch_count = 0

    #     for i in range(len(s1)):
    #         if s1[i] != s2[i]:
    #             diff_count[s1[i]] += 1
    #             diff_count[s2[i]] -= 1
    #             mismatch_count += 1

    #             if mismatch_count > 2:
    #                 return False

    #     if len(diff_count) > 2 or max(diff_count.values()) > 0:
    #         return False

    #     return True


class TestSolution(unittest.TestCase):
    def test_1(self):
        s1 = "bank"
        s2 = "kanb"
        output = True
        self.assertEqual(Solution().areAlmostEqual(s1, s2), output)

    def test_2(self):
        s1 = "attack"
        s2 = "defend"
        output = False
        self.assertEqual(Solution().areAlmostEqual(s1, s2), output)

    def test_3(self):
        s1 = "kelb"
        s2 = "kelb"
        output = True
        self.assertEqual(Solution().areAlmostEqual(s1, s2), output)

    def test_4(self):
        s1 = "qgqeg"
        s2 = "gqgeq"
        output = False
        self.assertEqual(Solution().areAlmostEqual(s1, s2), output)
