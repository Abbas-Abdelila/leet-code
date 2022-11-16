# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def height_left(node):
            counter = 0
            while node:
                counter += 1
                node = node.left
            
            return counter
        
        def height_right(node):
            counter = 0
            while node:
                counter += 1
                node = node.right
            
            return counter
        
        def dfs(node):
            if node == None:
                return 0
            
            return dfs(node.left) + dfs(node.right) + 1
        
        left = height_left(root)
        right = height_right(root)

        if left == right:
            return (2**left) - 1
        else:
            return dfs(root)
         
        
        
        
        