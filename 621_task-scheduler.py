from collections import deque
import heapq
from typing import Counter, List
import unittest


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = [-value for value in counts.values()]
        heapq.heapify(maxHeap)

        time = 0
        queue = deque()  # [(time, count)]

        while maxHeap or queue:
            time += 1

            if maxHeap:
                count = -heapq.heappop(maxHeap) - 1

                if count >= 1:
                    queue.append((time + n, count))

            if queue and queue[0][0] == time:
                heapq.heappush(maxHeap, -queue.popleft()[1])
        return time


class TestSolution(unittest.TestCase):
    def test_1(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 2
        res = 8
        self.assertEqual(Solution().leastInterval(tasks, n), res)

    def test_2(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 0
        res = 6
        self.assertEqual(Solution().leastInterval(tasks, n), res)

    def test_3(self):
        tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
        n = 2
        res = 16
        self.assertEqual(Solution().leastInterval(tasks, n), res)
