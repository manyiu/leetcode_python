from typing import List
import unittest


class Tries:
    def __init__(self):
        self.children = {}
        self.end = False

    def add(self, word: str) -> None:
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c] = Tries()
            curr = curr.children[c]

        curr.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tries = Tries()
        visit = set()
        res = []

        for word in words:
            tries.add(word)

        def dfs(row: int, column: int, node: Tries, currWord: str):
            if (
                row < 0
                or column < 0
                or row >= len(board)
                or column >= len(board[row])
                or board[row][column] not in node.children
                or (row, column) in visit
            ):
                return

            node = node.children[board[row][column]]
            currWord += board[row][column]

            if node.end == True:
                res.append(currWord)
                node.end = False

            visit.add((row, column))

            dfs(row - 1, column, node, currWord)
            dfs(row, column - 1, node, currWord)
            dfs(row + 1, column, node, currWord)
            dfs(row, column + 1, node, currWord)

            visit.remove((row, column))

        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(i, j, tries, "")

        return res


class TestSolution(unittest.TestCase):

    def test_solution(self):
        solution = Solution()

        self.assertListEqual(
            sorted(["oath", "eat"]),
            sorted(
                solution.findWords(
                    board=[
                        ["o", "a", "a", "n"],
                        ["e", "t", "a", "e"],
                        ["i", "h", "k", "r"],
                        ["i", "f", "l", "v"],
                    ],
                    words=["oath", "pea", "eat", "rain"],
                )
            ),
        )

        self.assertListEqual(["a"], solution.findWords(board=[["a", "a"]], words=["a"]))

        self.assertListEqual(["a"], solution.findWords(board=[["a"]], words=["a"]))

        self.assertListEqual(
            ["ab"], solution.findWords(board=[["a", "b"]], words=["ab"])
        )
