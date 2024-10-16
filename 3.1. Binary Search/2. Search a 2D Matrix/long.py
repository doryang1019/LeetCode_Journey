# Runtime 42ms
# Beats 77.85%

# Memory 17.18MB
# Beats 30.55%

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lowOuter, highOuter = 0, len(matrix) - 1
        res = False
        while lowOuter <= highOuter:
            midOuter = (lowOuter + highOuter) // 2
            if matrix[midOuter][0] <= target and matrix[midOuter][-1] >= target:
                nums = matrix[midOuter]
                lowInner, highInner = 0, len(nums) - 1
                while lowInner <= highInner:
                    midInner = (lowInner + highInner) // 2
                    midValue = nums[midInner]
                    if midValue == target:
                        return True
                    elif midValue > target:
                        highInner = midInner - 1
                    else:
                        lowInner = midInner + 1 
                return res # Not found in targeted list     
            elif matrix[midOuter][0] > target:
                highOuter = midOuter - 1
            else:
                lowOuter = midOuter + 1
        return res # Not found in any list