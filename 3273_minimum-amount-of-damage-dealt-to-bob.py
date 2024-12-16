from math import ceil
from typing import List
import unittest


class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        n = len(damage)

        comp = [(ceil(health[i] / power) / damage[i], i) for i in range(n)]
        comp.sort()

        res = 0
        t = 0

        for _, i in comp:
            t += ceil(health[i] / power)
            res += damage[i] * t

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        power = 4
        damage = [1, 2, 3, 4]
        health = [4, 5, 6, 8]
        assert Solution().minDamage(power, damage, health) == 39

    def test_2(self):
        power = 1
        damage = [1, 1, 1, 1]
        health = [1, 2, 3, 4]
        assert Solution().minDamage(power, damage, health) == 20

    def test_3(self):
        power = 8
        damage = [40]
        health = [59]
        assert Solution().minDamage(power, damage, health) == 320
