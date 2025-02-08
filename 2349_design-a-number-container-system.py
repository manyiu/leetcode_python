from collections import defaultdict
import heapq
import unittest


class NumberContainers:

    def __init__(self):
        self.container_heap = defaultdict(list)
        self.container = defaultdict(int)

    def change(self, index: int, number: int) -> None:
        heapq.heappush(self.container_heap[number], index)
        self.container[index] = number

    def find(self, number: int) -> int:
        while self.container_heap[number]:
            index = self.container_heap[number][0]
            if self.container[index] == number:
                return index
            else:
                heapq.heappop(self.container_heap[number])
        return -1


class TestSolution(unittest.TestCase):
    def test_1(self):
        nc = NumberContainers()
        assert nc.find(10) == -1
        nc.change(2, 10)
        nc.change(1, 10)
        nc.change(3, 10)
        nc.change(5, 10)
        assert nc.find(10) == 1
        nc.change(1, 20)
        assert nc.find(10) == 2


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
