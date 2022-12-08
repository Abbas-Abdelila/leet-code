# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(node, leaf_values):
            if not node:
                return 
            
            if node.left == None and node.right == None:
                leaf_values.append(node.val)
            else:
                dfs(node.left, leaf_values)
                dfs(node.right, leaf_values)

        
        leaf_values1 = []
        dfs(root1, leaf_values1)
        
        leaf_values2 = []
        dfs(root2, leaf_values2)
        
        return leaf_values1 == leaf_values2