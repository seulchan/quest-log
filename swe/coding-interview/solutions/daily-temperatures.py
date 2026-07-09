"""
Problem:
https://leetcode.com/problems/daily-temperatures/

Pattern:
- Stack

Complexity:
- Time: O(N) — Each day's index is pushed onto and popped from the stack at most once.
- Space: O(N) — In the worst-case scenario (e.g., temperatures in strictly decreasing order), the stack will store all N indices.

Insight:
A brute-force approach compares each day with all subsequent days, leading to an inefficient O(N^2) time complexity. By maintaining a **Monotonic Decreasing Stack** (where elements inside the stack are ordered from highest to lowest temperatures), we defer the calculation for colder days until a warmer day "breaks" the trend. The stack tracks the *indices* rather than raw values, allowing us to instantly calculate the dynamic distance (`i - idx`) between the event and its resolution.

Review:
- **Amortized Time Boundary:** Although there is a nested `while` loop inside the `for` loop, the time complexity remains strictly linear O(N). This is because no index can be popped more than once. The total number of operations across the entire execution is capped at 2N (N pushes and at most N pops).
- **Index-over-Value Strategy:** Storing the index `i` instead of the temperature value `current_temp` inside the stack is the golden rule of monotonic stack problems. The index grants dual powers: we can look up the value via `temperatures[stack[-1]]` and compute intervals via `i - idx`.
- **The Zero Invariant:** Initializing the `ans` array with `0` serves as a built-in fallback. Any day that never encounters a warmer future temperature will simply stay in the stack or finish the loop without being popped, correctly leaving its default waiting time at `0`.
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack: List[int] = []

        for i, current_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < current_temp:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)

        return ans
