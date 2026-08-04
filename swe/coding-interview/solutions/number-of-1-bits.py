"""
Problem:
https://leetcode.com/problems/number-of-1-bits/

Pattern:
- Bit Manipulation

Complexity:
- Time: O(1) — Checks up to 32 bits for a 32-bit unsigned integer (or O(log2 N) loop iterations relative to value N).
- Space: O(1) — Strict constant memory usage with zero extra allocations.

Insight:
This approach counts the set bits (`1`s) by repeatedly inspecting the Least Significant Bit (LSB) using `n & 1`. Bitwise AND with `1` isolates the lowest bit, yielding `1` if set and `0` otherwise. The right-shift operator (`n >> 1`) then shifts the remaining bits down, bringing the next bit into the LSB position until `n` becomes `0`.

Review:
- **Bit Masking Precision:** Using `n & 1` directly evaluates bit status in hardware-level bitwise operations rather than converting the integer to a string.
- **Loop Termination Condition:** The `while n > 0` condition guarantees the loop terminates early as soon as all remaining high-order bits are `0`, avoiding unnecessary shifts on smaller values.
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += 1 if n & 1 else 0
            n = n >> 1
        return count
