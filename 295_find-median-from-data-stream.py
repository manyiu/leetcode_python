import heapq
import unittest


class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == 0 or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        else:
            return -self.maxHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


class TestMedianFinder(unittest.TestCase):

    def test_median_finder(self):
        obj = MedianFinder()
        obj.addNum(1)
        obj.addNum(2)
        assert obj.findMedian() == 1.5
        obj.addNum(3)
        assert obj.findMedian() == 2.0
        obj.addNum(4)
        assert obj.findMedian() == 2.5
        obj.addNum(5)
        assert obj.findMedian() == 3.0
        obj.addNum(6)
        assert obj.findMedian() == 3.5
        obj.addNum(7)
        assert obj.findMedian() == 4.0
        obj.addNum(8)
        assert obj.findMedian() == 4.5
        obj.addNum(9)
        assert obj.findMedian() == 5.0
        obj.addNum(10)
        assert obj.findMedian() == 5.5
        obj.addNum(11)
        assert obj.findMedian() == 6.0
        obj.addNum(12)
        assert obj.findMedian() == 6.5
        obj.addNum(13)
        assert obj.findMedian() == 7.0
        obj.addNum(14)
        assert obj.findMedian() == 7.5
        obj.addNum(15)
        assert obj.findMedian() == 8.0
        obj.addNum(16)
        assert obj.findMedian() == 8.5
        obj.addNum(17)
        assert obj.findMedian() == 9.0
        obj.addNum(18)
        assert obj.findMedian() == 9.5
        obj.addNum(19)
        assert obj.findMedian() == 10.0
        obj.addNum(20)
        assert obj.findMedian() == 10.5
        obj.addNum(21)
        assert obj.findMedian() == 11.0
        obj.addNum(22)
        assert obj.findMedian() == 11.5
        obj.addNum(23)
        assert obj.findMedian() == 12.0
        obj.addNum(24)
        assert obj.findMedian() == 12.5
        obj.addNum(25)
        assert obj.findMedian() == 13.0
        obj.addNum(26)
        assert obj.findMedian() == 13.5
