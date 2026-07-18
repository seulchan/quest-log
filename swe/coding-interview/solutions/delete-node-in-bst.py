"""
Problem:
https://leetcode.com/problems/delete-node-in-a-bst/

Pattern:
- Trees

Complexity:
- Time: O(H) — Where H is the height of the BST. This translates to O(log N) for a balanced tree and O(N) for a skewed tree. We spend O(H) to find the node and another O(H) to find the inorder successor and delete it.
- Space: O(H) — Auxiliary space required for the recursive call stack frames, proportional to the height of the tree.

Insight:
Deleting a node from a BST requires preserving the underlying binary search sorting invariant. While removing leaves or single-child nodes is straightforward (simply bypassing them by returning the non-empty child), removing a node with two children requires structural surgery. By swapping the target value with its **Inorder Successor** (the absolute next largest value in the tree), we guarantee that every node to the left remains smaller and every node to the right remains larger.

Review:
- **Successor vs Predecessor:** Your strategy uses the Inorder Successor (`minValueNode(root.right)`). An equally valid and symmetric alternative would be using the **Inorder Predecessor**—finding the maximum value in the left subtree (`maxValueNode(root.left)`) and deleting that node instead.
- **Garbage Collection Trigger:** The mechanism `return root.right` (when `not root.left`) seamlessly cuts the current node out of the tree framework. The parent node re-stitches its pointer to this returned address, allowing Python to automatically clean up the unreferenced detached node.
- **Value Overwriting Shortcut:** Instead of physically swapping node pointers and updating multiple structural boundaries when dealing with two children, overwriting `root.val = min_node.val` simplifies the process into a standard single-child deletion subproblem.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getMinNode(root):
    cur = root
    while cur and cur.left:
        cur = cur.left
    return cur


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                min_node = getMinNode(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)

        return root
