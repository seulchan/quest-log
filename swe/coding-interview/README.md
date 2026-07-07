# Coding Interview

AI can generate code. Engineers build understanding. This repository is a record of strengthening the software engineering fundamentals that remain essential in the AI era.

---

## Progress

**Solved:** `12` Problems

---

## Algorithmic Patterns

| Algorithmic Pattern     | Solved |
| ----------------------- | -----: |
| Arrays & Hashing        |      3 |
| Two Pointers            |      1 |
| Sliding Window          |      0 |
| Stack                   |      3 |
| Binary Search           |      0 |
| Linked List             |      5 |
| Trees                   |      0 |
| Heap / Priority Queue   |      0 |
| Backtracking            |      0 |
| Tries                   |      0 |
| Graphs                  |      0 |
| Advanced Graphs         |      0 |
| 1-D Dynamic Programming |      0 |
| 2-D Dynamic Programming |      0 |
| Greedy                  |      0 |
| Intervals               |      0 |
| Math & Geometry         |      0 |
| Bit Manipulation        |      0 |

---

## Solved Problems

### Arrays & Hashing

- [x] [Max Consecutive Ones](./solutions/max-consecutive-ones.py)
  - **Insight:** Maintain a running streak of consecutive 1s. Reset on 0 and update the maximum streak in a single pass.
  - **Complexity:** Time $O(N)$ / Space $O(1)$
- [x] [Replace Elements with Greatest Element on Right Side](./solutions/replace-elements.py)
  - **Insight:** When a problem requires finding the maximum or minimum of elements to the right, a forward (left-to-right) scan forces redundant sub-array lookups, leading to quadratic time complexity. Reversing the direction and scanning from right to left allows us to maintain a running "Suffix Maximum" in a single pass.
  - **Complexity:** Time $O(N)$ / Space $O(1)$
- [x] [Concatenation of Array](./solutions/concatenation-of-array.py)
  - **Insight:** Python provides highly optimized built-in methods like `extend()` or the `+` operator for sequence concatenation. Utilizing `nums.extend(nums)` modifies the array in-place, which is incredibly efficient as it leverages underlying C-level optimizations in Python. Alternatively, allocating a new array of size 2N and using index offsetting (`idx + N`) demonstrates a lower-level manual approach to populating duplicated blocks in a single pass.
  - **Complexity:** Time $O(N)$ / Space $O(1)$
- [ ] [Design Dynamic Array (Resizable Array)](./solutions/design-dynamic-array.py)
  - **Insight:**

### Two Pointers

- [x] [Remove Element](./solutions/max-consecutive-ones.py)
  - **Insight:** Use a forward-moving write pointer to overwrite unwanted elements in place. Traverse the array in a single pass and only write elements that do not match the target value.
  - **Complexity:** Time $O(N)$ / Space $O(1)$

### Stack

- [x] [Baseball Game](./solutions/baseball-game.py)
  - **Insight:** Use a stack to keep track of the history of valid scores. Each operations ("+", "D", "C") interacts directly with the top (most recent) elements of the stack, which perfectly matches the Last-In-First-Out (LIFO) property.
  - **Complexity:** Time $O(N)$ / Space $O(N)$
- [x] [Valid Parentheses](./solutions/valid-parentheses.py)
  - **Insight:** Use a hash map to map closing brackets to their corresponding opening brackets. As we traverse the string, we push opening brackets onto a stack. When a closing bracket is encountered, it must match the top of the stack (the most recently opened bracket). Any mismatch or leftover brackets in the stack at the end indicates an invalid sequence.
  - **Complexity:** Time $O(N)$ / Space $O(N)$
- [x] [Min Stack](./solutions/min-stack.py)
  - **Insight:** A single variable cannot track the minimum value effectively because popping the current minimum requires restoring the _previous_ minimum. To achieve O(1) for all operations, maintain a primary stack alongside a secondary `minStack`. The `minStack` stores the running minimum corresponding to each state of the primary stack, ensuring that pushing and popping keep both stacks perfectly synchronized.
  - **Complexity:** Time $O(1)$ for all operations / Space $O(N)$

### Linked List

- [x] [Design Singly Linked List](./solutions/design-singly-linked-list.py)
  - **Insight:** Introducing a tracking variable `self.size` transforms boundary validation into an O(1) operation, preventing unnecessary list traversals for out-of-bound indices. By pairing the size check with a dedicated `tail` pointer, appending elements to the end of the list (`addAtIndex` at the boundary) can bypass the traversal loop completely, jumping straight to an O(1) operational path.
- [x] [Design Doubly Linked List](./solutions/design-doubly-linked-list.py)
  - **Insight:** Upgrading to a Doubly Linked List with dual sentinel nodes (Dummy Head & Dummy Tail) significantly simplifies implementation by removing boundary checks during insertions and deletions. By maintaining a `size` property, we can optimize item lookup to run in O(N/2) time by traversing from the head if the target index is in the first half, or from the tail if it is in the second half.
- [x] [Reverse Linked List](./solutions/reverse-linked-list.py)
  - **Insight:** Reverse a singly linked list in-place by maintaining three pointers: `prev` (the already reversed list), `curr` (the current node being processed), and a temporary `temp` pointer. At each step, isolate the rest of the list by saving `curr.next`, flip the current node's pointer backwards to point to `prev`, and shift both `prev` and `curr` forward.
  - **Complexity:** Time $O(N)$ / Space $O(1)$
- [x] [Merge Two Sorted Linked Lists](./solutions/merge-two-sorted-linked-list.py)
  - **Insight:** Use a dummy node to seamlessly build the merged linked list without handling null-head edge cases. By comparing the heads of both lists at each step, append the smaller node to the merged list and advance the corresponding pointer. Once one list is exhausted, append the remaining part of the other list directly in O(1) time.
  - **Complexity:** Time $O(N + M)$ / Space $O(1)$
- [x] [Browser History](./solutions/browser-history.py)
  - **Insight:** While a dynamic array provides O(1) jumping for `back` and `forward` navigation, rewriting the history timeline during a `visit` forces an O(N) slicing operation to clear forward history. A Doubly Linked List solves this by allowing O(1) history truncation—simply dropping the old `next` pointer and pointing to the new node. However, this trade-off makes navigation linear O(M steps) as we must physically traverse the node chain.
  - **Complexity:** Time $O(1)$ for visit(), $O(min(n, steps))$ for back() and forward() / Space $O(M*N)$

---

## Principles

- **Build fundamentals.**
- **Reason rigorously.**
- **Recognize patterns.**
- **Communicate clearly.**
