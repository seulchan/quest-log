"""
Problem:
https://leetcode.com/problems/max-area-of-island/

Pattern:
- Graphs (Matrix DFS / Connected Components Area)

Complexity:
- Time: O(M * N) — Every cell in the grid is visited at most twice during traversal.
- Space: O(M * N) — Stack space required for DFS recursion in the worst case (plus set space if using explicit `visit`).

Insight:
Calculating the area of connected components builds naturally on the **Number of Islands** pattern. Instead of just counting component entries, each recursive step returns `1 + sum_of_children_areas`. Returning integer totals back up the recursion stack provides the exact size of the current island, allowing `max(area, ...)` to track the peak value across all grid coordinates.

Review:
- **Additive DFS Formula:** The expression `1 + dfs(...) + dfs(...) + ...` cleanly aggregates area values without needing external global accumulator variables.
- **BFS Alternative:** Can also be implemented using iterative BFS with a queue. When popping nodes from the queue, increment a local `current_area` counter to achieve the identical result.
"""

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0

            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))

        return area
