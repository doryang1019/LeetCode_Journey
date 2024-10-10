# Runtime 76ms
# Beats 99.51%

# Memory 12.46MB
# Beats 59.09%

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while r > l: 
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            elif total > target: # Need to reduce total
                r -= 1
            else:
                l += 1 # Need to increase total