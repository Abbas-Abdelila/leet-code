# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        total_num = []
        total_sum = []
        ans = []
        queue = collections.deque([root])
                
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
            total_num.append(qLen)
            total_sum.append(sum(level))
        
        for i in range(len(total_num)):
            ans.append(total_sum[i]/total_num[i])
        
        return ans