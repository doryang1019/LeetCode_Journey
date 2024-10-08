# Runtime 353ms
# Beats 30.10%

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ----------------------> l2r
        #  a     b     c     d
        # [1     a     ab    abc]
        
        # <---------------------- r2l
        #  a     b     c     d
        # [bcd   cd    d     1]

        # Mulplication
        # [bcd   acd   abd   abc]

        l2r, r2l = [1], deque([1])
        n = len(nums)
        for i in range(1, n):
            l2r.append(nums[i-1] * l2r[i-1])
            r2l.appendleft(nums[n-i] * r2l[0]) # r2l[0]: always get the lastest element
        r2l = list(r2l)

        res = [l2r[i] * r2l[i] for i in range(n)]

        return res