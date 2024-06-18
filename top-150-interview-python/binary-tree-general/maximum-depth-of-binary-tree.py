from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        hright = 0
        hleft = 0
        if not root:
            return 0
        if root.left:
            hleft = self.maxDepth(root.left)
        if root.right:
            hright = self.maxDepth(root.right)
        if hright > hleft:
            return hright + 1
        else:
            return hleft + 1
        
# More sample:
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
        
#         hleft = self.maxDepth(root.left)
#         hright = self.maxDepth(root.right)
        
#         return max(hleft, hright) + 1