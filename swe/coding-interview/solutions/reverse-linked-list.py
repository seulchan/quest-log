"""
Problem:
https://leetcode.com/problems/reverse-linked-list/

Pattern:
- Linked List

Complexity:
- 1st Approach (Iterative): Time O(N) / Space O(1)
- 2nd Approach (Recursive): Time O(N) / Space O(N) (due to call stack)

Insight:
While the iterative approach flips pointers on the way forward using constant space, the recursive approach utilizes the implicit runtime call stack to reach the end of the list first. As the recursion unwinds backward, each node reverses its relationship with its successor (`head.next.next = head`) and severs its old forward link (`head.next = None`) to prevent cyclic loops.

Review:
- **Iterative vs Recursive Space Trade-off:** The recursive approach achieves the same O(N) time complexity but sacrifices space complexity to O(N) because it creates N activation records on the execution call stack. In a production environment with highly elongated lists, this could trigger a Stack Overflow.
- **The Magic Link Flip (`head.next.next = head`):** If node A points to node B (`head.next`), then `head.next.next` is B's next pointer. Setting `head.next.next = head` forces B to point back to A, beautifully flipping the link direction during the post-order phase.
- **Cycle Prevention:** Forgetting to set `head.next = None` at the end of each frame will leave the original head node pointing to its successor permanently, creating a disastrous 2-node infinite loop/cycle when the recursion finishes.
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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class RecursionSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead
