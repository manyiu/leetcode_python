from typing import List
import unittest


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = {}
        res = 0

        for answer in answers:
            if answer not in count:
                count[answer] = 0
            count[answer] += 1

        for answer, answer_count in count.items():
            group_size = answer + 1
            full_groups = answer_count // group_size
            remaining = answer_count % group_size

            res += full_groups * group_size + (group_size if remaining > 0 else 0)

        return res


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        answers = [1, 1, 2]
        expected = 5
        self.assertEqual(Solution().numRabbits(answers), expected)

    def test_example_2(self):
        answers = [10, 10, 10]
        expected = 11
        self.assertEqual(Solution().numRabbits(answers), expected)
