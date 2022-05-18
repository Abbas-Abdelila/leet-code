# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        def height(node):
            if node == None:
                return 0
            
            leftDepth = height(node.left)
            rightDepth = height(node.right)
            
            if leftDepth > rightDepth:
                return leftDepth+1
            else:
                return rightDepth+1
        
        k = height(root)
        total = 0
        
        def traverse(node, k):
            if node == None:
                return 0
            if node.left==None and node.right==None:
                if k==1:
                    nonlocal total
                    total += node.val
            traverse(node.left, k-1)
            traverse(node.right, k-1)
        
        traverse(root, k)
        
        return total
            
            
            
            
            
            
        