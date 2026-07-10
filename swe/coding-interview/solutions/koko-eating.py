"""
Problem:
https://leetcode.com/problems/koko-eating-bananas/

Pattern:
- Binary Search

Complexity:
- Time: O(N log M) — Where N is the number of piles (`len(piles)`) and M is the maximum number of bananas in a single pile (`max(piles)`). The binary search takes O(log M) steps, and each step runs a linear O(N) calculation helper.
- Space: O(1) — Only uses constant memory allocations for tracking boundaries and execution state.

Insight:
When a problem asks for a minimum or maximum optimal value under a given constraint, and the feasibility follows a monotonic property (e.g., if speed $k$ works, any speed $> k$ also works), we can application **Binary Search on Answer**. Instead of testing every speed sequentially from 1 to $10^9$ via linear search ($O(M)$), we treat the answer range as a virtual sorted array and binary split it, pulling down the execution scale dramatically.

Review:
- **Ceil Math Invariant:** The function `math.ceil(p / speed)` exactly enforces the core rule: Koko cannot jump to a new pile within the same hour. For instance, if a pile has 3 bananas and `speed = 2`, it consumes $ceil 3/2 ceil = 2$ hours entirely.
- **Convergence Guard (`lo < hi`):** Unlike standard binary search that exits immediately on a precise match via `return mid`, searching for a *minimum threshold* requires the boundaries to dynamically shrink down until they converge. Setting `hi = mid` (keeping `mid` as a viable candidate) and `lo = mid + 1` ensures the loop converges smoothly without getting trapped in an infinite cycle.
- **Upper Bound Strategy:** Setting `hi = max(piles)` is a highly optimal domain anchor. Eating any faster than the size of the largest pile provides no strategic advantage because Koko cannot eat from multiple piles during a single hour anyway.
"""

import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(speed):
            return sum(math.ceil(p / speed) for p in piles)

        lo, hi = 1, max(piles)  # answer range: 1 .. biggest pile
        while lo < hi:
            mid = (lo + hi) // 2
            if hours_needed(mid) <= h:
                hi = mid
            else:  # too slow -> must go faster
                lo = mid + 1
        return lo  # smallest feasible speed
