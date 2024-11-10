class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        leftWindow, rightWindow = 0, 0
        longestSubstring = 0
        characterDict = {}
        while rightWindow <= len(s):
            # For the last substring (including up to the last character)
            if rightWindow == len(s):
                longestSubstring = max(longestSubstring, rightWindow - leftWindow)
            else:
                currentCharacter = s[rightWindow]
                characterDict[currentCharacter] = characterDict.get(currentCharacter, 0) + 1
                
                maxOccurrence = max(characterDict.values())
                # Current window size - most frequent character > k -> window is invalid
                if rightWindow - leftWindow + 1 - maxOccurrence > k:
                    longestSubstring = max(longestSubstring, rightWindow - leftWindow)
                    leftWindow += 1
                    # leftWindow - 1: To avoid missing the first character, since rightWindow + 1 afterward
                    rightWindow = leftWindow - 1 
                    characterDict = {}  
            rightWindow += 1
        return longestSubstring