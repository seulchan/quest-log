"""
Problem:
https://leetcode.com/problems/range-sum-query-immutable/

Pattern:
- Arrays & Hashing / Prefix Sum

Complexity:
- Time:
  - `__init__`: O(N) — Single pass to precompute the prefix sum array of length N.
  - `sumRange`: O(1) — Direct index lookup and subtraction in constant time.
- Space: O(N) — Auxiliary memory used to store the `prefix` array of length N.

Insight:
Repeatedly summing range slice `nums[left:right+1]` for $Q$ queries takes $O(Q \cdot N)$ time, which easily causes TLE (Time Limit Exceeded). By precomputing a Prefix Sum array where `prefix[i] = sum(nums[0...i])`, any arbitrary range sum from index `left` to `right` reduces to $prefix[right] - prefix[left - 1]$ in $O(1)$ constant time.

Review:
- **`left == 0` Boundary Guard:** The ternary condition `self.prefix[left - 1] if left > 0 else 0` accurately handles queries starting from index 0 without causing negative indexing bugs (`prefix[-1]`).
- **Optimal Time Tradeoff:** Precomputing in $O(N)$ time allows processing up to $10^4$ subsequent `sumRange` queries in $O(1)$ time each, optimizing overall execution speed significantly.
"""


class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = []
        cur = 0
        for num in nums:
            cur += num
            self.prefix.append(cur)

    def sumRange(self, left: int, right: int) -> int:
        pre_right = self.prefix[right]
        pre_left = self.prefix[left - 1] if left > 0 else 0
        return pre_right - pre_left


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
