"""
Problem:
https://leetcode.com/problems/house-robber/

Pattern:
- 1D Dynamic Programming

Complexity:
- Time: O(N) — Single pass iteration over the array of houses of length N.
- Space: O(N) — Memory used by the DP array of size N (can be optimized to O(1)).

Insight:
This is a standard multi-stage decision problem with overlapping subproblems and optimal substructure. At house $i$, the choice reduces to taking $nums[i]$ and adding the optimal value from two steps prior ($dp[i-2]$), or skipping house $i$ and carrying forward $dp[i-1]$. The recurrence relation $dp[i] = \max(dp[i-1], nums[i] + dp[i-2])$ captures all state transitions.

Review:
- **Base Case Initialization:** Defining `dp[1] = max(nums[0], nums[1])` correctly handles the choice between house 0 and house 1, providing the correct foundation for index $i \ge 2$.
- **Space Complexity Optimization ($O(N) \to O(1)$):** Notice how computing `dp[i]` only depends on the previous two entries (`dp[i-1]` and `dp[i-2]`). Instead of maintaining a full length-$N$ array, you can track those state values using two scalar variables (`rob1`, `rob2`), reducing extra space to $O(1)$.
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]
