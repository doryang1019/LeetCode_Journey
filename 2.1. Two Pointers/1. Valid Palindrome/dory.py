# Runtime 48ms
# Beats 39.01%

# Memory 18.12MB
# Beats 17.81%
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def remove_non_alphabet(t):
            return re.sub(r'[^a-zA-Z0-9]', '', t)
        buffer = remove_non_alphabet(s).lower()
        print(buffer)
        return buffer == buffer[::-1]
