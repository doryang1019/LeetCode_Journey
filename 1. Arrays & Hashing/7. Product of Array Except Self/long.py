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

        l2r, r2l = [], deque([])
        n = len(nums)
        for i in range(n):
            if i == 0:
                l2r.append(1)
                r2l.append(1)
            else:
                l2r.append(nums[i-1] * l2r[i-1])
                r2l.appendleft(nums[n-i] * r2l[0]) # r2l[0]: always get the lastest element
        r2l = list(r2l)

        res = []
        for i in range(n):
            res.append(l2r[i] * r2l[i])

        return res

