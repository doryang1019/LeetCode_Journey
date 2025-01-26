# Runtime 43ms
# Beats 61.83%

# Memory 17.83MB
# Beats 69.21%

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
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        # If root is None but subRoot isn't -> Can't be a subtree
        if not root:
            return False
        
        # Check if current tree matches or subtree matches
        return (self.isSameTree(root, subRoot) or 
                self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))
        