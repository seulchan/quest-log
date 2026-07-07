"""
Problem:
https://neetcode.io/problems/queue

Pattern:
- Queue

Complexity:
- isEmpty: O(1)
- append / appendleft: O(1) — Constant time insertion at both ends via sentinel links.
- pop / popleft: O(1) — Constant time deletion at both ends via sentinel links.
- Space Complexity: O(N) to store N elements inside the deque structure.

Insight:
Implementing a Double Ended Queue (Deque) with a Doubly Linked List provides strict O(1) performance for all boundary operations. By anchoring the data structure with two permanent sentinel nodes (`head` and `tail`), we can safely bypass structural "empty list" edge cases. Inserting or deleting elements at either extreme simplifies into a uniform four-way pointer update, isolating the mutation between a sentinel and its immediate neighbor.

Review:
- **Sentinel Robustness:** The check `self.head.next == self.tail` inside `isEmpty()` is highly declarative. It relies entirely on the structural physical reality of the sentinels rather than tracking an explicit integer size, making it less error-prone.
- **Symmetric Pointer Rewiring:** In both `append` and `pop` families, the assignments flawlessly maintain the bidirectional integrity (`next` and `prev`) of the chain. For instance, in `popleft`, bridging `self.head` directly to `first_node.next` allows Python's garbage collector to seamlessly reclaim the detached `first_node`.
- **Double-Ended Flexibitly:** Unlike standard array-based queues that suffer from an O(N) shift cost when slicing or modifying the front, this pointer-swapping mechanism guarantees that unshifting/shifting (`appendleft`/`popleft`) scales flawlessly regardless of data size.
"""


# Doubly Linked List Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


# Linked List implementation of Double Ended Queue
class Deque:
    def __init__(self):
        # Create two dummy nodes and link them
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value) -> None:
        new_node = Node(value)
        last_node = self.tail.prev

        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.tail
        self.tail.prev = new_node

    def appendleft(self, value) -> None:
        new_node = Node(value)
        first_node = self.head.next

        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = first_node
        first_node.prev = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last_node = self.tail.prev
        value = last_node.value
        prev_node = last_node.prev

        prev_node.next = self.tail
        self.tail.prev = prev_node

        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first_node = self.head.next
        value = first_node.value
        next_node = first_node.next

        self.head.next = next_node
        next_node.prev = self.head

        return value
