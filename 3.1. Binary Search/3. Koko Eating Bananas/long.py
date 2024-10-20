# Runtime 175ms
# Beats 98.40%

# Memory 17.78MB
# Beats 99.14%

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        res = 0
        while start <= end:
            speed = (start + end) // 2
            timeToEat = 0
            for i in range(len(piles)):
                timeToEat += math.ceil(piles[i] / speed)
            
            if timeToEat > h: # Missing time -> increase speed
                start = speed + 1
            else: # Redundant time -> reduce speed
                res = speed
                end = speed - 1
        return res
