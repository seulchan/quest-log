"""
Problem:
https://neetcode.io/problems/insertionSort

Pattern:
- Arrays & Hashing (Sorting)

Complexity:
- Time: O(N^2) — In the worst and average cases, we perform nested shifting loops. (O(N) for an already sorted array).
- Space: O(N^2) total space to store the execution history (N states, each containing N elements), or O(1) auxiliary space if excluding the output list.

Insight:
Insertion sort logically divides the array into a "sorted" partition (left) and an "unsorted" partition (right). For each element, it backtracks through the sorted section, swapping items until it arrives at its valid home. Because we only swap when `pairs[j - 1].key > pairs[j].key` (strict inequality), elements with equal keys never cross paths, preserves their original relative order, and demonstrates **Sorting Stability**.

Review:
- **Snapshot Copy Invariant:** The expression `pairs[:]` creates a new list wrapper containing references to the original `Pair` instances. Without this cloning step, every slot in `ans` would point to the exact same list address, mutating into the final fully-sorted layout at termination.
- **Adaptive Optimization:** Insertion Sort is highly dynamic. If the input data is already fully or nearly sorted, the inner `while` condition `pairs[j-1].key > pairs[j].key` evaluates immediately to false, granting a swift O(1) loop pass and an optimal **O(N) Best-Case Time Complexity**.
- **Stability Safeguard:** Pay special attention to the comparison operator `>`. Changing it to `>=` would force elements with identical keys to swap places during backtracking, instantly stripping away the algorithm's stability guarantee.
"""

from typing import List


class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        ans = []
        for i, pair in enumerate(pairs):
            j = i
            while j > 0 and pairs[j - 1].key > pairs[j].key:
                pairs[j], pairs[j - 1] = pairs[j - 1], pairs[j]
                j -= 1
            ans.append(pairs[:])
        return ans
