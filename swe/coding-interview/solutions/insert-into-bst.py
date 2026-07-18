"""
Problem:
https://leetcode.com/problems/insert-into-a-binary-search-tree/

Pattern:
- Trees

Complexity:
- Time: O(H) — Where H is the height of the BST. In the average/best case (balanced tree), it takes O(log N). In the worst case (skewed tree like a linked list), it takes O(N).
- Space: O(H) — Memory consumed by the recursive call stack framework proportional to the height of the tree.

Insight:
The defining property of a Binary Search Tree is that for any given node, all elements in its left subtree are strictly smaller, and all elements in its right subtree are strictly larger. Insertion can always be completed by traveling down the tree as a leaf node insertion. By using a recursive approach that returns the modified subtree root, we can gracefully stitch the new node to its designated parent without tracking explicit parent pointers.

Review:
- **The Stitching Return Pattern:** The expressions `root.right = self.insertIntoBST(...)` and `root.left = ...` are beautiful patterns. For existing nodes, it simply re-assigns them to themselves. For the edge base case, it captures the newly born `TreeNode(val)` and links it immediately.
- **Root-Level Edge Case Protection:** The initial `if not root:` check acts as a dual-purpose guard. It serves as the deep leaf node base case activator, and also successfully handles the edge case where the initial input tree itself is completely empty (`None`).
- **Optimization Hint (Iterative Space O(1)):** While recursion is highly readable, it scales bound to O(H) stack memory. You can optimize the space footprint to strict O(1) by using an iterative `while` loop with a trailing pointer (`curr`) to navigate down until you find the insertion window, then linking the new leaf directly.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root
