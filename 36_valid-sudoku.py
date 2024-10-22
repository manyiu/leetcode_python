from typing import List
import unittest
import logging


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row_set = set()
            for j in range (len(board[i])):
                if board[i][j] != ".":
                    if board[i][j] in row_set:
                        return False
                    else:
                        row_set.add(board[i][j])

        for i in range(len(board[0])):
            column_set = set()
            for j in range(len(board)):
                if board[j][i] != ".":
                    if board[j][i] in column_set:
                        return False
                    else:
                        column_set.add(board[j][i])

        for i in range(0, len(board), 3):
            for j in range(0, len(board[i]), 3):
                block_set = set()
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] != ".":
                            if board[i+k][j+l] in block_set:
                                return False
                            else:
                                block_set.add(board[i+k][j+l])

        return True

        

class TestSolution(unittest.TestCase):

    def test(self):
        board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
        self.assertEqual(Solution().isValidSudoku(board), True)

        board = [
            ["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
        self.assertEqual(Solution().isValidSudoku(board), False)

        board = [
            [".",".",".",".","5",".",".","1","."],
            [".","4",".","3",".",".",".",".","."],
            [".",".",".",".",".","3",".",".","1"],
            ["8",".",".",".",".",".",".","2","."],
            [".",".","2",".","7",".",".",".","."],
            [".","1","5",".",".",".",".",".","."],
            [".",".",".",".",".","2",".",".","."],
            [".","2",".","9",".",".",".",".","."],
            [".",".","4",".",".",".",".",".","."]
        ]
        self.assertEqual(Solution().isValidSudoku(board), False)

