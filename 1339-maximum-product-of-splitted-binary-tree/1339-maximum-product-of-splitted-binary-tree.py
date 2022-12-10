# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0
            
            ans = node.val + dfs(node.left) + dfs(node.right)
            has.append(ans)
            return ans 
        
        has = []
        sum_all = dfs(root)
        
        return max((sum_all-i)*i for i in has) % (10**9 +7)            
        