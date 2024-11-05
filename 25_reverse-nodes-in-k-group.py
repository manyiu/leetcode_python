from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        groupPrev = dummy

        while True:
            kth = groupPrev
            count = 0

            while kth and count < k:
                kth = kth.next
                count += 1

            if count != k or not kth:
                break

            prev = kth.next
            curr = groupPrev.next

            for _ in range(k):
                # temp = curr.next
                # curr.next = prev
                # prev = curr
                # curr = temp
                temp = curr
                curr = curr.next
                temp.next = prev
                prev = temp

            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return dummy.next


class TestSolution(unittest.TestCase):
    def test_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        k = 2
        res = Solution().reverseKGroup(head, k)
        self.assertEqual(res.val, 2)
        self.assertEqual(res.next.val, 1)
        self.assertEqual(res.next.next.val, 4)
        self.assertEqual(res.next.next.next.val, 3)
        self.assertEqual(res.next.next.next.next.val, 5)
        self.assertEqual(res.next.next.next.next.next, None)

    def test_2(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        k = 3
        res = Solution().reverseKGroup(head, k)
        self.assertEqual(res.val, 3)
        self.assertEqual(res.next.val, 2)
        self.assertEqual(res.next.next.val, 1)
        self.assertEqual(res.next.next.next.val, 4)
        self.assertEqual(res.next.next.next.next.val, 5)
        self.assertEqual(res.next.next.next.next.next, None)
