"""
Problem:
https://leetcode.com/problems/combination-sum/

Pattern:
- Backtracking

Complexity:
- Time: O(2^T) — Where T is target / min(candidates). In the worst-case scenario, the decision tree height scales with the target value.
- Space: O(T) — Maximum recursive stack depth proportional to target divided by the smallest candidate value (excluding output array space).

Insight:
This problem models a Decision Tree with two branches at each step:
1. **Reuse Choice:** Add the current candidate `candidates[i]` and recurse with index `i` (unlimited selection).
2. **Skip Choice:** Skip `candidates[i]` entirely and recurse with index `i + 1`.

Because candidates are positive integers ($>= 2$), `total > target` acts as an effective **Pruning Boundary**, stopping hopeless recursive branches early.

Review:
- **Same Index Re-entry (`i` vs `i + 1`):** The distinction between `dfs(i, ...)` and `dfs(i + 1, ...)` handles the "unlimited use" requirement while preventing duplicate combination permutations (e.g., getting both `[2, 2, 3]` and `[3, 2, 2]`).
- **Pruning Boundary Guarantee:** Since all values in `candidates` are strictly positive integers, `total` is monotonically increasing. Once `total > target`, it is mathematically impossible to reach `target` down that branch.
- **Copy Invariant:** Just like Subsets, appending `curr.copy()` guarantees that mutable list updates during backtracking won't alter historical results already stored inside `res`.
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if target == total:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])

            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res
