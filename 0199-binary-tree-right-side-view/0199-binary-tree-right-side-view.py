# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def bfs(rootNode):
            if not rootNode:
                return []
            
            queue = collections.deque([rootNode])
            ans = []
            
            while queue:
                level = []
                qLen = len(queue)
                
                for _ in range(qLen):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                        
                    if node.right:
                        queue.append(node.right)
                    
                    level.append(node.val)
                ans.append(level[-1])
            
            return ans
        
        return bfs(root)        