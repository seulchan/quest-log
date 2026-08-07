"""
Problem:
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Pattern:
- Two Pointers

Complexity:
- Time: O(N) — Single pass with left and right pointers traversing at most N elements until target sum is met.
- Space: O(1) — Strict constant auxiliary space satisfying the problem's strict memory constraint.

Insight:
Sorting guarantees monotonicity: increasing `L` strictly increases or maintains `cur_sum`, while decreasing `R` strictly decreases or maintains `cur_sum`. This property allows us to systematically eliminate invalid candidate pairs from both ends in $O(1)$ time per step without needing a Hash Map ($O(N)$ space).

Review:
- **1-Indexed Return Precision:** Correctly adds `1` to 0-indexed positions `L` and `R` (`[L + 1, R + 1]`) to comply with the problem specification.
- **Strict O(1) Space Guarantee:** Unlike standard Two Sum (LeetCode 1) which utilizes a Hash Map, exploiting array order achieves constant extra space ($O(1)$ memory).
- **Exact Single Solution Guarantee:** Because the problem guarantees exactly one valid solution exists, the loop cleanly terminates at the `else` branch without requiring out-of-loop fallback handling.
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1

        while L < R:
            cur_sum = numbers[L] + numbers[R]

            if cur_sum < target:
                L += 1
            elif cur_sum > target:
                R -= 1
            else:
                return [L + 1, R + 1]
