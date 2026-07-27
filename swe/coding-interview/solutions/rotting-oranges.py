"""
Problem:
https://leetcode.com/problems/rotting-oranges/

Pattern:
- Graphs

Complexity:
- Time: O(M * N) — Every cell in the grid is visited at most a constant number of times (enqueued/dequeued once).
- Space: O(M * N) — Queue space bounded by the grid dimensions in the worst-case scenario.

Insight:
Unlike single-source BFS starting from a single point, infection/spread processes originating from multiple centers simultaneously require a **Multi-Source BFS**. Pushing all initial rotten oranges into the queue at minute 0 guarantees that the BFS naturally expands in parallel concentric waves, calculating the exact minimum elapsed time.

Review:
- **`while fresh > 0 and q:` Guard Benefit:** Checking `fresh > 0` as a loop condition avoids incrementing `time` on the final wave when all oranges are already rotten, eliminating the need for `time - 1` adjustments at the return statement.
- **Micro-Optimization (`row in range(...)` -> Inequality Comparisons):** Replacing `row in range(len(grid))` with standard range comparisons `0 <= row < len(grid)` avoids dynamically allocating a `range` object on every inner loop check, making execution noticeably faster in Python.
- **Unreachable Isolated Oranges:** If any fresh orange is completely isolated by empty spaces (`0`), `fresh` will never reach `0`, and returning `-1` correctly catches these disconnected graph components.
"""
