# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
#         array = []
#         def traverse(node):
#             if node == None:
#                 return
#             traverse(node.left)
#             nonlocal array
#             array.append(node.val)
#             traverse(node.right)
        
#         traverse(root);
        
#         if array:
#             return array[k-1]
#         return -1

#         Time and Space Complexity -> O(n)

#         Efficent solution
                      
        
        left = k
        result = None
            
        def inorder(node):
            if node is None:
                return 

            if(k<0):
                return -1
            
            inorder(node.left)

            nonlocal left
            left-=1
            if left==0:
                nonlocal result
                result = node.val

            inorder(node.right)
        
        inorder(root);
        return result
    # Time Complexity -> O(h)  Space Complexity -> O(1)