# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        # Approach 
        # 1. Have a helper function that takes a node
        # and returns True or False by calculating the average.
        def average_same(root):
            q = collections.deque([root])
            count = 0
            total = 0
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    total += node.val
                    count += 1
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    
            average = total//count
            return average == root.val
        # 2. Call the helper function on every node and when found increment
        # count
        ans = 0
        q = collections.deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                
                if average_same(node):
                    ans += 1
                    
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return ans
            