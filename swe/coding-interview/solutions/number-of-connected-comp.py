"""
Problem:
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

Pattern:
- Union-Find (Disjoint Set Union) / Graphs

Complexity:
- Time: O(V + E * α(V)) ≈ O(V + E) — Initializing DSU takes O(V) time. Processing E edges with path compression and union by rank takes amortized near-constant time per operation.
- Space: O(V) — Memory allocated for parent and rank arrays of size V inside the DSU class.

Insight:
Initially, each of the $N$ nodes forms its own isolated connected component. Every edge $[u, v]$ attempts to unite two sets. If $u$ and $v$ belong to different roots (`union` succeeds), merging them reduces the total count of connected components by exactly 1.

Review:
- **Clean Object-Oriented Encapsulation:** Separating the `DSU` helper class improves code readability and reusability for other graph-based Union-Find problems.
- **Pythonic Swap Logic (`pu, pv = pv, pu`):** Elegant rank-comparison logic simplifies attaching the smaller-ranked tree under the higher-ranked root.
- **Optimal Subtraction Logic:** Tracking decrements via `res -= 1` on valid unions avoids an additional $O(V)$ post-processing pass to count unique parent representatives.
"""


class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        curr = node

        while curr != self.parent[curr]:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]
        return curr

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for n1, n2 in edges:
            if dsu.union(n1, n2):
                res -= 1
        return res
