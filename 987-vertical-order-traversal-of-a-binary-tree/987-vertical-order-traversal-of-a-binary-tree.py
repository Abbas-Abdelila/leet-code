# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Creating dictionary of dictionary with defualt value as empty list
        D = collections.defaultdict(lambda : collections.defaultdict(list))
        
        #dfs to traverse through the tree
        #col and row are helped to identify the cell
        def dfs(node, col=0, row = 0):
            if not node:
                return 0
            D[col][row].append(node.val)
            dfs(node.left, col-1, row+1)
            dfs(node.right,col+1, row+1)
        dfs(root)  
        
        #creating list for maintaining all the columns
        ans = []
        for i in sorted(D):
            curCol = []
            for j in sorted(D[i]):
                curCol.extend(sorted(D[i][j]))
            ans.append(curCol)
        return(ans)