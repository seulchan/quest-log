"""
Problem:
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Pattern:
- Sliding Window

Complexity:
- Time: O(N) — Both left and right pointers (L and R) traverse the string s at most N times, leading to amortized linear time.
- Space: O(min(N, K)) — Space taken by char_set, where K is the size of the character set (e.g., 26 English letters, or up to 128 for ASCII symbols).

Insight:
A substring contains unique characters as long as no character appears more than once within the current window `[L, R]`. When `s[R]` introduces a duplicate, incrementing `L` and discarding `s[L]` from `char_set` restores uniqueness in $O(1)$ amortized steps per character.

Review:
- **Amortized O(N) Time Execution:** Every character in `s` is added to `char_set` once by `R` and removed at most once by `L`, yielding strictly $O(N)$ total operations.
- **Set Removal Order Precision:** Deleting `s[L]` sequentially in the while-loop correctly purges all characters up to and including the previous instance of the duplicate `s[R]`.
- **Empty String Guard:** Works seamlessly on empty inputs `s = ""` returning `0` because the `range(len(s))` loop body is skipped cleanly.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        char_set = set()
        longest = 0

        for R in range(len(s)):
            while s[R] in char_set:
                char_set.remove(s[L])
                L += 1
            char_set.add(s[R])
            longest = max(longest, R - L + 1)

        return longest
