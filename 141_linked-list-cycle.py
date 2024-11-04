from typing import Optional
import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


class TestSolution(unittest.TestCase):
    def test_hasCycle(self):
        head = ListNode(3)
        head.next = ListNode(2)
        head.next.next = ListNode(0)
        head.next.next.next = ListNode(-4)
        head.next.next.next.next = head.next
        self.assertEqual(Solution().hasCycle(head), True)
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = head
        self.assertEqual(Solution().hasCycle(head), True)
        head = ListNode(1)
        self.assertEqual(Solution().hasCycle(head), False)
