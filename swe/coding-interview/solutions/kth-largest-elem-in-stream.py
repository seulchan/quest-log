"""
Problem:
https://leetcode.com/problems/kth-largest-element-in-a-stream/

Pattern:
- Heap / Priority Queue

Complexity:
- Time:
  - `__init__`: O(N + (N - k) log N) where N is the length of initial `nums`. `heapify` takes O(N) linear time, and popping extra elements takes logarithmic time.
  - `add`: O(log k) — Standard `heappush` and `heappop` operation bounded by the max heap capacity $k$.
- Space: O(k) — Auxiliary memory footprint maintained inside `minHeap` to hold only the top $k$ largest values.

Insight:
To dynamically track the $k$-th largest element in a continuous data stream, holding all historical records is unnecessary and inefficient. By maintaining a **Min-Heap capped at capacity $k$**, the smallest value residing at the top (`self.minHeap[0]`) serves as the gateway threshold. Any number smaller than `self.minHeap[0]` gets discarded, while larger numbers displace the minimum, ensuring `self.minHeap[0]` always answers the $k$-th largest query in **$O(1)$ lookup time**.

Review:
- **`heapq.heappushpop` Micro-Optimization:** In the `add` method, if `len(self.minHeap) == self.k`, using `heapq.heappushpop(self.minHeap, val)` instead of separate `heappush` + `heappop` calls reduces internal pointer adjustments, resulting in slightly faster C-level execution.
- **Edge Case Protection:** Notice how the constraints specify $0 \le \text{nums.length} \le 10^4$ and $1 \le k \le \text{nums.length} + 1$. The initialization `while` loop handles empty or smaller-than-$k$ input lists seamlessly without raising index errors.
- **Space Efficiency Advantage:** Storing only $k$ values instead of $N$ values keeps space complexity strictly bounded to $O(k)$, preventing memory bloat even if the input stream receives millions of incoming `add` calls over time.
"""

import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
