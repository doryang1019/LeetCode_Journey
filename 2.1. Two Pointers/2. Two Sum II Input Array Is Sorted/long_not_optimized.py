# Runtime 99ms
# Beats 30.30%

# Memory 13.04MB
# Beats 6.93%

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers) 
        for l in range(n):
            if l > 0 and numbers[l] == numbers[l - 1]:
                continue
            r = l + 1
            while r < n: 
                total = numbers[l] + numbers[r]
                if total == target:
                    return [l + 1, r + 1]
                elif total > target:
                    break
                r += 1