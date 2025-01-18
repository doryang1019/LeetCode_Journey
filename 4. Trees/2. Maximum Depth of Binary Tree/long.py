# Runtime 7ms
# Beats 5.39%

# Memory 18.98MB
# Beats 42.21%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        
        # Return 1 (for current node) + maximum of left and right depths
        return 1 + max(leftDepth, rightDepth)