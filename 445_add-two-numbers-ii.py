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
        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        result = None
        carry = 0

        while stack1 or stack2 or carry:
            a, b = 0, 0

            if stack1:
                a = stack1.pop()

            if stack2:
                b = stack2.pop()

            sum = a + b + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            newNode.next = result
            result = newNode

        return result


class TestAddTwoNumbers(unittest.TestCase):
    def test_add_two_numbers(self):
        l1 = ListNode(7)
        l1.next = ListNode(2)
        l1.next.next = ListNode(4)
        l1.next.next.next = ListNode(3)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual(result.val, 7)
        self.assertEqual(result.next.val, 8)
        self.assertEqual(result.next.next.val, 0)
        self.assertEqual(result.next.next.next.val, 7)
        self.assertIsNone(result.next.next.next.next)

        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual(result.val, 8)
        self.assertEqual(result.next.val, 0)
        self.assertEqual(result.next.next.val, 7)
        self.assertIsNone(result.next.next.next)

        l1 = ListNode(0)
        l2 = ListNode(0)
        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual(result.val, 0)
        self.assertIsNone(result.next)

        l1 = ListNode(9)
        l1.next = ListNode(9)
        l1.next.next = ListNode(9)
        l1.next.next.next = ListNode(9)
        l1.next.next.next.next = ListNode(9)
        l1.next.next.next.next.next = ListNode(9)
        l1.next.next.next.next.next.next = ListNode(9)
        l2 = ListNode(9)
        l2.next = ListNode(9)
        l2.next.next = ListNode(9)
        l2.next.next.next = ListNode(9)
        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 0)
        self.assertEqual(result.next.next.val, 0)
        self.assertEqual(result.next.next.next.val, 0)
        self.assertEqual(result.next.next.next.next.val, 9)
        self.assertEqual(result.next.next.next.next.next.val, 9)
        self.assertEqual(result.next.next.next.next.next.next.val, 9)
        self.assertEqual(result.next.next.next.next.next.next.next.val, 8)
