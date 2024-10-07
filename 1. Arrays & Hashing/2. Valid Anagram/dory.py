# Runtime 48ms
# Beats 61.36%

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_s = sorted(s)
        sort_t = sorted(t)
        return sort_s == sort_t
