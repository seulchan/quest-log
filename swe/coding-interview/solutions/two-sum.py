"""
Problem:
https://leetcode.com/problems/two-sum/

Pattern:
- Hashing

Complexity:
- Time: O(N) — Single pass through the array. Looking up target complements inside the `seen` hash map takes average O(1) time.
- Space: O(N) — In the worst-case scenario, storing elements in the `seen` dictionary takes O(N) auxiliary space.

Insight:
Instead of testing every pair with two nested loops ($O(N^2)$ brute force), we store previously visited numbers alongside their indices in a Hash Map. For every element $n$, its pair complement is strictly $diff = target - n$. Checking whether $diff$ exists in a hash map takes $O(1)$ constant time, reducing the total time complexity to $O(N)$.

Review:
- **One-Pass vs Two-Pass:** By checking `if diff in seen` *before* inserting `seen[n] = i`, you naturally prevent using the same element twice (e.g., handling `nums = [3, 3], target = 6` without getting `[0, 0]`).
- **Index Order Guarantee:** Since `seen[diff]` holds the index of an element seen earlier and `i` is the current index, returning `[seen[diff], i]` naturally maintains a clean ascending index pair structure.
- **Strict Single Solution Constraint:** The problem guarantees exactly one valid solution, so returning upon the first match guarantees $O(N)$ runtime without needing extra boundary or fallback checks.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i

        return None
