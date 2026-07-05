"""
Problem:
https://leetcode.com/problems/baseball-game/

Pattern:
- Stack

Complexity:
- Time: O(N)
- Space: O(N)

Insight:
Use a stack to keep track of the history of valid scores. Each operations ("+", "D", "C") interacts directly with the top (most recent) elements of the stack, which perfectly matches the Last-In-First-Out (LIFO) property.

Review:
- **Time Complexity:** O(N) because we iterate through the list of operations exactly once. Inside the loop, all stack operations (`append`, `pop`, and negative indexing) take O(1) constant time. Finally, `sum(stack)` takes O(N) time at the end.
- **Space Complexity:** O(N) to store the scores in the stack, where in the worst-case scenario (all integer operations), the stack size matches the number of operations.
- Using negative indices like `stack[-1]` and `stack[-2]` provides a clean, pythonic way to inspect the top elements without having to calculate explicit lengths or pop them out prematurely.
"""

from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack: List[int] = []

        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(op))

        return sum(stack)
