from typing import List
import unittest


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        profit = [g - c for g, c in zip(gas, cost)]

        total = 0
        res = 0

        for i in range(len(profit)):
            total += profit[i]

            if total < 0:
                total = 0
                res = i + 1

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        assert Solution().canCompleteCircuit(gas, cost) == 3

    def test_2(self):
        gas = [2, 3, 4]
        cost = [3, 4, 3]
        assert Solution().canCompleteCircuit(gas, cost) == -1

    def test_3(self):
        gas = [3, 1, 1]
        cost = [1, 2, 2]
        assert Solution().canCompleteCircuit(gas, cost) == 0
