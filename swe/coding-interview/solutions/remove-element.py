"""
Problem:
https://leetcode.com/problems/remove-element/

Pattern:
- Two Pointers

Complexity:
- Time: O(N)
- Space: O(1)

Insight:
Use a forward-moving write pointer to overwrite unwanted elements in place. Traverse the array in a single pass and only write elements that do not match the target value.
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        for num in nums:
            if num != val:
                nums[write] = num
                write += 1
        return write
