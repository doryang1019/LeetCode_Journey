# Runtime 52ms
# Beats 57.09%

# Memory 16.65MB
# Beats 60.44%

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        leftWindow = 0
        longestSubstring = 0
        characterDict = {}
        for rightWindow in range(len(s)):
            currentCharacter = s[rightWindow]
            characterDict[currentCharacter] = characterDict.get(currentCharacter, 0) + 1
            
            # Find the most occurrence character
            maxOccurrence = max(characterDict.values())
            # Current window size - most frequent character > k -> window is invalid
            # -> Need to shrink the window
            if rightWindow - leftWindow + 1 - maxOccurrence > k:
                characterDict[s[leftWindow]] -= 1  
                leftWindow += 1
                
            longestSubstring = max(longestSubstring, rightWindow - leftWindow + 1)
            
        return longestSubstring
