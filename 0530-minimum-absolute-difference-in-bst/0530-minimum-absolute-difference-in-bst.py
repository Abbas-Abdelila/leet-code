# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # inorder traversal gives the result in sorted manner since it is BST
        def inorder(root, values):
            if not root:
                return 
            
            inorder(root.left, values)
            values.append(root.val)
            inorder(root.right, values)
        
        values = []
        inorder(root, values)
        diff = 10 ** 20
        for i in range(len(values)-1):
            diff = min(diff, values[i+1]- values[i])
        
        return diff