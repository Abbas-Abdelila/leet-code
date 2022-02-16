/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    ArrayList<Integer> numbers = new ArrayList<>();
    public boolean findTarget(TreeNode root, int k) {
        if(root==null)
            return false;
        
        inorder(root);
        
        int left = 0; 
        int right = numbers.size()-1;
        
        while(left<right) {
            if(numbers.get(left)+numbers.get(right) == k)
                return true;
            else if(numbers.get(left)+numbers.get(right) > k)
                right--;
            else 
                left++;
        }
        
        return false;
        
    }
    
    private void inorder(TreeNode root) {
        if(root==null)
            return;
        
        inorder(root.left);
        numbers.add(root.val);
        inorder(root.right);
    }
}