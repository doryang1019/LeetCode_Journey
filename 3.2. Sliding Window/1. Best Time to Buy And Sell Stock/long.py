# Runtime 108ms
# Beats 39.72%

# Memory 25.97MB
# Beats 91.56%

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        leftWindow, rightWindow = 0, 1
        
        while rightWindow < len(prices):
            if prices[leftWindow] > prices[rightWindow]: # Find minimum
                leftWindow = rightWindow
            else:
                maxProfit = max(maxProfit, prices[rightWindow] - prices[leftWindow])
            rightWindow += 1

        return maxProfit