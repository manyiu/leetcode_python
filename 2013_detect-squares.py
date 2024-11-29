from typing import List
import unittest


class DetectSquares:

    def __init__(self):
        self.pointsCount = {}

    def add(self, point: List[int]) -> None:
        if tuple(point) not in self.pointsCount:
            self.pointsCount[tuple(point)] = 0
        self.pointsCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0

        for posX, posY in self.pointsCount:
            if abs(x - posX) != abs(y - posY) or (x == posX and y == posY):
                continue
            if (x, posY) in self.pointsCount and (posX, y) in self.pointsCount:
                res += (
                    self.pointsCount[(posX, posY)]
                    * self.pointsCount[(x, posY)]
                    * self.pointsCount[(posX, y)]
                )

        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)


class TestDetectSquares(unittest.TestCase):
    def test_0(self):
        detect_squares = DetectSquares()
        detect_squares.add([3, 10])
        detect_squares.add([11, 2])
        detect_squares.add([3, 2])
        self.assertEqual(detect_squares.count([11, 10]), 1)
        self.assertEqual(detect_squares.count([14, 8]), 0)
        detect_squares.add([11, 2])
        self.assertEqual(detect_squares.count([11, 10]), 2)
