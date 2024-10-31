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
            # prev, prev.next, head = head, prev, head.next
            curr = head
            head = head.next
            prev.next = prev
            curr = prev
        return prev


class TestSolution(unittest.TestCase):
    def test_1(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)

        new_head = Solution().reverseList(head)

        assert new_head.val == 5
        assert new_head.next.val == 4
        assert new_head.next.next.val == 3
        assert new_head.next.next.next.val == 2
        assert new_head.next.next.next.next.val == 1

    def test_2(self):
        head = ListNode(1)
        head.next = ListNode(2)

        new_head = Solution().reverseList(head)

        assert new_head.val == 2
        assert new_head.next.val == 1
