from typing import List
import unittest


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(i: int, j: int):
            if (
                i < 0
                or i >= len(board)
                or j < 0
                or j >= len(board[i])
                or board[i][j] == "X"
                or board[i][j] == "T"
            ):
                return

            board[i][j] = "T"

            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i, j + 1)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i in [0, len(board) - 1] or j in [0, len(board[i]) - 1]) and board[
                    i
                ][j] == "O":
                    dfs(i, j)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"


class TestSolve(unittest.TestCase):
    def test_1(self):
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
        Solution().solve(board)
        self.assertEqual(
            board,
            [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "O", "X", "X"],
            ],
        )

    def test_2(self):
        board = [["X"]]
        Solution().solve(board)
        self.assertEqual(board, [["X"]])

    def test_3(self):
        board = [["O"]]
        Solution().solve(board)
        self.assertEqual(board, [["O"]])
