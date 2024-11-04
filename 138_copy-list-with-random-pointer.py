import random
from typing import Optional
import unittest


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        oldToCopy = {None: None}
        curr = head

        while curr:
            if curr not in oldToCopy:
                oldToCopy[curr] = Node(curr.val)
            else:
                oldToCopy[curr].val = curr.val
            if curr.next not in oldToCopy:
                oldToCopy[curr.next] = Node(-1)
            oldToCopy[curr].next = oldToCopy[curr.next]
            if curr.random not in oldToCopy:
                oldToCopy[curr.random] = Node(-1)
            oldToCopy[curr].random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]


class TestCopyRandomList(unittest.TestCase):
    def test_copy_random_list(self):
        head = Node(7)
        head.next = Node(13)
        head.next.random = head
        head.next.next = Node(11)
        head.next.next.next = Node(10)
        head.next.next.next.random = head.next.next
        head.next.next.next.next = Node(1)
        head.next.next.random = head.next.next.next.next
        head.next.next.next.next.random = head
        head.random = None
        head = Solution().copyRandomList(head)
        self.assertEqual(head.val, 7)
        self.assertEqual(head.next.val, 13)
        self.assertEqual(head.next.random.val, 7)
        self.assertEqual(head.next.next.val, 11)
        self.assertEqual(head.next.next.random.val, 1)
        self.assertEqual(head.next.next.next.val, 10)
        self.assertEqual(head.next.next.next.random.val, 11)
        self.assertEqual(head.next.next.next.next.val, 1)
        self.assertEqual(head.next.next.next.next.random.val, 7)
        self.assertIsNone(head.next.next.next.next.next)
        self.assertIsNone(head.next.next.next.next.random.random)
