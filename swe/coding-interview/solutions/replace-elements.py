"""
Problem:
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

Pattern:
- Arrays (Suffix Max)

Complexity:
- 1st Approach (Brute Force): Time O(N^2) / Space O(1)
- 2nd Approach (Suffix Max): Time O(N) / Space O(N)
- 3rd Approach (In-place Optimal): Time O(N) / Space O(1)

Insight:
When a problem requires finding the maximum or minimum of elements to the right, a forward (left-to-right) scan forces redundant sub-array lookups, leading to quadratic time complexity. Reversing the direction and scanning from right to left allows us to maintain a running "Suffix Maximum" in a single pass.

Review:
- Avoid nested array slicing (`max(arr[i+1:])`) inside a loop whenever possible, as slicing and finding the max both take O(N) time, inadvertently creating an O(N^2) bottleneck.
- Order of operations matters in the right-to-left approach: the current `rightMax` must be assigned to the output array *before* updating `rightMax` with the current element's value. Otherwise, an element would incorrectly consider itself as part of its own right-side maximum.
- To optimize Space Complexity from O(N) to O(1), store the current element's value in a temporary variable (`current_val`) before overwriting it, allowing in-place modification of the input array.
"""

from typing import List


### 1st Approach: Brute Force (Left-to-Right Scan with Slicing)
class BruteForceSolution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i, num in enumerate(arr):
            if i == len(arr) - 1:
                arr[i] = -1
            else:
                arr[i] = max(arr[i + 1 :])
        return arr


### 2nd Approach: Optimal (Right-to-Left Scan / Suffix Max)
class SuffixMaxSolution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        rightMax = -1
        for i in range(n - 1, -1, -1):
            ans[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return ans


### 3rd Approach: In-place Optimal (Space Optimized to O(1))
class InPlaceSolution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        for i in range(len(arr) - 1, -1, -1):
            current_val = arr[i]
            arr[i] = rightMax
            rightMax = max(current_val, rightMax)
        return arr
