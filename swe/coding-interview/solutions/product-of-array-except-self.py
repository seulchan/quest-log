"""
Problem:
https://leetcode.com/problems/product-of-array-except-self/

Pattern:
- Arrays & Hashing / Prefix Sum (Prefix & Suffix Products)

Complexity:
- Time: O(N) — Three sequential passes over the array of length N (prefix accumulation, suffix accumulation, and element-wise multiplication).
- Space: O(N) — Auxiliary memory used to store the `pref` and `suff` product arrays.

Insight:
The product of all elements except `nums[i]` is equivalent to `(product of elements to the left of i) * (product of elements to the right of i)`. By constructing a prefix product array `pref` and a suffix product array `suff`, the result for index `i` is determined via `pref[i] * suff[i]` in $O(1)$ time, completely avoiding division operations.

Review:
- **No Division Constraint Satisfaction:** Directly fulfills the problem constraint prohibiting the division operator (`/`), correctly handling inputs containing single or multiple zeros (`0`).
- **Base Case Initialization:** Setting `pref[0] = 1` and `suff[N-1] = 1` cleanly accounts for boundary elements that lack left or right neighbors.
- **Index Boundary Precision:** The reverse range `range(N-2, -1, -1)` correctly computes trailing suffix products from right to left without index-out-of-bound errors.
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        pref = [0] * N
        suff = [0] * N
        res = [0] * N

        pref[0] = suff[N - 1] = 1

        for i in range(1, N):
            pref[i] = pref[i - 1] * nums[i - 1]

        for i in range(N - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]

        for i in range(N):
            res[i] = pref[i] * suff[i]

        return res
