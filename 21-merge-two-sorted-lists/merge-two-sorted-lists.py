# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases
        dummy = ListNode()
        current = dummy

        # Traverse both lists and link nodes in sorted order
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Append the remaining nodes (only one of the lists will have nodes left)
        if list1:
            current.next = list1
        else:
            current.next = list2

        # Return the next of dummy, which is the head of the merged list
        return dummy.next
