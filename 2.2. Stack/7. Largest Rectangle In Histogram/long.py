# Runtime 146ms
# Beats 100.00%

# Memory 34.47MB
# Beats 13.59%

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        lastHeight = 0
        stack = []
        for i in range(len(heights)):
            height = heights[i]
            if height >= lastHeight: # Put to stack only if we can extend to the right
                stack.append((i, height))
            else: # If not, calculate its area to the left
                while stack and stack[-1][1] > height: # stack[-1][1]: height to the top element
                    # Remove the element if it can extend to the left and can't extend to the right
                    lastIndex, previousHeight = stack.pop() 
                    maxArea = max(maxArea, (i - lastIndex) * previousHeight)
                stack.append((lastIndex, height))

            lastHeight = height # Update the height of the last bar in stack

        while stack: # Calculate area for remaining elements in the stack
            startingIndex, previousHeight = stack.pop() 
            maxArea = max(maxArea, (len(heights) - startingIndex) * previousHeight)

        return maxArea