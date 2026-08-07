"""
Problem:
https://leetcode.com/problems/valid-palindrome/

Pattern:
- Two Pointers

Complexity:
- Time: O(N) — Single pass with left and right pointers traversing at most N characters.
- Space: O(1) — Strict constant auxiliary space without creating a new filtered string.

Insight:
Instead of creating a pre-filtered string using extra memory ($O(N)$ space), two pointers starting at opposite ends (`L` and `R`) can inspect characters in-place. Inner loops advance the pointers over invalid characters (`not isalnum()`) until valid characters meet at `L` and `R`, allowing direct case-insensitive comparison.

Review:
- **In-Place Space Optimization ($O(1)$ Memory):** Skipping invalid characters on the fly avoids allocating memory for a new string, keeping memory usage purely constant.
- **Inner Loop Boundary Guard (`L < R`):** Including `L < R` and `R > L` conditions inside the inner `while` loops prevents index out-of-bounds errors when scanning string segments that consist entirely of special characters or spaces (e.g., `"   "`).
- **Pythonic `isalnum()` Utilization:** Correctly identifies both letters and digits, satisfying the alphanumeric problem criteria.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        while L < R:
            while L < R and not s[L].isalnum():
                L += 1
            while R > L and not s[R].isalnum():
                R -= 1
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1

        return True
