# Runtime 280ms
# Beats 28.61%

# Memory 25.91MB
# Beats 37.11%

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        # prefix
        #  0 1 2 3 (index)
        #  1 2 3 4 (value)
        #  1 2 6 24 (first element stays 1, do the product from second element,  result = prefix[0] * nums[1], )
        # ------>

        # postfix
        # 1  2  3 4
        # 24 12 4 1
        # <------
        for i in range(len(nums)):
            #print(nums[i])
            if i == 0:
                continue
            else:
                prefix[i] = prefix[i-1] * nums[i-1]
        print(prefix)
        nums_reverse = nums[::-1]
        for i in range(len(nums_reverse)):
            if i == 0:
                continue
            else:
                postfix[i] = postfix[i-1] * nums_reverse[i-1]
        postfix_reverse = postfix[::-1]
        print(postfix_reverse)
        result = []
        for index, value in enumerate(prefix):
            value *= postfix_reverse[index]
            result.append(value)
        return result
