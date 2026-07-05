"""
Problem:
https://leetcode.com/problems/valid-parentheses/

Pattern:
- Stack

Complexity:
- Time: O(N)
- Space: O(N)

Insight:
Use a hash map to map closing brackets to their corresponding opening brackets. As we traverse the string, we push opening brackets onto a stack. When a closing bracket is encountered, it must match the top of the stack (the most recently opened bracket). Any mismatch or leftover brackets in the stack at the end indicates an invalid sequence.

Review:
- **Time Complexity:** O(N) since we process each character in the string exactly once. Lookup in the `closeToOpen` hash map and stack operations (`append`, `pop`) all run in O(1) constant time.
- **Space Complexity:** O(N) because, in the worst-case scenario (e.g., a string full of opening brackets like `((((((`), the stack will store all N characters.
- Mapping `closeToOpen` (Closing as Key, Opening as Value) simplifies the conditional logic significantly compared to mapping opening to closing, as it allows for a direct comparison with `stack[-1]`.
"""

from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack: List[str] = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
