"""
Problem:
https://leetcode.com/problems/guess-number-higher-or-lower/

Pattern:
- Binary Search

Complexity:
- Time: O(log N) — The range of potential hidden numbers is divided by 2 after each API call.
- Space: O(1) — Constant memory is used for range trackers (`l`, `r`, `m`).

This problem is a classic application of Binary Search modeled as an interactive game. Instead of matching an explicit index inside an array, we are searching within a virtual, implicitly sorted sequence of integers from 1 to `n`. The pre-defined `guess(m)` API functions identically to comparing a target against `nums[mid]`, guiding us on whether to search the upper half (`l = m + 1`) or the lower half (`r = m - 1`).

Review:
- **API Mapping Realization:** Understanding how to wire external feedback into internal binary branch choices is essential. Here, `res > 0` (meaning our guess was too low) directly maps to `target > nums[mid]`, telling us to advance the left pivot past the midpoint.
- **Infinite Loop Validity:** Using `while True:` is safe and efficient here because the problem constraints guarantee that the target `pick` lies strictly within the interval `[1, n]`. Thus, the `else: return m` clause is mathematically guaranteed to hit before the boundaries cross over.
- **Integer Bounds Performance:** With a constraint up to $n = 2^{31} - 1$, a linear scanner would time out instantly. Binary search thrives under these high-volume constraints, slicing down a 2-billion-count domain into a trivial maximum of 31 lookup cycles.
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while True:
            m = (l + r) // 2
            res = guess(m)
            if res > 0:
                l = m + 1
            elif res < 0:
                r = m - 1
            else:
                return m
