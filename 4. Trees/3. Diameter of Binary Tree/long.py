# Runtime 3ms
# Beats 94.11%

# Memory 20.65 MB 
# Beats 77.14%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def length(self, node):
        if not node:
            return 0
        
        # Get lengths of left and right subtrees
        left_length = self.length(node.left)
        right_length = self.length(node.right)
        
        # Update diameter if path through current node is longer
        self.diameter = max(self.diameter, left_length + right_length)
        
        # Return length of current node
        return 1 + max(left_length, right_length)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.length(root)
        return self.diameter