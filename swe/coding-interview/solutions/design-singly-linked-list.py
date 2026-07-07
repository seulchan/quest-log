"""
Problem:
https://leetcode.com/problems/design-linked-list/

Pattern:
- Linked List

Complexity:
- get: O(N)
- addAtHead: O(1)
- addAtTail: O(1)
- addAtIndex: O(N) — Optimized to O(1) when inserting at the tail (`index == self.size`).
- deleteAtIndex: O(N)
- Space Complexity: O(N) total space to store N nodes.

Insight:
Introducing a tracking variable `self.size` transforms boundary validation into an O(1) operation, preventing unnecessary list traversals for out-of-bound indices. By pairing the size check with a dedicated `tail` pointer, appending elements to the end of the list (`addAtIndex` at the boundary) can bypass the traversal loop completely, jumping straight to an O(1) operational path.

Review:
- **Optimal Branching:** Hijacking `addAtIndex` when `index == self.size` to call `addAtTail` is an excellent design choice that shaves off an O(N) traversal bottleneck for append actions masquerading as index insertions.
- **Tail Maintenance on Deletion:** Safely redirecting `self.tail = cur` right before executing `cur.next = cur.next.next` ensures the internal tail reference never becomes a dangling pointer when the trailing node is discarded.
- **Sentinel Robustness:** The initialized dummy head (`ListNode(-1)`) continues to anchor the structure, abstracting away empty list checks so that standard node-shifting logic applies globally across all methods.
"""


class ListNode:
    def __init__(self, val: int, next_node=None):
        self.val = val
        self.next = next_node


class MyLinkedList:
    def __init__(self):
        self.head = ListNode(-1)  # 더미 헤드
        self.tail = self.head  # tail 포인터 유지 (O(1) tail 추가용)
        self.size = 0  # size 유지 (인덱스 예외 처리용)

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val, self.head.next)
        self.head.next = new_node
        # 리스트가 비어있었다면 tail을 새 노드로 지정
        if self.tail == self.head:
            self.tail = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        # 맨 뒤에 추가하는 것이라면 O(1)로 처리
        if index == self.size:
            self.addAtTail(val)
            return

        cur = self.head
        for _ in range(index):
            cur = cur.next

        new_node = ListNode(val, cur.next)
        cur.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        cur = self.head
        for _ in range(index):
            cur = cur.next

        # 삭제할 노드가 tail이라면 tail을 이전 노드로 당김
        if cur.next == self.tail:
            self.tail = cur

        cur.next = cur.next.next
        self.size -= 1
