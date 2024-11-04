from typing import List, Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        curr = res

        while True:
            minList = -1
            minVal = float("infinity")

            for i in range(len(lists)):
                if lists[i] and lists[i].val < minVal:
                    minVal = lists[i].val
                    minList = i

            if minList == -1:
                break
            else:
                lists[minList] = lists[minList].next
                curr.next = ListNode(minVal)
                curr = curr.next

        return res.next


class TestSolution(unittest.TestCase):
    def test_1(self):
        lists = [
            ListNode(1, ListNode(4, ListNode(5))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(2, ListNode(6)),
        ]
        res = Solution().mergeKLists(lists)
        self.assertEqual(res.val, 1)
        self.assertEqual(res.next.val, 1)
        self.assertEqual(res.next.next.val, 2)
        self.assertEqual(res.next.next.next.val, 3)
        self.assertEqual(res.next.next.next.next.val, 4)
        self.assertEqual(res.next.next.next.next.next.val, 4)
        self.assertEqual(res.next.next.next.next.next.next.val, 5)
        self.assertEqual(res.next.next.next.next.next.next.next.val, 6)
        self.assertEqual(res.next.next.next.next.next.next.next.next, None)

    def test_2(self):
        lists = []
        res = Solution().mergeKLists(lists)
        self.assertEqual(res, None)

    def test_3(self):
        lists = [None]
        res = Solution().mergeKLists(lists)
        self.assertEqual(res, None)

    def test_4(self):
        lists = [ListNode(0)]
        res = Solution().mergeKLists(lists)
        self.assertEqual(res.val, 0)
        self.assertEqual(res.next, None)

    def test_5(self):
        lists = [
            ListNode(1, ListNode(4, ListNode(5))),
            ListNode(1, ListNode(3, ListNode(4))),
            None,
        ]
        res = Solution().mergeKLists(lists)
        self.assertEqual(res.val, 1)
        self.assertEqual(res.next.val, 1)
        self.assertEqual(res.next.next.val, 3)
        self.assertEqual(res.next.next.next.val, 4)
        self.assertEqual(res.next.next.next.next.val, 4)
        self.assertEqual(res.next.next.next.next.next.val, 5)
        self.assertEqual(res.next.next.next.next.next.next, None)
