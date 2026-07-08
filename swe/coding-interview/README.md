# Coding Interview

AI can generate code. Engineers build understanding. This repository is a record of strengthening the software engineering fundamentals that remain essential in the AI era.

---

## Progress

**Solved:** `18` Problems

---

## Algorithmic Patterns

| Algorithmic Pattern     | Solved |
| ----------------------- | -----: |
| Arrays & Hashing        |      4 |
| Two Pointers            |      1 |
| Sliding Window          |      0 |
| Stack                   |      3 |
| Binary Search           |      0 |
| Linked List             |      5 |
| Queue                   |      3 |
| Trees                   |      0 |
| Heap / Priority Queue   |      0 |
| Backtracking            |      0 |
| Tries                   |      0 |
| Graphs                  |      0 |
| Advanced Graphs         |      0 |
| 1-D Dynamic Programming |      1 |
| 2-D Dynamic Programming |      0 |
| Greedy                  |      0 |
| Intervals               |      0 |
| Math & Geometry         |      1 |
| Bit Manipulation        |      0 |

---

## Solved Problems

### Arrays & Hashing

- [x] [Design Dynamic Array (Resizable Array)](./solutions/design-dynamic-array.py)
  - **Insight:** A dynamic array achieves O(1) random access while supporting dynamic resizing. The core mechanic relies on fixed-size allocations; when the element count (`length`) reaches the allocated limits (`capacity`), a `resize()` occurs. By doubling the capacity during a resize rather than increasing it incrementally, the costly O(N) copy operations are minimized, allowing the `pushback` operation to maintain an average **O(1) Amortized** time complexity.
- [x] [Max Consecutive Ones](./solutions/max-consecutive-ones.py)
  - **Insight:** Maintain a running streak of consecutive 1s. Reset on 0 and update the maximum streak in a single pass.
  - **Complexity:** Time $O(N)$ / Space $O(1)$
- [x] [Replace Elements with Greatest Element on Right Side](./solutions/replace-elements.py)
  - **Insight:** When a problem requires finding the maximum or minimum of elements to the right, a forward (left-to-right) scan forces redundant sub-array lookups, leading to quadratic time complexity. Reversing the direction and scanning from right to left allows us to maintain a running "Suffix Maximum" in a single pass.
  - **Complexity:** Time $O(N)$ / Space $O(1)$
- [x] [Concatenation of Array](./solutions/concatenation-of-array.py)
  - **Insight:** Python provides highly optimized built-in methods like `extend()` or the `+` operator for sequence concatenation. Utilizing `nums.extend(nums)` modifies the array in-place, which is incredibly efficient as it leverages underlying C-level optimizations in Python. Alternatively, allocating a new array of size 2N and using index offsetting (`idx + N`) demonstrates a lower-level manual approach to populating duplicated blocks in a single pass.
  - **Complexity:** Time $O(N)$ / Space $O(1)$

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
  - **Insight:** While the iterative approach flips pointers on the way forward using constant space, the recursive approach utilizes the implicit runtime call stack to reach the end of the list first. As the recursion unwinds backward, each node reverses its relationship with its successor (`head.next.next = head`) and severs its old forward link (`head.next = None`) to prevent cyclic loops.
  - **Complexity:**
    - 1st Approach (Iterative): Time O(N) / Space O(1)
    - 2nd Approach (Recursive): Time O(N) / Space O(N) (due to call stack)

- [x] [Merge Two Sorted Linked Lists](./solutions/merge-two-sorted-linked-list.py)
  - **Insight:** Use a dummy node to seamlessly build the merged linked list without handling null-head edge cases. By comparing the heads of both lists at each step, append the smaller node to the merged list and advance the corresponding pointer. Once one list is exhausted, append the remaining part of the other list directly in O(1) time.
  - **Complexity:** Time $O(N + M)$ / Space $O(1)$
- [x] [Browser History](./solutions/browser-history.py)
  - **Insight:** While a dynamic array provides O(1) jumping for `back` and `forward` navigation, rewriting the history timeline during a `visit` forces an O(N) slicing operation to clear forward history. A Doubly Linked List solves this by allowing O(1) history truncation—simply dropping the old `next` pointer and pointing to the new node. However, this trade-off makes navigation linear O(M steps) as we must physically traverse the node chain.
  - **Complexity:** Time $O(1)$ for visit(), $O(min(n, steps))$ for back() and forward() / Space $O(M*N)$

### Queue

- [x] [Design Double-ended Queue](./solutions/design-double-ended-queue.py)
  - **Insight:** Implementing a Double Ended Queue (Deque) with a Doubly Linked List provides strict O(1) performance for all boundary operations. By anchoring the data structure with two permanent sentinel nodes (`head` and `tail`), we can safely bypass structural "empty list" edge cases. Inserting or deleting elements at either extreme simplifies into a uniform four-way pointer update, isolating the mutation between a sentinel and its immediate neighbor.
- [x] [Implement Stack Using Queues](./solutions/stack-using-queue.py)
  - **Insight:** To implement a Stack (LIFO) using a Queue (FIFO), we must ensure that the most recently added element is always positioned at the front of the queue. By leveraging a single queue, we can achieve this during the `push` operation: append the new element, and then cyclically shift all previous `len(q) - 1` elements by popping them from the front and appending them back to the rear.
  - **Complexity:** Time $O(N)$ for push, $O(1)$ for pop, top, empty / Space $O(N)$
- [x] [Number of Students Unable to Eat Lunch](./solutions/stduent-queue.py)
  - **Insight:** This problem simulates a queue-stack matching process with a specific gridlock condition: if the top sandwich matches no one currently in the queue, the simulation halts. By tracking a rotation counter (`cnt`), we can detect when a full loop has occurred without any match. If a match is found, the sandwich is consumed, the queue shrinks, and the rotation reset condition triggers.
  - **Complexity:** Time $O(N^2)$ / Space $O(N)$

### 1-D Dynamic Programming

- [x] [Climbing Stairs](./solutions/climb-stairs.py)
  - **Insight:** The problem of reaching the n-th stair breaks down into smaller subproblems: to reach stair `i`, you must come from either stair `i-1` (taking 1 step) or stair `i-2` (taking 2 steps). This recursive structure directly mimics the Fibonacci sequence pattern. By adding a memoization array (`cache`), we prune the redundant branches of the decision tree, converting an exponential O(2^N) time complexity into linear O(N).
  - **Complexity:** Time $O(N)$ / Space $O(N)$

### Math & Geometry

- [x] [Power of Two](./solutions/power-of-two.py)
  - **Insight:** A mathematical power of two can be reduced to the base case of 1 by continuous division by 2 without ever producing a remainder. In a recursive structure, any number that hits an odd remainder before reaching 1 (checked via `n % 2 == 1`) or drops below the valid domain (`n <= 0`) can be immediately pruned from the execution path.
  - **Complexity:** Time $O(log N)$ / Space $O(log N)$

---

## Principles

- **Build fundamentals.**
- **Reason rigorously.**
- **Recognize patterns.**
- **Communicate clearly.**
