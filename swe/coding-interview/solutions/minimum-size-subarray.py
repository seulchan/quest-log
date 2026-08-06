"""
Problem:
https://leetcode.com/problems/minimum-size-subarray-sum/

Pattern:
- Sliding Window

Complexity:
- Time: O(N) — Although there is a nested while loop, both left and right pointers (L and R) traverse the array at most N times.
- Space: O(1) — Strict constant auxiliary space with scalar variables.

Insight:
Since all array elements are positive integers ($nums[i] > 0$), expanding the right boundary `R` strictly increases `total`, and shrinking the left boundary `L` strictly decreases `total`. This monotonic property allows us to dynamically shrink the window size whenever `total >= target` to find the shortest valid length starting from `L`.

Review:
- **Amortized O(N) Time Proof:** Even though the `while` loop is nested inside the `for` loop, pointer `L` is only incremented up to $N$ times total throughout the entire execution, guaranteeing $O(N)$ linear time.
- **Ternary Guard Return (`0 if length == float("inf") else length`):** Correctly handles the edge case where the sum of all elements combined is still strictly smaller than `target`, returning `0` as specified.
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, total = 0, 0
        length = float("inf")

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                length = min(R - L + 1, length)
                total -= nums[L]
                L += 1

        return 0 if length == float("inf") else length
