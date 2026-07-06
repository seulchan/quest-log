"""
Problem:
https://leetcode.com/problems/design-linked-list/

Pattern:
- Linked List

Complexity:
- get: O(N)
- addAtHead: O(1)
- addAtTail: O(1)
- addAtIndex: O(N)
- deleteAtIndex: O(N)
- Space Complexity: O(N) total space for storing N nodes.

Insight:
Designing a robust linked list requires precise handling of edge cases such as inserting at the boundaries (head/tail) or deleting the last node. Utilizing a dummy head node simplifies insertion and deletion routines by ensuring that a predecessor node always exists. Additionally, maintaining a `tail` pointer enables O(1) operations for appending elements to the end of the list.

Review:
- **Tail Pointer Synchronization:** When mutating the list via `addAtHead`, `addAtIndex`, or `deleteAtIndex`, it is crucial to update the `tail` pointer if the operation affects the final element (e.g., if `new_node.next` is null, it becomes the new tail; if the tail is deleted, its predecessor becomes the new tail).
- **Index Traversal:** Starting the traversal from the dummy head (`self.head`) instead of the actual first node allows the pointer to stop exactly at the `(index - 1)`th node, which is the perfect predecessor position needed for subsequent structural modifications.
"""


class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class MyLinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        idx = 0

        while curr:
            if idx == index:
                return curr.val
            idx += 1
            curr = curr.next

        return -1

    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val)
        new_head.next = self.head.next
        self.head.next = new_head
        if not new_head.next:
            self.tail = new_head

    def addAtTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def addAtIndex(self, index: int, val: int) -> None:
        idx = 0
        curr = self.head

        while curr and idx < index:
            idx += 1
            curr = curr.next

        if curr:
            new_node = ListNode(val)
            new_node.next = curr.next
            curr.next = new_node

            if not new_node.next:
                self.tail = new_node

    def deleteAtIndex(self, index: int) -> None:
        idx = 0
        curr = self.head

        while curr and idx < index:
            idx += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
