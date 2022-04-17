# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        sentinel = TreeNode(-1)
        tail = sentinel
        
        def inorder(node):
            if node == None:
                return
            
            inorder(node.left)
            nonlocal tail
            tail.right = node
            tail.left = None
            tail = tail.right
            tail.left=None
            
            inorder(node.right)
            tail.right=None
        
        inorder(root);
        return sentinel.right
        