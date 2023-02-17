# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from sortedcontainers import SortedList
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        nodes = SortedList()
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            nodes.add(node.val)
            inorder(node.right)
        
        inorder(root)
        
        min_diff = 10 ** 20
        for i in range(1, len(nodes)):
            min_diff = min(min_diff, nodes[i] - nodes[i-1])
        
        return min_diff
        
            