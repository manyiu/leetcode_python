from typing import List
import unittest


class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        board = [["."] * n for _ in range(n)]

        def checkSafe(newPlace: tuple[int, int]) -> bool:
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == "Q":
                        if (
                            i == newPlace[0]
                            or j == newPlace[1]
                            or abs(i - newPlace[0]) == abs(j - newPlace[1])
                        ):
                            return False

            return True

        def backtrack(row: int):
            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for col in range(n):
                if checkSafe((row, col)):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."

            return True

        backtrack(0)

        return res


class TestSolution(unittest.TestCase):

    def test_solution(self):
        sol = Solution()

        self.assertListEqual(
            sol.solveNQueens(4),
            [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]],
        )
        self.assertListEqual(
            sol.solveNQueens(1),
            [["Q"]],
        )
        self.assertListEqual(
            sol.solveNQueens(2),
            [],
        )
