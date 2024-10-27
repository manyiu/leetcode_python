from typing import List
import unittest


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(zip(position, speed))
        fleet = []

        for p, s in pair[::-1]:
            finish_time = (target - p) / s
            if len(fleet) == 0 or finish_time > fleet[-1]:
                fleet.append(finish_time)

        return len(fleet)


class TestCarFleet(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual(
            solution.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]),
            3,
        )
        self.assertEqual(
            solution.carFleet(10, [6, 8], [3, 2]),
            2,
        )
        self.assertEqual(
            solution.carFleet(10, [0, 4, 2], [2, 1, 3]),
            1,
        )
        self.assertEqual(
            solution.carFleet(10, [0, 4, 2], [2, 1, 1]),
            2,
        )
        self.assertEqual(
            solution.carFleet(10, [0, 4, 2], [2, 1, 2]),
            1,
        )
        self.assertEqual(
            solution.carFleet(10, [0, 4, 2], [2, 1, 4]),
            1,
        )
        self.assertEqual(
            solution.carFleet(10, [0, 4, 2], [2, 1, 5]),
            1,
        )
        self.assertEqual(
            solution.carFleet(10, [0, 4, 2], [2, 1, 6]),
            1,
        )
        self.assertEqual(
            solution.carFleet(10, [0, 4, 2], [2, 1, 7]),
            1,
        )
        self.assertEqual(
            solution.carFleet(10, [0, 4, 2], [2, 1, 8]),
            1,
        )
        self.assertEqual(
            solution.carFleet(10, [0, 4, 2], [2, 1, 9]),
            1,
        )
        self.assertEqual(
            solution.carFleet(10, [0, 4, 2], [2, 1, 10]),
            1,
        )
        self.assertEqual(
            solution.carFleet(10, [0, 4, 2], [2, 1, 11]),
            1,
        )
