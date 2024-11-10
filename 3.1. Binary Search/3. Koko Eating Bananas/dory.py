class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            middle = (left + right) //2

            hr = 0

            for pile in piles:
                hr += math.ceil(pile / middle)
            if hr <=h:
                right = middle
            else:
                left = middle +1

        return right
