"""
Problem:
https://leetcode.com/problems/binary-search/

Pattern:
- Binary Search

Complexity:
- Time: O(log N) — The search space is halved at each step.
- Space: O(1) — Uses constant iterative variables without any extra data structures.

Insight:
Linear search checks every element from scratch, resulting in an O(N) time footprint. If the input array is already **sorted**, we can leverage Binary Search. By comparing the `target` to the midpoint value (`nums[mid]`), we can discard half of the remaining elements instantly. This exponential elimination path scales incredibly well for enormous datasets.

Review:
- **Overflow Prevention Math:** The expression `mid = L + ((R - L) // 2)` is identical to `(L + R) // 2` mathematically, but it is standard best practice across programming languages. It prevents an integer overflow bug that occurs if `L + R` exceeds the maximum capacity of a standard 32-bit integer wrapper (though Python handles arbitrarily large numbers automatically, it's a stellar habit).
- **Loop Boundary Conditions:** The loop constraint `L <= R` is essential. If you omit the `=` (using `L < R`), the search framework will prematurely exit whenever the array narrows down to a single remaining candidate element, causing false negatives.
- **Strict Invariant:** Binary search has one ironclad dependency: **the input sequence must be strictly sorted**. If the array is unsorted, the binary split logic falls apart completely.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = L + ((R - L) // 2)
            if target < nums[mid]:
                R = mid - 1
            elif target > nums[mid]:
                L = mid + 1
            else:
                return mid
        return -1
