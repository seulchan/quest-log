"""
Problem:
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Pattern:
- Two Pointers

Complexity:
- Time: O(N) — Single pass with two pointers traversing the array of length N at most once.
- Space: O(1) — In-place modification with strict constant auxiliary space.

Insight:
Since the input array is already sorted, all duplicate values are contiguous. The right pointer `R` identifies contiguous blocks of identical values, while the left pointer `L` marks the next available slot for a unique value. Placing `nums[R]` at `nums[L]` and advancing `R` over all matching duplicates achieves in-place deduplication in $O(N)$ time.

Review:
- **In-Place Modification Precision:** Modifying `nums[L]` directly satisfies the strict memory requirement of $O(1)$ extra space without creating auxiliary arrays.
- **Inner Loop Boundary Guard (`R < N`):** Including `R < N` in the inner skip condition prevents index-out-of-bounds errors when scanning duplicates at the end of the array.
- **Return Value Clarity:** Returning `L` after the loop naturally gives the total number of unique elements $k$, matching the required 0 to $k-1$ index boundary.
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = R = 0
        N = len(nums)

        while R < N:
            nums[L] = nums[R]
            while R < N and nums[L] == nums[R]:
                R += 1
            L += 1
        return L
