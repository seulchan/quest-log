"""
Problem:
https://leetcode.com/problems/middle-of-the-linked-list/

Pattern:
- Two Pointers

Complexity:
- Time: O(N) — Single pass traversal over the linked list of length N (fast pointer moves twice as fast, visiting N nodes).
- Space: O(1) — Strict constant memory usage with two pointer variables.

Insight:
By advancing the `fast` pointer two nodes at a time and the `slow` pointer one node at a time, the distance between `head` and `slow` is always half the distance between `head` and `fast`. When `fast` reaches the end of the list (or `None`), `slow` naturally points to the middle node.

Review:
- **Even/Odd Node Handling:**
  - For odd node counts (e.g., 5 nodes), `fast.next` becomes `None` at node 5, leaving `slow` at node 3 (exact middle).
  - For even node counts (e.g., 6 nodes), `fast` becomes `None` past node 6, leaving `slow` at node 4 (the second middle node as required).
- **Loop Condition Robustness:** The `while fast and fast.next:` guard prevents `NoneType` attribute access errors on `fast.next.next`.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
