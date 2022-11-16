# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def bfs(rootNode):
            if not rootNode:
                return []
            
            queue = collections.deque([rootNode])
            res = []
            while queue:
                level = []
                for i in range(len(queue)):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                        
                    level.append(node.val)
                res.insert(0,level)
            
            return res
            
        return bfs(root)
                    