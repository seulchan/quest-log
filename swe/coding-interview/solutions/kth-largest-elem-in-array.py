"""
Problem:
https://leetcode.com/problems/kth-largest-element-in-an-array/

Pattern:
- Heap / Priority Queue

Complexity:
- Time: O(N log k) — Building and maintaining a min-heap of size k across all N elements in the array.
- Space: O(k) — Memory consumed by storing the top k elements in the priority queue.

Insight:
Finding the $k$-th largest element without performing a full $O(N \log N)$ sort is a classic use case for a **Min-Heap of size k**. By maintaining a min-heap that caps its capacity at $k$, the root node always represents the smallest item among the $k$ largest elements seen so far. Once all $N$ elements are processed, the top of the heap (or index `[-1]` of `nlargest`) is precisely the $k$-th largest number.

Review:
- **`heapq.nlargest` Internal Mechanics:** Under the hood, `heapq.nlargest(k, nums)` builds a min-heap of size $k$ from the first $k$ elements ($O(k)$), then iterates through the remaining $N - k$ elements. It compares each candidate with the heap's minimum root ($O(1)$) and performs a `heappushpop` ($O(\log k)$) whenever a larger value is found, guaranteeing $O(N \log k)$ total execution time.
- **Alternative Optimization Strategy (QuickSelect - Average O(N)):** While the Min-Heap approach provides a reliable $O(N \log k)$ time boundary with $O(k)$ auxiliary space, this problem can also be tackled using **QuickSelect** (a variant of Quick Sort partitioning). QuickSelect achieves an average time complexity of **$O(N)$** and $O(1)$ space by only recursing into the single partition containing the target $k$-th index.
"""

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
