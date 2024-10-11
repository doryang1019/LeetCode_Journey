# Runtime 537ms
# Beats  26.54%

# Memory 30MB
# Beats 8.04%
class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left = 0
        right = len(height)-1

        while left < right:
            curr_size = (right - left) * min(height[left], height[right])
            result = max(curr_size, result)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return result
