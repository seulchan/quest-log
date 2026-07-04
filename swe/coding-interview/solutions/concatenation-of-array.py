"""
Problem:
https://leetcode.com/problems/concatenation-of-array/

Pattern:
- Arrays

Complexity:
- 1st Approach (Built-in Method): Time O(N) / Space O(1) auxiliary (In-place extension)
- 2nd Approach (Manual Pointer/Single Pass): Time O(N) / Space O(N) (Creating a new array)

Insight:
Python provides highly optimized built-in methods like `extend()` or the `+` operator for sequence concatenation. Utilizing `nums.extend(nums)` modifies the array in-place, which is incredibly efficient as it leverages underlying C-level optimizations in Python. Alternatively, allocating a new array of size 2N and using index offsetting (`idx + N`) demonstrates a lower-level manual approach to populating duplicated blocks in a single pass.

Review:
- **Built-in vs Manual:** The 1st approach is generally faster in Python practice due to C-level execution within `extend()`. It also avoids allocating a completely new variable structure from scratch, making it memory-efficient.
- **Assignment Chaining:** The 2nd approach showcases an elegant use of assignment chaining (`ans[idx] = ans[idx + N] = num`), which perfectly maps the element to both target destinations simultaneously without needing a second separate loop.
"""

from typing import List


### 1st Approach: Pythonic Built-in Method (`extend`)
class BuiltinSolution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums


### 2nd Approach: Manual Single-Pass Assignment
class ManualSolution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [0] * (2 * N)
        for idx, num in enumerate(nums):
            ans[idx] = ans[idx + N] = num
        return ans
