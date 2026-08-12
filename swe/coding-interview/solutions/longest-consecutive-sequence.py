"""
Problem:
https://leetcode.com/problems/longest-consecutive-sequence/

Pattern:
- Arrays & Hashing

Complexity:
- Time: O(N) — Iterates through the array of length N once. Hash map insertions and boundary key lookups take average O(1) time.
- Space: O(N) — Hash map `mp` stores at most N key-value pairs.

Insight:
Instead of relying on sorting ($O(N \log N)$) or set scanning, each number `num` acts as a bridge connecting two existing sub-sequences ending at `num - 1` and starting at `num + 1`. By tracking sequence lengths inside a hash map, adding `num` merges these sub-sequences into a single longer sequence. Updating only the new boundary endpoints (`num - left_length` and `num + right_length`) takes $O(1)$ constant time per number.

Review:
- **Duplicate Prevention Guard (`if not mp[num]`):** Safely skips duplicate numbers so already processed sequence lengths aren't mistakenly duplicated or overwritten.
- **O(1) Boundary Update Precision:** `mp[num - mp[num - 1]]` accurately targets the leftmost boundary of the left sequence, and `mp[num + mp[num + 1]]` targets the rightmost boundary of the right sequence, maintaining boundary integrity effortlessly.
- **Zero-Sorting Linear Time:** Strictly satisfies the problem's mandatory $O(N)$ runtime limit without requiring pre-sorting.
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
            res = max(res, mp[num])
        return res
