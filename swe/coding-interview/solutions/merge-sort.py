"""
Problem:
https://neetcode.io/problems/mergeSort

Pattern:
- Arrays & Hashing

Complexity:
- Time: O(N log N) — The array is split logarithmically into O(log N) levels, and at each level, a linear O(N) merge operation is performed.
- Space: O(N) — Requires auxiliary space to store temporary subarrays (`L` and `R`) during the merge phase.

Insight:
Merge sort splits the unsorted array into individual single-element arrays, which are inherently sorted by definition. It then builds back up by combining pairs of sorted subarrays. To maintain **Sorting Stability**, when two keys are equal, the element from the left subarray (`L[i]`) must take priority and be placed back into the main array first.

Review:
- **The Stability Guard Rail:** The condition `L[i].key <= R[j].key` is the linchpin of stable merge sorting. If it were changed to strict inequality `<`, elements in the right partition would cross over identical keys in the left partition, destroying the original relative chronological layout.
- **Guaranteed Logarithmic Time:** Unlike Quick Sort, which can degrade to O(N^2) under a disastrous pivot selection, Merge Sort enforces a strict mathematical midpoint division (`(s + e) // 2`). This guarantees a rigid **O(N log N) time boundary** for Best, Average, and Worst-Case scenarios.
- **Memory Overhead Cost:** The trade-off for this guaranteed time boundary is its auxiliary space profile. Slicing and allocating temporary sublists `L` and `R` requires O(N) transient memory allocations, making it less memory-friendly than in-place sorting mechanisms like Insertion Sort or Quick Sort.
"""

from typing import List


class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


class Solution:
    # Implementation of Merge Sort
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)

    def mergeSortHelper(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        if e - s + 1 <= 1:
            return pairs

        # The middle index of the array
        m = (s + e) // 2

        # Sort the left half
        self.mergeSortHelper(pairs, s, m)

        # Sort the right half
        self.mergeSortHelper(pairs, m + 1, e)

        # Merge sorted halfs
        self.merge(pairs, s, m, e)

        return pairs

    # Merge in-place
    def merge(self, arr: List[Pair], s: int, m: int, e: int) -> None:
        # Copy the sorted left & right halfs to temp arrays
        L = arr[s : m + 1]
        R = arr[m + 1 : e + 1]

        i = 0  # index for L
        j = 0  # index for R
        k = s  # index for arr

        # Merge the two sorted halfs into the original array
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # One of the halfs will have elements remaining
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
