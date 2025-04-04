from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # combined = ListNode(-101)
        # curr = combined

        # while list1 or list2:
        #     if not list1:
        #         curr.next = list2
        #         list2 = list2.next
        #     elif not list2:
        #         curr.next = list1
        #         list1 = list1.next
        #     elif list1.val < list2.val:
        #         curr.next = list1
        #         list1 = list1.next
        #     else:
        #         curr.next = list2
        #         list2 = list2.next
        #     curr = curr.next
        # return combined.next

        if not list1 or not list2:
            return list1 or list2

        head = None

        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        curr = head

        while list1 or list2:
            if not list1:
                curr.next = list2
                break
            elif not list2:
                curr.next = list1
                break
            elif list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        return head
