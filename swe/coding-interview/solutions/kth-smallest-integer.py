"""
Problem:
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Pattern:
- Trees

Complexity:
- Time: O(N) — Visits all N nodes in the tree to build the complete inorder array.
- Space: O(N) — Requires space for the recursion call stack plus the `res` array storing N elements.

Insight:
The defining characteristic of a Binary Search Tree (BST) is that performing an **Inorder Traversal (Left -> Root -> Right)** guarantees a strictly ascending sorted sequence of node values. By flattening the tree into a sorted array via DFS, the k-th smallest element directly corresponds to the item at index `k - 1`.

Review:
- **Inorder Preservation Invariant:** This solution relies entirely on the BST property. If the tree were a standard Binary Tree rather than a BST, the resulting array would not be sorted and this approach would fail.
- **Early Termination Optimization (Space & Time O(H + k)):** While gathering all nodes takes O(N) time and space, we can optimize this to **stop early** as soon as we reach the k-th element. Using an iterative stack approach (or passing a counter down the recursive calls), we can exit the traversal immediately when the visited node count hits `k`, reducing average time complexity to O(H + k) and space complexity to O(H).
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)

        return res[k - 1]
