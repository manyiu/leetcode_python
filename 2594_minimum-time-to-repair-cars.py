import heapq
from typing import List
import unittest


class Solution:
    def canRepair(self, ranks: List[int], cars: int, time: int) -> bool:
        for rank in ranks:
            cars_repaired = int((time // rank) ** 0.5)

            # while rank * (car + 1) ** 2 <= time:
            #     car += 1

            cars -= cars_repaired

            if cars <= 0:
                return True

        return False

    # def canRepair(self, ranks: List[int], cars: int, time: int) -> bool:
    #     min_heap = [(rank, rank, 1) for rank in ranks]
    #     heapq.heapify(min_heap)

    #     total = 0

    #     while cars > 0:
    #         current_repair_time, rank, car = heapq.heappop(min_heap)
    #         total = max(total, current_repair_time)

    #         next_repair_time = rank * (car + 1) ** 2
    #         heapq.heappush(min_heap, (next_repair_time, rank, car + 1))

    #         cars -= 1

    #     return total <= time

    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 1, min(ranks) * cars * cars

        while l <= r:
            m = l + (r - l) // 2

            if self.canRepair(ranks, cars, m):
                r = m - 1
            else:
                l = m + 1

        return l


class TestSolution(unittest.TestCase):
    def test_1(self):
        ranks = [4, 2, 3, 1]
        cars = 10
        output = 16
        self.assertEqual(Solution().repairCars(ranks, cars), output)

    def test_2(self):
        ranks = [5, 1, 8]
        cars = 6
        output = 16
        self.assertEqual(Solution().repairCars(ranks, cars), output)
