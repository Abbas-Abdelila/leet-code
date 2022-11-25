# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        queue = collections.deque([root])
        flag = False
        while queue:
            qLen = len(queue)
            level = []
            for _ in range(qLen):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                if flag:
                    level.insert(0, node.val)
                else:
                    level.append(node.val)
            ans.append(level)
            flag = not flag
        
        return ans        