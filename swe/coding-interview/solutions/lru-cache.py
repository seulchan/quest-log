"""
Problem:
https://leetcode.com/problems/lru-cache/

Pattern:
- Hashing

Complexity:
- Time: O(1) for both `get` and `put` operations — Hash table lookups and pointer reassignment in `OrderedDict` take strict O(1) time.
- Space: O(capacity) — Memory overhead required to store up to `capacity` key-value pairs inside the cache structure.

Insight:
An LRU Cache dynamically tracks usage age to determine which entry to evict upon capacity overflow. Combining a **Hash Map** (for O(1) key-to-node indexing) with a **Doubly Linked List** (for O(1) arbitrary node insertion, deletion, and relocation) satisfies all operational time bounds. Python's `OrderedDict` acts as a battle-tested wrapper around this exact hybrid structure.

Review:
- **`move_to_end` Efficiency:** In standard lists, moving an item to the end takes O(N) due to array re-indexing. Because `OrderedDict` maintains internal pointers of a doubly linked list, `move_to_end` updates head/tail references in strict O(1) time.
- **`popitem(last=False)` Invariant:** Setting `last=False` forces removal from the left side (head) of the internal doubly linked list, which represents the LRU (Least Recently Used) boundary.
- **Low-Level Implementation Context:** In coding interviews, interviewers sometimes explicitly ask to implement LRU Cache **without built-in `OrderedDict`**. In those cases, you would manually define a `Node` class with `prev` and `next` pointers, along with dummy `head` and `tail` sentinel nodes.
"""

from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
