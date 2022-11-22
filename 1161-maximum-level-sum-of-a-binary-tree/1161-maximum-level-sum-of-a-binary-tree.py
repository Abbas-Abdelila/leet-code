# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        d = {}
        q = collections.deque([root])
        count = 0
        while q:
            level = 0 
            count += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level += node.val
            if level not in d:
                d[level] = count
        
        maximum = max([key for key in d.keys()])
        return d[maximum]
        
        