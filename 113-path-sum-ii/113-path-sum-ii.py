# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []
        def dfs(node, path, sm):
            if node == None:
                return node
            
            tmp = path+[node.val]
            sm += node.val
            
            if node.left:
                dfs(node.left, tmp, sm)
            if node.right:
                dfs(node.right, tmp, sm)
            
            if not node.left and not node.right and sm == targetSum:
                nonlocal ans
                ans.append(tmp)
            
        if not root: 
            return []
        dfs(root, [], 0)
        return ans
        