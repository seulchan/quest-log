"""
Problem:
https://leetcode.com/problems/course-schedule/

Pattern:
- Graphs

Complexity:
- Time: O(V + E) — Where V is the number of courses (`numCourses`) and E is the number of prerequisite pairs (`prerequisites.length`). Every node and edge is processed at most once thanks to the `pre_map[crs] = []` memoization step.
- Space: O(V + E) — Memory allocated for the adjacency list `pre_map`, recursion call stack, and `visiting` set.

Insight:
Determining if all courses can be completed is equivalent to checking whether a Directed Graph contains a **Cycle**. A directed cycle indicates a deadlocked dependency chain (e.g., A needs B, B needs A). Using Depth-First Search (DFS) with a recursion stack tracker (`visiting`), encountering an already active node confirms a cycle. Clearing visited dependencies (`pre_map[crs] = []`) prevents redundant re-traversals of fully validated subgraphs.

Review:
- **Importance of `pre_map[crs] = []` Memoization:** Without clearing `pre_map[crs] = []` after validation, the algorithm would repeatedly re-evaluate shared dependencies across different starting nodes, inflating time complexity from linear $O(V + E)$ up to exponential $O(V^E)$ in dense DAGs.
- **Backtracking State Clean-up (`visiting.remove(crs)`):** Removing `crs` from `visiting` after exiting recursion ensures nodes on separate, independent branches are not falsely flagged as cycles.
- **Kahn's Algorithm (BFS Indegree Approach):** An alternative classic approach for topological sorting uses In-degrees and BFS. By enqueueing nodes with an in-degree of 0 and decrementing neighbor counts upon popping, if total processed nodes equals `numCourses`, no cycle exists.
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if pre_map[crs] == []:
                return True

            visiting.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            pre_map[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
