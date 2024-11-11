from typing import List
import unittest


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = set()

        def dfs(i: int, j: int, wordIndex: int) -> bool:
            if (
                i < 0
                or i >= len(board)
                or j < 0
                or j >= len(board[i])
                or board[i][j] != word[wordIndex]
                or (i, j) in visit
            ):
                return False

            if wordIndex == len(word) - 1:
                return True

            visit.add((i, j))

            res = (
                dfs(i - 1, j, wordIndex + 1)
                or dfs(i, j - 1, wordIndex + 1)
                or dfs(i + 1, j, wordIndex + 1)
                or dfs(i, j + 1, wordIndex + 1)
            )

            visit.remove((i, j))

            return res

        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(i, j, 0):
                    return True

        return False


class TestSolution(unittest.TestCase):

    def test_solution(self):
        sol = Solution()

        self.assertTrue(
            sol.exist(
                [
                    ["A", "B", "C", "E"],
                    ["S", "F", "C", "S"],
                    ["A", "D", "E", "E"],
                ],
                "ABCCED",
            )
        )
        self.assertTrue(
            sol.exist(
                [
                    ["A", "B", "C", "E"],
                    ["S", "F", "C", "S"],
                    ["A", "D", "E", "E"],
                ],
                "SEE",
            )
        )
        self.assertFalse(
            sol.exist(
                [
                    ["A", "B", "C", "E"],
                    ["S", "F", "C", "S"],
                    ["A", "D", "E", "E"],
                ],
                "ABCB",
            )
        )
