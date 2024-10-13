class Solution:
    def trap(self, height: List[int]) -> int:
        maxHeight = max(height)
        
        n = len(height)
        trapWater = 0
        for i in range(maxHeight):
            l, r = 0, n - 1
            while height[l] == 0:
                l += 1
            while height[r] == 0:
                r -= 1

            for i in range(l + 1, r):
                if height[i] == 0:
                    trapWater += 1

            height = [x - 1 if x != 0 else 0 for x in height] # Decrease water level by 1

        return trapWater
            