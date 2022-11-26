# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    
    def __init__(self, root: Optional[TreeNode]):
        
        def bfs(root):
            queue = collections.deque([root])
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node.left:
                        node.left.val = (2 * node.val) + 1
                        queue.append(node.left)
                        self.seen.add(node.left.val)
                    if node.right:
                        node.right.val = (2 * node.val) + 2
                        queue.append(node.right)
                        self.seen.add(node.right.val)
                    
        
        root.val = 0
        self.seen = set([0])
        bfs(root)

    def find(self, target: int) -> bool:
        return target in self.seen
        
    


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)