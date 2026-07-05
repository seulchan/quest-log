"""
Problem:
https://leetcode.com/problems/min-stack/

Pattern:
- Stack

Complexity:
- Time: O(1) for all operations (`push`, `pop`, `top`, `getMin`)
- Space: O(N)

Insight:
A single variable cannot track the minimum value effectively because popping the current minimum requires restoring the *previous* minimum. To achieve O(1) for all operations, maintain a primary stack alongside a secondary `minStack`. The `minStack` stores the running minimum corresponding to each state of the primary stack, ensuring that pushing and popping keep both stacks perfectly synchronized.

Review:
- **Time Complexity:** O(1) for all methods since Python's list `append()` and `pop()` operate in constant time, and we only inspect the last element (`[-1]`) without traversing the stack.
- **Space Complexity:** O(N) because the `minStack` consumes additional space proportional to the number of elements pushed, tracking the history of minimums.
- **Optimization Tip:** To save space, the `minStack` could alternatively store pairs `(min_val, count)` or only push a new minimum when `val <= minStack[-1]`. However, the implemented synchronized twin-stack approach is highly readable and less prone to edge-case bugs.
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
