"""
Problem:
https://leetcode.com/problems/design-browser-history/

Pattern:
- Arrays / Doubly Linked List

Complexity:
- 1st Approach (Dynamic Array with Slicing):
  - visit: O(N) due to array slicing (`self.arr[:self.cur]`)
  - back / forward: O(1) direct index access
- 2nd Approach (Doubly Linked List):
  - visit: O(1) pointer redirection
  - back / forward: O(M) where M is the number of steps

Insight:
While a dynamic array provides O(1) jumping for `back` and `forward` navigation, rewriting the history timeline during a `visit` forces an O(N) slicing operation to clear forward history. A Doubly Linked List solves this by allowing O(1) history truncation—simply dropping the old `next` pointer and pointing to the new node. However, this trade-off makes navigation linear O(M steps) as we must physically traverse the node chain.

Review:
- **Slicing Bottleneck:** In the 1st approach, `self.arr[:self.cur]` creates a new list copy, which can degrade performance if the history grows large. To achieve true O(1) for all operations using an array, you can maintain a fixed-size pointer for the maximum boundary (`right_bound`) instead of physical truncation.
- **Implicit Garbage Collection:** In the Doubly Linked List approach, when `self.cur.next` is overwritten, the old forward nodes lose their references and are automatically collected by Python's garbage collector, achieving history clearing for free.
- Boundary math checks can be simplified using Python's built-in `min()` and `max()` functions to clamp indices cleanly, as shown in the refactored 1st approach snippets.
"""


# 1st Approach
class DABrowserHistory:
    def __init__(self, homepage: str):
        self.cur = 0
        self.arr = []
        self.arr.append(homepage)

    def visit(self, url: str) -> None:
        self.cur += 1
        self.arr = self.arr[: self.cur]
        self.arr.append(url)

    def back(self, steps: int) -> str:
        if steps > self.cur:
            self.cur = 0
            return self.arr[0]
        self.cur = self.cur - steps
        return self.arr[self.cur]

    def forward(self, steps: int) -> str:
        if steps + self.cur >= len(self.arr):
            self.cur = len(self.arr) - 1
            return self.arr[self.cur]
        self.cur = self.cur + steps
        return self.arr[self.cur]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


# 2nd Approach
class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class LLBrowserHistory:
    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.cur.next = ListNode(url, self.cur)
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val
