import unittest


class Solution(object):
    def wallsAndGates(self, rooms):

        def dfs(row: int, column: int, dist: int):
            if (
                row < 0
                or row >= len(rooms)
                or column < 0
                or column >= len(rooms[row])
                or rooms[row][column] == -1
                or (dist > rooms[row][column])
            ):
                return

            rooms[row][column] = dist

            dfs(row - 1, column, dist + 1)
            dfs(row, column - 1, dist + 1)
            dfs(row + 1, column, dist + 1)
            dfs(row, column + 1, dist + 1)

        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0:
                    dfs(i, j, 0)


class TestWallsAndGates(unittest.TestCase):
    def test_1(self):
        rooms = [
            [2147483647, -1, 0, 2147483647],
            [2147483647, 2147483647, 2147483647, -1],
            [2147483647, -1, 2147483647, -1],
            [0, -1, 2147483647, 2147483647],
        ]
        Solution().wallsAndGates(rooms)
        self.assertEqual(
            rooms, [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
        )

    def test_2(self):
        rooms = [[0, -1], [2147483647, 2147483647]]
        Solution().wallsAndGates(rooms)
        self.assertEqual(rooms, [[0, -1], [1, 2]])
