"""
Problem:
https://leetcode.com/problems/find-pivot-index/

Pattern:
- Arrays & Hashing / Prefix Sum

Complexity:
- Time: O(N) — First pass constructs the 1-indexed prefix sum array in O(N), and the second pass checks pivot conditions in O(N).
- Space: O(N) — Auxiliary memory used to store the prefix array of size N + 1.

Insight:
The pivot index requires comparing the sum of elements strictly to its left with those strictly to its right. By building a 1-indexed prefix sum array where `prefix[k] = sum(nums[0...k-1])`, the left sum at index `i` is directly `prefix[i]` and the right sum is `prefix[N] - prefix[i+1]`. This eliminates repetitive slicing or summing in $O(1)$ lookup time per candidate index.

Review:
- **Edge Case Boundary Handling:** Initializing `prefix` with size $N + 1$ and starting with `0` handles index 0 (left edge) and index $N-1$ (right edge) naturally without requiring separate `if/else` checks for boundary cases.
- **Leftmost Guarantee:** Traversing sequentially from index `0` to `N - 1` guarantees returning the first (leftmost) valid pivot index encountered.
"""


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i + 1] = prefix[i] + nums[i]

        for i in range(N):
            left_sum = prefix[i]
            right_sum = prefix[N] - prefix[i + 1]
            if left_sum == right_sum:
                return i

        return -1
