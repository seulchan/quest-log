"""
Problem:
https://leetcode.com/problems/flood-fill/

Pattern:
- Graphs

Complexity:
- Time: O(M * N) — In the worst-case scenario where all pixels share the original color, every cell in the grid is visited once.
- Space: O(M * N) — Recursive execution stack depth can grow up to M * N in a fully connected single-color grid.

Insight:
A 2D matrix can be modeled as an implicit **Graph**, where each cell `[r, c]` represents a vertex connected to up to 4 neighboring edges. Replacing colors in connected components is equivalent to finding a connected subgraph starting from `[sr, sc]`. Changing `image[r][c] = color` directly inside the recursion serves a dual purpose: updating the pixel value while implicitly marking the cell as **visited**, avoiding the need for an extra `visited` 2D array.

Review:
- **`orig == color` Infinite Recursion Trap:** Without checking `if orig == color: return image`, a pixel whose color gets updated to `color` would still match `orig` on subsequent recursive calls, resulting in an infinite recursion stack overflow.
- **In-Place Visited Mutation:** Because we immediately update `image[r][c] = color` before neighbor exploration, `image[r][c] != orig` acts as a natural boundary filter against revisiting previously updated cells.
- **BFS Alternative:** This problem can also be solved iteratively using a queue (`collections.deque`). Both algorithms carry identical $O(M \cdot N)$ time and space bounds, though BFS avoids potential call stack depth limits on very large matrices.
"""

from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        orig = image[sr][sc]
        if orig == color:
            return image

        m, n = len(image), len(image[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != orig:
                return

            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image
