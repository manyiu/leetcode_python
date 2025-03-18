from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            # head, prev, prev.next = head.next, head, prev
            curr = head
            head = head.next
            curr.next = prev
            prev = curr

        return prev


class TestSolution(unittest.TestCase):
    def test_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        output = Solution().reverseList(head)
        self.assertEqual(output.val, 5)
        self.assertEqual(output.next.val, 4)
        self.assertEqual(output.next.next.val, 3)
        self.assertEqual(output.next.next.next.val, 2)
        self.assertEqual(output.next.next.next.next.val, 1)

    def test_2(self):
        head = ListNode(1, ListNode(2))
        output = Solution().reverseList(head)
        self.assertEqual(output.val, 2)
        self.assertEqual(output.next.val, 1)

    def test_3(self):
        head = None
        output = Solution().reverseList(head)
        self.assertEqual(output, None)
