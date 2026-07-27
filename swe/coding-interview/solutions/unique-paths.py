"""
Problem:
https://leetcode.com/problems/unique-paths/

Pattern:
- 2D Dynamic Programming

Complexity:
- Time: O(m * n) — Each unique cell state (i, j) in the m x n grid is evaluated and cached exactly once.
- Space: O(m * n) — Memory used by the `memo` table of size m x n plus recursion stack depth up to (m + n).

Insight:
From any coordinate $(i, j)$, moving towards the target $(m-1, n-1)$ reduces to adding paths from moving right $(i, j+1)$ and down $(i+1, j)$. Because paths repeatedly overlap across branches, caching the total path count for cell $(i, j)$ inside a 2D memo table avoids exponential state re-computation.

Review:
- **Bottom-Up Tabulation Alternative ($O(m \cdot n)$ time, $O(n)$ space):**
  Instead of recursion, a 2D table can be filled iteratively where `dp[i][j] = dp[i-1][j] + dp[i][j-1]`. Since row $i$ only depends on row $i-1$, updating a single row vector of size $n$ drops auxiliary space down to $O(n)$.
- **Mathematical Combinatorics Approach ($O(m)$ time, $O(1)$ space):**
  To reach $(m-1, n-1)$ from $(0, 0)$, a robot must make exactly $(m-1)$ down moves and $(n-1)$ right moves (total $m + n - 2$ steps). The problem simplifies to choosing $(m-1)$ down moves from $(m + n - 2)$ total steps, calculated directly via combinatorics:
  $$ \binom{m + n - 2}{m - 1} = \frac{(m + n - 2)!}{(m - 1)! \cdot (n - 1)!} $$
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]

            memo[i][j] = dfs(i + 1, j) + dfs(i, j + 1)
            return memo[i][j]

        return dfs(0, 0)
