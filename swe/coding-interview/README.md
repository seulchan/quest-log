# Coding Interview

AI can generate code. Engineers build understanding. This repository is a record of strengthening the software engineering fundamentals that remain essential in the AI era.

---

## Progress

**Solved:** `3` Problems

---

## Algorithmic Patterns

| Algorithmic Pattern     | Solved |
| ----------------------- | -----: |
| Arrays & Hashing        |      2 |
| Two Pointers            |      1 |
| Sliding Window          |      0 |
| Stack                   |      0 |
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

### Two Pointers

- [x] [Remove Element](./solutions/max-consecutive-ones.py)
  - **Insight:** Use a forward-moving write pointer to overwrite unwanted elements in place. Traverse the array in a single pass and only write elements that do not match the target value.
  - **Complexity:** Time $O(N)$ / Space $O(1)$

---

## Principles

- **Build fundamentals.**
- **Reason rigorously.**
- **Recognize patterns.**
- **Communicate clearly.**
