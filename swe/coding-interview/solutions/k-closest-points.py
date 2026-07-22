"""
Problem:
https://leetcode.com/problems/k-closest-points-to-origin/

Pattern:
- Heap / Priority Queue

Complexity:
- Time: O(N + k log N) — Computing distances and `heapify` takes O(N) linear time. Popping k closest points takes O(k log N).
- Space: O(N) — Memory used to store the `min_heap` elements containing `[dist, x, y]`.

Insight:
Comparing geometric distances from the origin $(0,0)$ does not require computing actual square roots ($\sqrt{x^2 + y^2}$) because the square root function is strictly monotonic ($a > b \iff \sqrt{a} > \sqrt{b}$). Eliminating $\sqrt{\phantom{x}}$ saves significant floating-point arithmetic overhead. Transforming the list into a **Min-Heap** allows us to extract the top $k$ minimum distances sequentially in $O(k \log N)$ time.

Review:
- **Optimization Strategy 1 (Max-Heap of size K -> O(N log k)):**
  Instead of building a Min-Heap of all $N$ elements ($O(N)$ space and $O(N + k \log N)$ time), you can maintain a **Max-Heap capped at size $k$**. By pushing inverted distances (`-dist`), the largest distance in the top $k$ set stays at the root. When the heap size exceeds $k$, you pop the largest element. This drops time complexity to **$O(N \log k)$** and reduces auxiliary memory space to strictly **$O(k)$**.
- **Optimization Strategy 2 (QuickSelect -> Average O(N)):**
  Similar to Kth Largest Element, this problem can also be solved using **QuickSelect** partitioning, achieving an average time complexity of $O(N)$ and $O(1)$ auxiliary space.
"""

import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x, y in points:
            dist = (x**2) + (y**2)
            min_heap.append([dist, x, y])

        heapq.heapify(min_heap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(min_heap)
            res.append([x, y])
            k -= 1

        return res
