"""
Problem:
https://leetcode.com/problems/contains-duplicate/

Pattern:
- Arrays & Hashing

Complexity:
- Time: O(N) — Single iteration through the array. Checking membership and adding to a hash set runs in average O(1) time.
- Space: O(N) — In the worst-case scenario where all elements are unique, storing them inside the `seen` hash set requires O(N) auxiliary space.

Insight:
Detecting duplicates requires checking whether an element has been encountered previously in the sequence. A Hash Set stores unique elements and supports constant-time membership lookups ($O(1)$ average complexity). Iterating through the array once while populating the set guarantees finding duplicates in linear time $O(N)$.

Review:
- **Early Termination Advantage:** Your `for` loop checks membership before adding. If a duplicate exists early in the array (e.g., index 0 and 1), execution returns `True` immediately without processing the remaining elements.
- **Pythonic Shorthand (`len(set(nums)) < len(nums)`):** In Python, this can also be written in a single line as `return len(nums) != len(set(nums))`. While concise, converting the whole list to a set forces building the full $O(N)$ set upfront without early termination.
- **Sorting Alternative ($O(N \log N)$ Time, $O(1)$ Space):** If auxiliary memory space is strictly constrained to $O(1)$, sorting the array first allows checking adjacent elements (`nums[i] == nums[i-1]`) in linear time after an $O(N \log N)$ sort.
"""

from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
