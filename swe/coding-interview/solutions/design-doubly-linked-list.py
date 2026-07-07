"""
Problem:
https://leetcode.com/problems/design-linked-list/

Pattern:
- Linked List

Complexity:
- get: O(N) — Optimized to O(N/2) by choosing the closest starting sentinel node.
- addAtHead: O(1)
- addAtTail: O(1)
- addAtIndex: O(N) — O(N/2) traversal via getPrev, followed by O(1) pointer updates.
- deleteAtIndex: O(N) — O(N/2) traversal via getPrev, followed by O(1) pointer updates.
- Space Complexity: O(N) total space to store N nodes.

Insight:
Upgrading to a Doubly Linked List with dual sentinel nodes (Dummy Head & Dummy Tail) significantly simplifies implementation by removing boundary checks during insertions and deletions. By maintaining a `size` property, we can optimize item lookup to run in O(N/2) time by traversing from the head if the target index is in the first half, or from the tail if it is in the second half.

Review:
- **Bidirectional Traversal Optimization:** Splitting the search logic based on `index <= self.size // 2` is an excellent touch that maximizes the architectural advantage of bidirectional references (`prev` and `next`).
- **DRY Principle (Don't Repeat Yourself):** Reusing the core `addAtIndex` logic inside `addAtHead` and `addAtTail` is highly structural and reduces duplicate pointer manipulation code, preventing subtle off-by-one errors.
- **Four-Way Pointer Updates:** When modifying a Doubly Linked List, remember that a single insertion/deletion requires modifying **four pointer references** in total (two for the new/target node, and one each for the predecessor and successor). Your assignment order flawlessly maintains these connections without dropping references.
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def getPrev(self, index: int) -> ListNode:
        if index <= self.size // 2:
            cur = self.head
            for _ in range(index):
                cur = cur.next
        else:
            cur = self.tail
            for _ in range(self.size - index + 1):
                cur = cur.prev
        return cur

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        return self.getPrev(index).next.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        node = ListNode(val)
        prev = self.getPrev(index)
        next = prev.next
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        prev = self.getPrev(index)
        cur = prev.next
        next = cur.next
        prev.next = next
        next.prev = prev
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
