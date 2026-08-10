"""
Problem:
https://leetcode.com/problems/find-the-duplicate-number/

Pattern:
- Two Pointers (Fast & Slow Pointers / Floyd's Cycle Detection)

Complexity:
- Time: O(N) — Phase 1 (finding cycle collision point) and Phase 2 (finding cycle entrance) each traverse at most N steps linearly.
- Space: O(1) — Uses constant extra space with pointer variables without modifying the input array.

Insight:
Since values in `nums` range from $1$ to $n$ for an array of size $n + 1$, each element can be treated as a pointer pointing to index `nums[i]`. A duplicate value means multiple indices point to the same target index, creating a cycle in the implicit directed graph. The entrance to this cycle corresponds exactly to the duplicate number.

Review:
- **Strict Problem Constraints Satisfaction:** Satisfies all requirements by running in $O(N)$ time, $O(1)$ auxiliary memory, and leaving the original array completely unmodified.
- **Phase 1 Collision Guarantee:** Starting both pointers at index 0 and moving `slow` by 1 step (`nums[slow]`) and `fast` by 2 steps (`nums[nums[fast]]`) guarantees a collision within the cycle loop.
- **Phase 2 Mathematical Precision:** According to Floyd's algorithm, the distance from index 0 to the cycle entrance equals the distance from the Phase 1 collision point to the cycle entrance. Advancing `slow` and `slow2` at equal speed pinpoints the duplicate value seamlessly.
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
