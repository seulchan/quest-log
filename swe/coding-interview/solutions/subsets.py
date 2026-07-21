"""
Problem:
https://leetcode.com/problems/subsets/

Pattern:
- Backtracking

Complexity:
- Time: O(N * 2^N) — There are 2^N total subsets for N elements. At each leaf state, creating a copy of the subset (`subset.copy()`) takes O(N) time.
- Space: O(N) — Memory used by the recursive call stack and the `subset` state array (excluding the output array `res`).

Insight:
Generating all possible subsets corresponds to traversing a **Decision Tree** of depth N, where each level represents a binary choice for element `nums[i]`: either include it or exclude it. Backtracking allows us to reuse a single dynamic array (`subset`) across all paths by restoring state via `subset.pop()` when unwinding from recursive branches.

Review:
- **`subset.copy()` Snapshot Requirement:** Appending `subset` directly without `.copy()` (or `subset[:]`) would push a mutable reference into `res`. As `subset.pop()` executes later, all elements in `res` would mutate and end up empty `[]`.
- **Decision Tree Branching:** Each step explores two distinct branches: `dfs(i+1)` with `nums[i]` added, and `dfs(i+1)` without `nums[i]`. This structural symmetry guarantees that all $2^N$ combinations are covered without duplicates.
- **Deep vs Shallow Backtracking:** Notice how this contrasts with pure DFS where scalar state variables are passed downward. Here, because we mutate a shared reference object in-place, the explicit `subset.pop()` restoration step is strictly mandatory.
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
