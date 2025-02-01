# Runtime 58ms
# Beats 56.49%

# Memory 20.90MB
# Beats 67.98%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Get the current node value
        curr = root.val
        
        # If both p and q are greater than current node, LCA is in right subtree
        if p.val > curr and q.val > curr:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # If both p and q are less than current node, LCA is in left subtree
        if p.val < curr and q.val < curr:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # If one value is less and other is greater or one of them equals current value
        # LCA is current node
        return root