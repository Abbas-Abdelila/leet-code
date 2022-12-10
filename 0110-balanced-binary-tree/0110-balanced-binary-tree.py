# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def max_depth(node):
            if not node:
                return 0
            
            return 1 + max(max_depth(node.left), max_depth(node.right))
        
        
        def is_balanced(node):
            if not node:
                return True
            
            left_depth = max_depth(node.left)   
            right_depth = max_depth(node.right)
            
            if abs(left_depth-right_depth) > 1:
                return False
            
            return is_balanced(node.left) and is_balanced(node.right)
        
        return is_balanced(root)