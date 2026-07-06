"""
Problem:
https://leetcode.com/problems/merge-two-sorted-lists/

Pattern:
- Linked List

Complexity:
- Time: O(N + M)
- Space: O(1)

Insight:
Use a dummy node to seamlessly build the merged linked list without handling null-head edge cases. By comparing the heads of both lists at each step, append the smaller node to the merged list and advance the corresponding pointer. Once one list is exhausted, append the remaining part of the other list directly in O(1) time.

Review:
- **Time Complexity:** O(N + M) where N and M are the lengths of `list1` and `list2` respectively. We traverse each node across both lists at most once.
- **Space Complexity:** O(1) because we are only rearranging the existing nodes' `next` pointers in-place rather than allocating new node structures or memory.
- Using `node.next = list1 or list2` is a clean, pythonic way to automatically splice whichever list still has remaining elements after the main loop finishes.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        node = dummy = ListNode()

        while list1 and list2:
            if list1.val > list2.val:
                node.next = list2
                list2 = list2.next
            else:
                node.next = list1
                list1 = list1.next
            node = node.next

        node.next = list1 or list2

        return dummy.next
