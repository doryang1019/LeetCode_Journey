# Runtime 0ms
# Beats 100.00%

# Memory 18.01MB
# Beats 13.89%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both trees are None -> Same
        if not p and not q:
            return True
        
        # One tree is None while the other isn't -> Different
        if not p or not q:
            return False
        
        # Check if current node values are the same
        if p.val != q.val:
            return False
        
        # Check left and right subtrees
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))