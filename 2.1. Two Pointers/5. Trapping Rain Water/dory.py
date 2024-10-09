# Runtime 122ms
# Beats 47%

# Memory 18.47MB
# Beats 51.22%
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        left_max = 0
        right_max = 0
        result = 0
        # the last element(rightest) must > 0  to be the wall, but the leftest side can be 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(height[left], left_max)
                result = left_max - height[left] + result if left_max >= height[left] else result
                left += 1
            else:
                right_max = max(height[right], right_max)
                result = right_max - height[right] + result if right_max >= height[right] else result
                right -= 1

        return result
