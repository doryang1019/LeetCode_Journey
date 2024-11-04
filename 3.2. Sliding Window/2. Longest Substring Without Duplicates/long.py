# Runtime 348ms
# Beats 5.63%

# Memory 16.64MB
# Beats 61.92%

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: # Empty string
            return 0

        longestSubstring = 1
        leftWindow, rightWindow = 0, 1
        while rightWindow < len(s):
            # If there is a duplicate
            if s[rightWindow] in s[leftWindow:rightWindow]: 
                longestSubstring = max(longestSubstring, rightWindow - leftWindow)
                leftWindow += 1
                rightWindow = leftWindow # Reset the sliding window
            
            rightWindow += 1
            if rightWindow == len(s): # End of the string (for the last substring), for examle "au"
                longestSubstring = max(longestSubstring, rightWindow - leftWindow)

        return longestSubstring
        