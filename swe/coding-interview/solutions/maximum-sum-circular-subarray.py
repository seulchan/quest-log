"""
Problem:
https://leetcode.com/problems/maximum-sum-circular-subarray/

Pattern:
- Greedy

Complexity:
- Time: O(N) — Single pass iteration over the array of length N to compute globalMax, globalMin, and total sum.
- Space: O(1) — Uses constant auxiliary space with scalar tracking variables.

Insight:
A circular maximum subarray can take two shapes:
1. A standard contiguous subarray in the middle (calculated via `globalMax`).
2. A wrapped subarray taking prefix and suffix elements. The sum of a wrapped subarray equals `Total Sum - Minimum Middle Subarray Sum` (`total - globalMin`).

By computing both standard Kadane's Maximum (`globalMax`) and Minimum (`globalMin`) during a single loop, the maximum circular sum is simply `max(globalMax, total - globalMin)`.

Review:
- **All-Negative Subarray Edge Case Handling:** The ternary condition `if globalMax > 0 else globalMax` perfectly prevents the edge case bug where an all-negative array (e.g., `[-3, -2, -3]`) calculates `total - globalMin = 0`, ensuring it correctly evaluates to `-2`.
- **Optimal Single-Pass State Tracking:** Updating `curMax`, `curMin`, `globalMax`, `globalMin`, and `total` within a single iteration keeps the run time strictly linear ($O(N)$) with minimal memory footprint ($O(1)$).
"""


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax, curMin = 0, 0
        globalMax, globalMin = nums[0], nums[0]
        total = 0

        for num in nums:
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)
            total += num
            globalMax = max(globalMax, curMax)
            globalMin = min(globalMin, curMin)

        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax
