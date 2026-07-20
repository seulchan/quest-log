"""
Problem:
https://leetcode.com/problems/balanced-binary-tree/

Pattern:
- Trees

Complexity:
- Time: O(N) — Every node in the binary tree is visited exactly once in a post-order traversal.
- Space: O(H) — Auxiliary call stack space proportional to the height of the tree (O(N) worst-case for a skewed tree, O(log N) for a balanced tree).

Insight:
A naive approach calculates subtree heights separately for each node, leading to a redundant $O(N^2)$ complexity. By adopting a **Bottom-Up Post-Order Traversal** (`Left -> Right -> Root`), we pass height information upward alongside the balance status. If any subtree fails the balance condition (`abs(left_height - right_height) <= 1`), that failure flag propagates directly to the root, guaranteeing an optimal $O(N)$ runtime.

Review:
- **Avoid Repeated Work:** Returning a dual-value tuple/list (`[balanced, height]`) is a classic dynamic programming-like pattern on trees. It eliminates redundant recalculations of tree depths.
- **Short-Circuit Optimization:** If `left[0]` is already `False`, the rest of the boolean expression (`and right[0] and ...`) short-circuits in Python, avoiding unnecessary evaluation overhead.
- **Post-Order Advantage:** Processing children before calculating the current node's state guarantees that the height calculations are accurate and complete at every step up the execution call stack.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
