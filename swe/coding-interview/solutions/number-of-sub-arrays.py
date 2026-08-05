"""
Problem:
https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

Pattern:
- Sliding Window

Complexity:
- Time: O(N) — Single pass traversal through the array of length N.
- Space: O(1) — Uses constant auxiliary space with scalar variables.

Insight:
Instead of recomputing the sum of $k$ contiguous elements from scratch ($O(N \cdot k)$ time) or calculating float averages (`cur_sum / k >= threshold`), we maintain a running window sum (`cur_sum`) in $O(1)$ time. Pre-multiplying `threshold *= k` converts the condition into `cur_sum >= threshold`, avoiding floating-point division entirely.

Review:
- **`threshold *= k` Division Elimination:** Multiplying the threshold by $k$ before the loop transforms floating-point comparisons into integer checks, boosting performance while avoiding potential floating-point precision issues.
- **Pythonic Boolean Addition (`res += cur_sum >= threshold`):** Leverages Python's implicit boolean conversion where `True` evaluates to `1` and `False` to `0`, keeping the loop body concise and clear.
- **Single Pointer Indexing (`arr[R - k + 1]`):** Removing the leftmost element via `R - k + 1` allows managing the $k$-sized window seamlessly using only the right pointer `R`.
"""


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        res = cur_sum = 0

        for R in range(len(arr)):
            cur_sum += arr[R]
            if R >= k - 1:
                res += cur_sum >= threshold
                cur_sum -= arr[R - k + 1]

        return res
