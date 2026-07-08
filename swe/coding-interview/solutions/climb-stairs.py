"""
Problem:
https://leetcode.com/problems/climbing-stairs/

Pattern:
- 1-D Dynamic Programming

Complexity:
- Time: O(N) — Each state from 0 to n is calculated exactly once.
- Space: O(N) — Required for both the `cache` array of size N and the recursive DFS call stack.

Insight:
The problem of reaching the n-th stair breaks down into smaller subproblems: to reach stair `i`, you must come from either stair `i-1` (taking 1 step) or stair `i-2` (taking 2 steps). This recursive structure directly mimics the Fibonacci sequence pattern. By adding a memoization array (`cache`), we prune the redundant branches of the decision tree, converting an exponential O(2^N) time complexity into linear O(N).

Review:
- **Base Case Evaluation:** The base condition `return i == n` is a very clever and mathematically clean way to handle boundaries. It evaluates to `1` when a valid path hits the top exactly, and `0` when a choice overshoots the staircase limits.
- **Optimization Hint (Bottom-Up / Space O(1)):** While this Top-Down approach is optimal in time, it incurs an O(N) memory overhead due to the recursion stack. We can optimize the Space Complexity to O(1) by using a Bottom-Up iterative approach, maintaining only the last two calculated step combinations (e.g., `one, two = 1, 1`), as we only ever need the values of `i-1` and `i-2`.
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n

        def dfs(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]

        return dfs(0)
