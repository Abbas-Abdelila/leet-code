# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        def bfs(root_node):
            if not root_node:
                return 0
            queue = collections.deque([root_node])
            size = 0
            
            while queue:
                qLen = len(queue)
                for _ in range(qLen):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    
                size += 1
            
            return size
        
        return bfs(root)        