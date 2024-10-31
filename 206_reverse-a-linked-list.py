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
