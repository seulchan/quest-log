"""
Problem:
https://leetcode.com/problems/last-stone-weight/

Pattern:
- Heap / Priority Queue (Max-Heap Simulation)

Complexity:
- Time: O(N log N) — Heapify takes O(N). In each step of the loop, popping two elements and pushing one takes O(log N). There are at most N steps.
- Space: O(N) or O(1) — Mutates the negated input array or creates a transformed negative values list of size N.

Insight:
Simulating a greedy process where we repeatedly extract the two largest elements is the textbook use case for a **Priority Queue / Max-Heap**. Since Python's native `heapq` only implements a Min-Heap, multiplying all numbers by `-1` dynamically flips the structural ordering—allowing the absolute largest positive weights to float to the top as the minimum negative numbers.

Review:
- **Sign Algebra Clarity:** Since both `first` and `second` are negative numbers where `|first| >= |second|`, calculating the remaining weight `|first| - |second|` translates directly to `(-first) - (-second) = second - first` in positive space, which equals pushing `first - second` back into the negative heap.
- **Edge Guard (`stones.append(0)`):** If an even number of identical stones all cancel out (e.g., `[2, 2]`), the heap becomes completely empty (`len == 0`). Adding `0` guarantees `stones[0]` exists without needing extra `if not stones:` conditional branches.
"""

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])
