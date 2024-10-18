class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        widths = [0] * len(heights)

        # Loop through each bar in the histogram
        for i in range(len(heights)):
            # Calculate the number of bars to the left that are higher or equal to the current bar
            leftWidth = 0
            for j in range(i - 1, -1, -1):
                if heights[j] >= heights[i]:
                    leftWidth += 1
                else:
                    break

            # Calculate the number of bars to the right that are higher than the current bar
            rightWidth = 0
            for j in range(i + 1, len(heights)):
                if heights[j] > heights[i]:
                    rightWidth += 1
                else:
                    break

            # Store the total width for the current bar (including itself)
            widths[i] = leftWidth + 1 + rightWidth

        # Initialize an array to store the area of the rectangle for each bar
        areas = [0] * len(heights)

        # Calculate the area for each bar
        for i in range(len(heights)):
            areas[i] = widths[i] * heights[i]

        # Return the maximum area found
        return max(areas)