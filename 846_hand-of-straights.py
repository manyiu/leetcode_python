from typing import List
import unittest


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()

        count = {}

        for card in hand:
            if card not in count:
                count[card] = 0
            count[card] += 1

        for card in hand:
            if count[card] > 0:
                for i in range(groupSize):
                    if card + i in count and count[card + i] > 0:
                        count[card + i] -= 1
                    else:
                        return False

        return True


class TestSolution(unittest.TestCase):
    def test_1(self):
        hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
        groupSize = 3
        assert Solution().isNStraightHand(hand, groupSize) == True

    def test_2(self):
        hand = [1, 2, 3, 4, 5]
        groupSize = 4
        assert Solution().isNStraightHand(hand, groupSize) == False

    def test_3(self):
        hand = [1, 2, 3, 4, 5, 6]
        groupSize = 2
        assert Solution().isNStraightHand(hand, groupSize) == True
