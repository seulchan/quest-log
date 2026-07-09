"""
Problem:
https://neetcode.io/problems/quickSort

Pattern:
- Arrays & Hashing (Divide and Conquer / Sorting)

Complexity:
- Time: O(N log N) Average/Best Case, O(N^2) Worst Case.
- Space: O(log N) Average memory consumed by the recursion stack framework, degrading to O(N) in the worst case. (In-place sorting).

Insight:
Quick Sort utilizes a Divide and Conquer paradigm driven by a core operation called **Partitioning**. Unlike Merge Sort, which splits arrays regardless of value, Quick Sort organizes elements relative to a chosen `pivot`. By shifting smaller elements to the left, the pivot naturally falls into its absolute, permanent sorted index. However, because elements can swap across large distances, Quick Sort is fundamentally **Unstable**, meaning identical keys can swap relative order (as seen in the example where `"bird"` crossed over `"cat"`).

Review:
- **In-Place Space Superiority:** Unlike Merge Sort, which demands O(N) extra memory arrays to merge slices, Quick Sort rearranges values directly within the input array wrapper (`In-place swap`). The only extra memory footprint stems from the logarithmic recursive frames on the call stack.
- **The Worst-Case Trap:** Lomuto partitioning using a fixed pivot (always selecting `arr[e]`) is highly vulnerable to sorted data. If the input array is already completely sorted or reversed, the pivot always splits an empty segment on one side, degrading performance to a catastrophic **O(N^2) Worst-Case Time Complexity**.
- **Pivot Optimization Hint:** To mitigate the worst-case scenario in real-world implementations, developers often swap `arr[e]` with a randomly selected index or the median of three elements (first, middle, last) before running the partition loop.
"""

from typing import List


class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quickSortHelper(pairs, 0, len(pairs) - 1)

    def quickSortHelper(self, pairs, s, e):
        if e - s + 1 <= 1:
            return pairs

        pivot = pairs[e]
        left = s

        for i in range(s, e):
            if pairs[i].key < pivot.key:
                tmp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = tmp
                left += 1

        pairs[e] = pairs[left]
        pairs[left] = pivot

        # Quick sort left side
        self.quickSortHelper(pairs, s, left - 1)

        # Quick sort right side
        self.quickSortHelper(pairs, left + 1, e)

        return pairs
