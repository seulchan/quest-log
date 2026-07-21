"""
Problem:
https://leetcode.com/problems/binary-tree-level-order-traversal/

Pattern:
- Trees (Breadth-First Search)

Complexity:
- Time: O(N) — Every node in the binary tree is enqueued (`q.append`) and dequeued (`q.popleft`) exactly once.
- Space: O(W) — Where W is the maximum width of the tree (number of nodes at the leaves level). In the worst case of a balanced binary tree, the queue holds up to N/2 leaf nodes, scaling to O(N).

Insight:
While Depth-First Search (DFS) relies on a LIFO stack (or recursion) to explore paths vertically, **Breadth-First Search (BFS)** uses a FIFO queue to process tree levels horizontally. The critical insight for grouping nodes level-by-level is capturing `q_len = len(q)` at the beginning of each iteration. This bounds the inner `for` loop to consume only the current depth's nodes before moving on to the newly appended children of the next depth.

Review:
- **`deque` vs `list` Performance:** Using `collections.deque` gives strict O(1) time complexity for `popleft()`. Using a regular Python `list.pop(0)` would degrade the time complexity to O(N) per pop due to element shifting, inflating the total runtime to O(N^2).
- **Snapshot Isolation Pattern:** Taking `q_len` before enqueuing child nodes prevents newly pushed elements (`q.append(node.left)`) from polluting the current level's processing loop.
- **Handling Null Inputs:** Initializing the queue with `root` even when `root` is `None` is safely handled by checking `if node:` inside the loop, preventing extra edge-case checks at the beginning.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curSum):
            if not node:
                return False

            curSum += node.val
            if not node.left and not node.right:
                return curSum == targetSum

            return dfs(node.left, curSum) or dfs(node.right, curSum)

        return dfs(root, 0)
