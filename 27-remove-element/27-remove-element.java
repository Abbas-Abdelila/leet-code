class Solution {
    public int removeElement(int[] nums, int val) {
        int counter = -1;
        for(int i=0; i<nums.length; i++) {
            if(nums[i]!=val) {
                counter++;
                nums[counter] = nums[i];
            }
             
        }
        
        return counter+1;    
        
    }
}