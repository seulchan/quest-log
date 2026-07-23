"""
Problem:
https://leetcode.com/problems/valid-anagram/

Pattern:
- Hashing

Complexity:
- Time: O(N) — Where N is the length of string s (and t). We traverse both strings once to build frequency counts, then compare the two hash maps in O(Sigma) time (where Sigma is the alphabet size).
- Space: O(1) or O(Sigma) — Storing frequency counts for lowercase English letters takes at most O(26) space, which simplifies to O(1) auxiliary space.

Insight:
An anagram requires two strings to contain the exact same characters with identical frequency counts, regardless of character order. Storing frequencies in a Hash Map provides $O(1)$ constant-time lookup and updates. Comparing two hash maps checks whether every character in string $s$ has a matching frequency in string $t$.

Review:
- **Follow-up Answer (Unicode Handling):** Your Hash Map implementation already handles Unicode seamlessly! Because Python dictionary keys are hashable objects, unicode code points (emojis, accented characters, foreign scripts like Korean/Vietnamese) act as standard keys without requiring fixed-size array mapping (`[0]*26`).
- **Pythonic Shorthand (`collections.Counter`):** In Python, this entire logic can be reduced to `return Counter(s) == Counter(t)`.
- **Fixed Array Alternative ($O(26)$ Memory):** If space is constrained to zero dynamic allocations for lower-case English alphabets, a fixed integer array of size 26 using ASCII offsets (`ord(char) - ord('a')`) can be used to increment/decrement counts.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        return count_s == count_t
