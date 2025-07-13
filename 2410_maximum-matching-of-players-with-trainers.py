import unittest
from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        trainers_index = 0
        matches = 0

        for player_index in range(len(players)):
            while (
                trainers_index < len(trainers)
                and trainers[trainers_index] < players[player_index]
            ):
                trainers_index += 1
            if trainers_index < len(trainers):
                matches += 1
                trainers_index += 1

        return matches


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        players = [4, 7, 9]
        trainers = [8, 2, 5, 8]
        expected = 2
        actual = Solution().matchPlayersAndTrainers(players, trainers)
        self.assertEqual(actual, expected)

    def test_example_2(self):
        players = [1, 1, 1]
        trainers = [10]
        expected = 1
        actual = Solution().matchPlayersAndTrainers(players, trainers)
        self.assertEqual(actual, expected)
