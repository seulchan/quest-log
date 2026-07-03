"""
Problem:
https://leetcode.com/problems/max-consecutive-ones/

Pattern:
- Arrays

Complexity:
- Time: O(N)
- Space: O(1)

Insight:
Maintain a running streak of consecutive 1s. Reset on 0 and update the maximum streak in a single pass.
"""

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        ones = 0
        for num in nums:
            if num == 1:
                ones += 1
            else:
                ones = 0

            if ones > max_ones:
                max_ones = ones

        return max_ones
