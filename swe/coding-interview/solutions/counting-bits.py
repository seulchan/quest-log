"""
Problem:
https://leetcode.com/problems/counting-bits/

Pattern:
- Bit Manipulation

Complexity:
- Time: O(N log N) — Iterates from 0 to N. For each number i, bitwise right-shift checks up to log2(i) bits.
- Space: O(1) auxiliary space (excluding the output array of size N + 1).

Insight:
This solution reuses the exact same bitwise inspection logic from "Number of 1 Bits" (LeetCode 191). For every integer $i$, the algorithm isolates the Least Significant Bit using `num & 1` and shifts bits to the right (`num >>= 1`) until all active bits are processed.

Review:
- **Bitwise Logic Precision:** Uses fundamental bit operators (`&` and `>>=`) without relying on Python built-ins like `bin().count('1')`.
- **Auxiliary Space Efficiency:** Modifies the `output` array elements in-place with zero additional heap allocations ($O(1)$ memory).
"""


class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)

        for i in range(n + 1):
            num = i
            while num > 0:
                output[i] += 1 if num & 1 else 0
                num >>= 1

        return output
