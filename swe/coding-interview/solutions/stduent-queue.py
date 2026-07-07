"""
Problem:
https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

Pattern:
- Queue

Complexity:
- Time: O(N^2) — In the worst case, we might rotate the queue of size N up to N times for each sandwich.
- Space: O(N) — Requiring auxiliary space to convert the students list into a `deque`.

Insight:
This problem simulates a queue-stack matching process with a specific gridlock condition: if the top sandwich matches no one currently in the queue, the simulation halts. By tracking a rotation counter (`cnt`), we can detect when a full loop has occurred without any match. If a match is found, the sandwich is consumed, the queue shrinks, and the rotation reset condition triggers.

Review:
- **Loop Termination Condition:** The condition `while cnt < N` is the silver bullet of this simulation. It counts how many times students have skipped the current sandwich. If `cnt` reaches the current size of the queue, it mathematically proves that none of the remaining students prefer the top sandwich, causing an unresolvable deadlock.
- **Optimization Hint (O(N) Counter Approach):** Because students can rotate infinitely until a match happens, the *order* of students doesn't actually prevent them from eventually getting a sandwich—only the *total count* of preferences matters. We can optimize this to O(N) time and O(1) space by simply counting the number of students who want `0` and `1` (using a hash map or array of size 2) and iterating through the sandwiches until we run out of a requested type.
"""


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        N = len(students)

        res = N
        for sandwich in sandwiches:
            cnt = 0
            while cnt < N and sandwich != q[0]:
                cur = q.popleft()
                q.append(cur)
                cnt += 1

            if sandwich == q[0]:
                res -= 1
                q.popleft()
            else:
                break
        return res
