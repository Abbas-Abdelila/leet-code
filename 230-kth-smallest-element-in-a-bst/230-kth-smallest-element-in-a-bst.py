# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        array = []
        def traverse(node):
            if node == None:
                return
            traverse(node.left)
            nonlocal array
            array.append(node.val)
            traverse(node.right)
        
        traverse(root);
        
        if array:
            return array[k-1]
        return -1