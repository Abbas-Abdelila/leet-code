# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        ans = 0
        
        def preorder(node, x):
            
            nonlocal ans
            if node == None:
                return 
            
            if node.val >= x:
                ans += 1
                x = node.val
            
            preorder(node.left, x)
            preorder(node.right, x)
        
        
        preorder(root, root.val)
        
        return ans
        