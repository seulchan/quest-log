"""
Problem:
https://leetcode.com/problems/reverse-bits/

Pattern:
- Bit Manipulation

Complexity:
- Time: O(1) — Always executes a fixed 32 iterations for a 32-bit integer.
- Space: O(1) — Strict constant memory usage with zero extra allocations.

Insight:
Reversing a 32-bit integer requires mapping the bit at index $i$ (from the right, 0-indexed) to position $31 - i$. Right-shifting `n >> i` followed by bitwise AND `& 1` isolates the bit at position $i$. Left-shifting `bit << (31 - i)` positions this bit into its mirrored location, which is accumulated into `res`.

Review:
- **32-Bit Fixed Boundary Guarantee:** Unlike dynamic while-loops, using `range(32)` guarantees that leading zeros in the input are correctly shifted and preserved as trailing zeros in the output.
- **Operator Readability:** The combination of `(n >> i) & 1` and `bit << (31 - i)` directly mirrors the arithmetic formula for bit-position reversal.
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += bit << (31 - i)
        return res
