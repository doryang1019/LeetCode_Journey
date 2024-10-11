# Runtime 523ms
# Beats 75.27%

# Memory 22.18MB
# Beats 49.78%

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxAmount = 0
        l, r = 0, len(height) - 1
        while r > l:
            distance = r - l
            amount = min(height[l], height[r]) * distance
            maxAmount = max(amount, maxAmount)
            # Move the shorter edge
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxAmount