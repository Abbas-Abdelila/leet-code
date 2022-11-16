# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        
        def dfs(node, path):
            if node == None:
                return
            
            if node.left == None and node.right == None:
                paths.append(path + [str(node.val)])

            dfs(node.left, path+[str(node.val)])
            dfs(node.right, path+[str(node.val)])
        
        dfs(root, [])
        
        ans = []
        for path in paths:
            ans.append("->".join(path))
        
        return ans        