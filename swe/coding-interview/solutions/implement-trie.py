"""
Problem:
https://leetcode.com/problems/implement-trie-prefix-tree/

Pattern:
- Trie / Trees

Complexity:
- Time:
  - `insert(word)`: O(L) — Iterates through each character in word of length L.
  - `search(word)`: O(L) — Traverses at most L nodes along the character path.
  - `startsWith(prefix)`: O(L) — Traverses at most L nodes along the prefix path.
- Space: O(N * L) — Overall memory allocated across all inserted words, where N is the total number of words and L is the average word length.

Insight:
A Trie compresses common prefixes among strings into shared tree paths. By maintaining child pointer lookups via HashMaps (`self.children`) and storing a boolean marker `self.is_end`, string insertions, full word lookups, and prefix checks are performed in time proportional to string length $O(L)$, independent of the total number of stored words.

Review:
- **`search` vs `startsWith` Distinction Precision:** Correctly checks `curr.is_end` at the end of `search()` to ensure `"app"` is not falsely reported as a full word when only `"apple"` exists in the tree.
- **HashMap Node Space Efficiency:** Utilizing a Python dictionary for `children` instead of a fixed array of size 26 dynamically allocates memory only when characters are actually encountered, optimizing memory footprint.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
