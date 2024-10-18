# Runtime 131ms
# Beats 100.00%

# Memory 36.12MB
# Beats 88.05%

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        carsSortedByPosition = sorted(cars)

        noFleet = 0
        while carsSortedByPosition:
            carLast = carsSortedByPosition.pop()
            timeArrivalLast = (target - carLast[0]) / carLast[1]
            while carsSortedByPosition:
                carSecondLast = carsSortedByPosition[-1]
                # Check how long the car will reach to target
                timeArrivalSecondLast = (target - carSecondLast[0]) / carSecondLast[1] 

                if timeArrivalSecondLast <= timeArrivalLast: # If can merge, remove that car from stack
                    carsSortedByPosition.pop()
                else: # Will be another fleet because the speed is lower than the last car
                    break
            noFleet += 1

        return noFleet