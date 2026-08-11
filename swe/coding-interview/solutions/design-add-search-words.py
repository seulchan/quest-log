"""
Problem:
https://leetcode.com/problems/design-add-and-search-words-data-structure/

Pattern:
- Trie

Complexity:
- Time:
  - `addWord(word)`: O(L) — Iterates through each character in word of length L.
  - `search(word)`:
    - Best / Average Case (without dots): O(L) — Direct path traversal in the Trie.
    - Worst Case (with wildcard dots '.'): O(26^L) — If word consists entirely of '.', DFS branches into all 26 children at each depth level. Given the problem constraint (at most 2 dots), execution speed remains fast in practice.
- Space:
  - `addWord`: O(N * L) — Overall space across all inserted words where N is total words and L is average word length.
  - `search`: O(L) — Recursion stack depth is bounded by the word length L (up to 25).

Insight:
Standard Trie search works linearly for exact matching. When wildcard character `.` is encountered, the algorithm branches using DFS to try every available child node in `curr.children`. Recursion advances to `i + 1`, successfully matching any lowercase character, and backtracks if a path fails.

Review:
- **Wildcard Branching Logic Precision:** The loop `for child in curr.children.values():` correctly skips nonexistent character paths and only explores active branches, avoiding unnecessary allocations.
- **Index Continuation (`dfs(i + 1, child)`):** Passing `i + 1` seamlessly jumps to the next character in `word` after matching the wildcard `.`.
- **Early Termination Efficiency:** Returning `True` immediately when any DFS branch succeeds prevents exploring remaining subtrees unnecessarily.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.is_end

        return dfs(0, self.root)
