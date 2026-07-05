# Coding Interview

AI can generate code. Engineers build understanding. This repository is a record of strengthening the software engineering fundamentals that remain essential in the AI era.

---

## Progress

**Solved:** `7` Problems

---

## Algorithmic Patterns

| Algorithmic Pattern     | Solved |
| ----------------------- | -----: |
| Arrays & Hashing        |      3 |
| Two Pointers            |      1 |
| Sliding Window          |      0 |
| Stack                   |      3 |
| Binary Search           |      0 |
| Linked List             |      0 |
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

---

## Principles

- **Build fundamentals.**
- **Reason rigorously.**
- **Recognize patterns.**
- **Communicate clearly.**
