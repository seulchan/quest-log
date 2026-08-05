"""
Problem:
https://leetcode.com/problems/contains-nearby-duplicate/

Pattern:
- Sliding Window

Complexity:
- Time: O(N) — Single pass through the array. Adding, removing, and looking up elements in the set takes average O(1) time.
- Space: O(min(N, k)) — The hash set stores at most k + 1 unique elements representing the current sliding window.

Insight:
The condition $|i - j| \le k$ restricts the search for duplicates to a fixed sliding window of size $k$. By maintaining a Hash Set containing elements of the current window, checking whether `nums[R]` exists inside the set takes $O(1)$ average time. When the window size exceeds $k$, removing `nums[L]` keeps the set synchronized with the moving range.

Review:
- **Optimal Space Bound:** The memory size of `result` never exceeds $k+1$, which guarantees $O(\min(N, k))$ auxiliary space complexity.
- **Order of Operations Precision:** Shrinking the window (`R - L > k`) *before* performing the `nums[R] in result` lookup ensures that elements beyond distance $k$ are excluded, preventing false positive matches.
- **Hash Map Alternative:** Another standard approach uses a Hash Map (`num -> index`), updating the last seen index of each value and checking `i - map[num] <= k`. Your sliding set approach achieves identical $O(N)$ runtime while using less memory overhead.
"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        result = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                result.remove(nums[L])
                L += 1
            if nums[R] in result:
                return True
            result.add(nums[R])

        return False
