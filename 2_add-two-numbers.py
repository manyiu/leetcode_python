from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        curr = dummy

        while l1 or l2 or carry > 0:
            a, b = 0, 0

            if l1:
                a = l1.val
                l1 = l1.next

            if l2:
                b = l2.val
                l2 = l2.next

            sum = a + b + carry
            digit = sum % 10
            carry = sum // 10

            curr.next = ListNode(digit)
            curr = curr.next

        return dummy.next


class TestAddTwoNumbers(unittest.TestCase):
    def test_add_two_numbers(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual(result.val, 7)
        self.assertEqual(result.next.val, 0)
        self.assertEqual(result.next.next.val, 8)
        self.assertIsNone(result.next.next.next)
