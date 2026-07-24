"""
Problem:
https://leetcode.com/problems/shortest-path-in-binary-matrix/

Pattern:
- Graphs (Matrix BFS / Shortest Path)

Complexity:
- Time: O(N^2) — In an N x N matrix, every cell is visited and pushed to the queue at most once. Each cell checks up to 8 neighbors.
- Space: O(N^2) — Space required for the `visit` set and BFS queue in the worst-case scenario.

Insight:
For unweighted graphs or uniform-cost matrices, **Breadth-First Search (BFS)** mathematically guarantees finding the shortest path first because it explores node distances layer-by-layer. Since diagonal movement is permitted, we expand neighbor searches in 8 directions instead of 4. Marking cells as visited upon insertion into the queue prevents redundant queue entries and memory bloat.

Review:
- **Enqueue-Time Visited Marking:** A common bug in matrix BFS is adding nodes to `visit` when popping (`popleft`). Adding them right at `q.append` ensures that adjacent cells don't push the same coordinate multiple times during the same BFS level, keeping memory footprint optimal.
- **In-Place Matrix Mutation (Space O(1)):** If modifying the input parameter is permitted, you can set `grid[nr][nc] = 1` instead of using a separate `visit` set, optimizing extra space complexity down to $O(N)$ for the queue alone.
- **Small Bug Fix (`visit = set((0, 0))`):** In standard Python, `set((0, 0))` creates a set containing a single integer `{0}` because `(0, 0)` is unpacked as an iterable tuple. It should be initialized with a list of tuples `set([(0, 0)])` or set literal `{(0, 0)}` to correctly store coordinate tuples.
"""

from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] or grid[N - 1][N - 1]:
            return -1

        q = deque([(0, 0, 1)])
        visit = set((0, 0))
        direct = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        while q:
            r, c, length = q.popleft()
            if r == N - 1 and c == N - 1:
                return length

            for dr, dc in direct:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < N
                    and 0 <= nc < N
                    and grid[nr][nc] == 0
                    and (nr, nc) not in visit
                ):
                    q.append((nr, nc, length + 1))
                    visit.add((nr, nc))

        return -1
