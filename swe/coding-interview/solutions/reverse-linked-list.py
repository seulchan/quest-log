"""
Problem:
https://leetcode.com/problems/reverse-linked-list/

Pattern:
- Linked List

Complexity:
- Time: O(N)
- Space: O(1)

Insight:
Reverse a singly linked list in-place by maintaining three pointers: `prev` (the already reversed list), `curr` (the current node being processed), and a temporary `temp` pointer. At each step, isolate the rest of the list by saving `curr.next`, flip the current node's pointer backwards to point to `prev`, and shift both `prev` and `curr` forward.

Review:
- **Time Complexity:** O(N) because we visit each of the N nodes exactly once during the single-pass iteration.
- **Space Complexity:** O(1) auxiliary space, as the reversal is performed entirely in-place by changing pointer references without allocating new nodes.
- **Pointer Synchronization:** The order of updating pointers inside the `while` loop is critical. `curr.next` must be saved *before* it is overwritten, and `prev` must move to `curr` *before* `curr` jumps to the next node (`temp`).
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
