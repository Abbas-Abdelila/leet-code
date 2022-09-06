# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        if not root.left and not root.right:
            return root if root.val == 1 else None
        
        root.left = self.pruneTree(root.left)
        root.right= self.pruneTree(root.right)
        
        return root if root.left or root.right or root.val == 1 else None