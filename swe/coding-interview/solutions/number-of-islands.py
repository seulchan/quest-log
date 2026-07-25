"""
Problem:
https://leetcode.com/problems/number-of-islands/

Pattern:
- Graphs

Complexity:
- Time: O(M * N) — Every cell in the grid is visited at most twice (once by the main loops and once inside the DFS traversal).
- Space: O(M * N) — Stack space required for DFS recursive calls in the worst case (e.g., a grid filled entirely with land `"1"`).

Insight:
This problem maps directly to finding the total number of **Connected Components** in an undirected graph. By mutating `grid[r][c] = "0"` upon visiting each land pixel, the algorithm "sinks" the entire island reachable from the starting cell. As a result, subsequent grid iterations will never re-trigger DFS for previously processed land cells.

Review:
- **String vs Integer Invariant:** Note that grid inputs are character strings (`"1"` and `"0"`), not integers (`1` and `0`). Your code correctly matches string types.
- **In-Place Mutation Space Advantage:** Modifying the grid in-place eliminates the $O(M \cdot N)$ memory allocation required for an explicit `visited = set()` structure.
- **BFS Alternative (Queue-Based):** The same logic can be executed using BFS with a `collections.deque`. Iterative BFS avoids the depth-limit stack overflow risk associated with Python's recursive call stack on large $M \times N$ matrices.
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            for nr, nc in directions:
                dfs(r + nr, c + nc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands
