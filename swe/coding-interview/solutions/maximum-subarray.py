"""
Problem:
https://leetcode.com/problems/maximum-subarray/

Pattern:
- Greedy

Complexity:
- Time: O(N) — Single pass iteration over the array of length N.
- Space: O(1) — Uses constant auxiliary space with two scalar tracking variables.

Insight:
If a contiguous subarray's sum becomes negative, adding it to subsequent elements will only decrease their total sum. Therefore, whenever `curSum` drops below zero, resetting it to `0` effectively discards the prefix and starts evaluating a new subarray starting from index `i`.

Review:
- **`curSum = max(curSum, 0)` Placement Precision:** Resetting `curSum` before adding `nums[i]` correctly ensures that negative prefix sums are discarded, while naturally handling cases where `nums[i]` itself is negative.
- **All-Negative Values Correctness:** Initializing `maxSum = nums[0]` ensures that if all elements in the array are negative (e.g., `[-3, -1, -2]`), the algorithm safely returns the maximum single negative element (`-1`) rather than `0`.
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]

        for i in range(len(nums)):
            curSum = max(curSum, 0)
            curSum += nums[i]
            maxSum = max(curSum, maxSum)

        return maxSum
