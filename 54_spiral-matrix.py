from typing import List
import unittest


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        visit = set()

        def dfs(i: int, j: int, direction: tuple[int, int]) -> bool:
            if (
                i < 0
                or i >= len(matrix)
                or j < 0
                or j >= len(matrix[i])
                or (i, j) in visit
            ):
                return False

            visit.add((i, j))
            res.append(matrix[i][j])

            if not dfs(i + direction[0], j + direction[1], direction):
                return dfs(
                    i + direction[1], j - direction[0], (direction[1], -direction[0])
                )

            return True

        dfs(0, 0, (0, 1))

        return res


class TestSolution(unittest.TestCase):
    def test_0(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(Solution().spiralOrder(matrix), [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test_1(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        self.assertEqual(
            Solution().spiralOrder(matrix), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        )

    def test_2(self):
        matrix = [[1]]
        self.assertEqual(Solution().spiralOrder(matrix), [1])

    def test_3(self):
        matrix = [[1, 2], [3, 4]]
        self.assertEqual(Solution().spiralOrder(matrix), [1, 2, 4, 3])

    def test_4(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
            [17, 18, 19, 20],
            [21, 22, 23, 24],
        ]
        self.assertEqual(
            Solution().spiralOrder(matrix),
            [
                1,
                2,
                3,
                4,
                8,
                12,
                16,
                20,
                24,
                23,
                22,
                21,
                17,
                13,
                9,
                5,
                6,
                7,
                11,
                15,
                19,
                18,
                14,
                10,
            ],
        )
