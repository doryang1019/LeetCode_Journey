# Runtime 26ms
# Beats 77.62%

# Memory 13.94MB
# Beats 26.04%

class Solution:
    def isPalindrome(self, s: str) -> bool:
        sFiltered = ''.join([c.lower() for c in s if c.isalnum()])
        return sFiltered == sFiltered[::-1]