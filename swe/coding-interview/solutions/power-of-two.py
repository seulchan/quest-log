"""
Problem:
https://leetcode.com/problems/power-of-two/

Pattern:
- Math & Geometry

Complexity:
- Time: O(log N) — The input number is divided by 2 at each recursive step, resulting in a logarithmic number of calls.
- Space: O(log N) — Memory allocated for the implicit recursion call stack frames proportional to the depth of the recursion.

Insight:
A mathematical power of two can be reduced to the base case of 1 by continuous division by 2 without ever producing a remainder. In a recursive structure, any number that hits an odd remainder before reaching 1 (checked via `n % 2 == 1`) or drops below the valid domain (`n <= 0`) can be immediately pruned from the execution path.

Review:
- **Base Case Strategy:** The solution relies on two distinct layers of base cases: a success anchor (`n == 1`) and an early failure filter (`n <= 0 or n % 2 == 1`). This prevents infinite recursion and handles non-positive numbers safely.
- **Logarithmic Scale:** Because the problem size halving property tracks exactly with the definition of binary logarithm ($log_2 N$), the time complexity scales incredibly efficiently, requiring at most 31 stack frames for a standard 32-bit signed integer.
- **Alternative (Bit Manipulation):** While this recursive solution sits under Math & Geometry, this problem can also be solved in the **Bit Manipulation** pattern using the expression `n > 0 and (n & (n - 1)) == 0`, which optimizes the runtime performance down to strict O(1) time and O(1) space.
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0 or n % 2 == 1:
            return False
        return self.isPowerOfTwo(n // 2)
