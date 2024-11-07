# Runtime 2990ms
# Beats 9.46%

# Memory 16.91MB
# Beats 8.08%

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start = 0
        sortedS1 = sorted(s1)
        lengthS1, lengthS2 = len(s1), len(s2)
        while start < (lengthS2 - lengthS1 + 1):
            if s2[start] in s1:
                if sorted(s2[start:start + lengthS1]) == sortedS1:
                    return True
            start += 1
        return False