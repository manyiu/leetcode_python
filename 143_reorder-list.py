from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next

        while curr:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp

        slow.next = None

        head1, head2 = head, prev

        while head1 and head2:
            next1 = head1.next
            next2 = head2.next

            head1.next = head2
            head1 = next1

            head2.next = head1
            head2 = next2


class TestSolution(unittest.TestCase):
    def test_reorder_list(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        Solution().reorderList(head)
        self.assertEqual(head.val, 1)
        self.assertEqual(head.next.val, 5)
        self.assertEqual(head.next.next.val, 2)
        self.assertEqual(head.next.next.next.val, 4)
        self.assertEqual(head.next.next.next.next.val, 3)
