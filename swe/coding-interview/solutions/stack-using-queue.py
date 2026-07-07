"""
Problem:
https://leetcode.com/problems/implement-stack-using-queues/

Pattern:
- Queue

Complexity:
- push: O(N) — Requires rotating the entire queue so the newest element comes to the front.
- pop: O(1)
- top: O(1)
- empty: O(1)
- Space Complexity: O(N) to store N elements inside the queue.

Insight:
To implement a Stack (LIFO) using a Queue (FIFO), we must ensure that the most recently added element is always positioned at the front of the queue. By leveraging a single queue, we can achieve this during the `push` operation: append the new element, and then cyclically shift all previous `len(q) - 1` elements by popping them from the front and appending them back to the rear.

Review:
- **Push Bottleneck:** While `pop` and `top` become highly efficient O(1) operations, the trade-off is an O(N) time complexity for `push` due to the internal rotation loop. This is known as a "Push-Heavy" stack implementation.
- **Queue Rotation Mechanics:** The expression `range(len(self.q) - 1)` perfectly isolates everything *except* the newly added element, safely shifting the historical data behind the new front runner without needing secondary working memory.
- Using Python's `collections.deque` ensures that both `append` and `popleft` operations are executed in true O(1) time, preserving the intended complexity boundaries.
"""

from collections import deque


class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
