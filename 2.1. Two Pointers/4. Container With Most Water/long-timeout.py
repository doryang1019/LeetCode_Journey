class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxAmount = 0
        n = len(height)
        for distance in range(1, n):
            l = 0
            r = l + distance 
            while r < n:
                amount = min(height[l], height[r]) * distance
                if maxAmount < amount: 
                    maxAmount = amount
                l += 1
                r += 1
        return maxAmount