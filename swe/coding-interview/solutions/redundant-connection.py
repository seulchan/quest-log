"""
Problem:
https://leetcode.com/problems/redundant-connection/

Pattern:
- Union-Find

Complexity:
- Time: O(N * α(N)) ≈ O(N) — Iterates through N edges. Each find/union operation with path compression and rank optimization runs in near-constant amortized time O(α(N)).
- Space: O(N) — Auxiliary space allocated for parent (`par`) and rank (`rank`) arrays of size N + 1.

Insight:
A tree with $N$ nodes has exactly $N-1$ edges and no cycles. Adding 1 extra edge introduces exactly 1 cycle. Using the Disjoint Set Union (DSU) algorithm, we process edges one by one: if two nodes `n1` and `n2` already share the same root representative (`p1 == p2`), adding the edge `[n1, n2]` forms a cycle, making it the redundant edge.

Review:
- **Path Compression Efficiency (`par[p] = par[par[p]]`):** Flattens the tree structure during find operations, preventing deep recursion trees and maintaining near $O(1)$ lookup times.
- **1-Based Index Allocation (`len(edges) + 1`):** Safely handles 1-indexed node numbers without needing to adjust node values (`n1 - 1`).
- **Last Occurrence Requirement:** Processing edges sequentially from left to right naturally returns the last edge that completes the cycle, satisfying the problem specification.
"""


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]

            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
