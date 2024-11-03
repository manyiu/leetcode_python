from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        slow, fast = dummy, dummy

        for _ in range(n):
            if not fast.next:
                return ListNode()
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next


class TestSolution(unittest.TestCase):
    def test_remove_nth_from_end(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        head = Solution().removeNthFromEnd(head, 2)
        self.assertEqual(head.val, 1)
        self.assertEqual(head.next.val, 2)
        self.assertEqual(head.next.next.val, 3)
        self.assertEqual(head.next.next.next.val, 5)
        self.assertIsNone(head.next.next.next.next)
        head = Solution().removeNthFromEnd(head, 1)
        self.assertEqual(head.val, 1)
        self.assertEqual(head.next.val, 2)
        self.assertEqual(head.next.next.val, 3)
        self.assertIsNone(head.next.next.next)
        head = Solution().removeNthFromEnd(head, 3)
        self.assertEqual(head.val, 2)
        self.assertEqual(head.next.val, 3)
        self.assertIsNone(head.next.next)
        head = Solution().removeNthFromEnd(head, 2)
        self.assertEqual(head.val, 3)
        self.assertIsNone(head.next)
        head = Solution().removeNthFromEnd(head, 1)
        self.assertIsNone(head)
