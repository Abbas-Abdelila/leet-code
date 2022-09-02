# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        Sum = defaultdict(float)
        Total = defaultdict(int)
        ans = []
        
        def dfs(node, h):
            if not node:
                return
            
            dfs(node.left, h+1)
            dfs(node.right, h+1)
            Sum[h] += node.val
            Total[h] += 1
        
        dfs(root, 0)
        
        for i in range(len(Sum)):
            ans.append(Sum[i]/Total[i])
        
        return ans
            