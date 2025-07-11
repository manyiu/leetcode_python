import heapq
from typing import List
import unittest


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        free_rooms = [i for i in range(n)]
        busy_rooms = []
        room_count = [0] * n

        for start_time, end_time in sorted(meetings):
            while busy_rooms and busy_rooms[0][0] <= start_time:
                _, room_id = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room_id)
            if free_rooms:
                room_id = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (end_time, room_id))
            else:
                time, room_id = heapq.heappop(busy_rooms)
                heapq.heappush(busy_rooms, (time + (end_time - start_time), room_id))
            room_count[room_id] += 1

        return room_count.index(max(room_count))


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        n = 2
        meetings = [[0, 10], [1, 5], [2, 7], [3, 4]]
        expected = 0
        actual = Solution().mostBooked(n, meetings)
        self.assertEqual(actual, expected)

    def test_example_2(self):
        n = 3
        meetings = [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]
        expected = 1
        actual = Solution().mostBooked(n, meetings)
        self.assertEqual(actual, expected)
