# Runtime 131ms
# Beats 28.26%

# Memory 18.46MB
# Beats 52.65%

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        trapWater = 0
        
        # To find trapped water at the ith index 
        # Need to find maximum height on its left side and maximum height on its right side

        maxRightList = [0] * n
        maxRightList[n - 1] = height[n - 1]
        for i in range(n - 2, 1, -1):
            maxRightList[i] = max(height[i], maxRightList[i + 1])

        maxLeft = height[0]
        for i in range (1, n-1):
            maxLeft = max(height[i-1], maxLeft)
            maxRight = maxRightList[i+1]

            minOfMaxLeftRight = min(maxLeft, maxRight)
            if minOfMaxLeftRight != 0:
                water = minOfMaxLeftRight - height[i]
                trapWater += water if water > 0 else 0

        return trapWater

            