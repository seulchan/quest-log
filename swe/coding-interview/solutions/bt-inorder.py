"""
Problem:
https://leetcode.com/problems/binary-tree-inorder-traversal/

Pattern:
- Trees

Complexity:
- Time: O(N) — Every node in the binary tree is visited exactly once.
- Space: O(N) worst-case (unbalanced/skewed tree) or O(log N) average-case (balanced tree) due to the call stack frames, plus O(N) space for the result array `res`.

Insight:
Inorder traversal strictly follows the **Left Child -> Root -> Right Child** execution order. DFS naturally implements this using function recursion: descending to the leftmost leaf first, recording node values during the call stack unwind phase, and then pivoting to the right subtree.

Review:
- **BST Invariant Correlation:** If this traversal is performed on a Binary Search Tree (BST), the generated output list is mathematically guaranteed to be sorted in strictly ascending order.
- **Traversal Variants:**
  - **Preorder (Root -> Left -> Right):** Useful for cloning trees or serialization.
  - **Inorder (Left -> Root -> Right):** Useful for sorted order retrieval in BSTs.
  - **Postorder (Left -> Right -> Root):** Useful for bottom-up node deletions or evaluating expression trees.
- **Optimization Hint (Iterative with Explicit Stack):** To avoid potential stack overflow errors on ultra-deep trees, this can also be implemented iteratively using an explicit `stack` data structure: push all left nodes onto the stack in a `while` loop, pop to record the value, and then step to the right child.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)
        return res
