# Runtime 1ms
# Beats 64.24%

# Memory 16.92MB
# Beats 30.77%

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median1, median2 = 0, 0 # Median values

        nums1Length, nums2Length = len(nums1), len(nums2)
        noOfMedian = 2 if (nums1Length + nums2Length) % 2 == 0 else 1
        # Index of the first median
        indexMedian = (nums1Length + nums2Length) // 2 if noOfMedian == 1 else (nums1Length + nums2Length) // 2 - 1

        startNums1, startNums2 = 0, 0
        currentIndex, currentNoOfMedian = 0, 0
        currentNumber = 0
        while startNums1 <= nums1Length and startNums2 <= nums2Length:
            # Finished integrating the entire nums1, or the nums1 is empty
            if startNums1 == nums1Length:
                currentNumber = nums2[startNums2]
                startNums2 += 1
            # Finished integrating the entire nums2, or the nums2 is empty
            elif startNums2 == nums2Length:
                currentNumber = nums1[startNums1]
                startNums1 += 1
            else:
                if nums1[startNums1] <= nums2[startNums2]:
                    currentNumber = nums1[startNums1]
                    startNums1 += 1
                else: 
                    currentNumber = nums2[startNums2]
                    startNums2 += 1

            # Check if the current index is one of the median positions
            if currentIndex in {indexMedian, indexMedian + 1}:
                if currentIndex == indexMedian:
                    median1 = currentNumber
                else:
                    median2 = currentNumber
                currentNoOfMedian += 1

            currentIndex += 1
            if currentNoOfMedian == noOfMedian: # Enough number of medians
                break

        return median1 if noOfMedian == 1 else (median1 + median2) / 2.0