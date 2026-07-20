"""
Problem:
https://leetcode.com/problems/binary-tree-right-side-view/

Pattern:
- Trees

Complexity:
- Time: O(N) — Every node in the binary tree is enqueued and dequeued exactly once.
- Space: O(W) — Maximum width of the tree, which can hold up to N/2 leaf nodes in a balanced tree, scaling to O(N).

Insight:
Looking at a binary tree from the right side means capturing the last visible node at each depth level. By performing a standard Level Order Traversal (BFS), we process nodes level by level from left to right. Storing a level-scoped reference (`rightSide`) continuously updates until the `for` loop finishes, cleanly leaving the rightmost node reference intact.

Review:
- **Left-to-Right Overwrite Invariant:** Since children are pushed in `left` then `right` order, the loop naturally processes the rightmost element at index `qLen - 1`.
- **Alternative (DFS Reverse Preorder):** This problem can also be solved using DFS with a `Right -> Left` traversal order (Root -> Right -> Left). By keeping track of the current depth, we append a node's value to `res` only when visiting that depth for the first time (`len(res) == current_depth`). This optimizes space auxiliary memory down to O(H) call stack frames.
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for _ in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res
