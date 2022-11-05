# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        
        def find(node):
            if node == None:
                return False
            
            if k - node.val in seen:
                return True
            
            seen.add(node.val)
            return find(node.left) or find(node.right)
        
        return find(root)