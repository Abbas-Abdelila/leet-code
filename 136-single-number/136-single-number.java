class Solution {
    public int singleNumber(int[] nums) {
        
        
        int singleNumber = 0;
        for(int i=0; i<nums.length; i++) {
            // XOR -> if "singleNumber" and number are different it is passed to "singleNumber". 
            singleNumber ^=nums[i];
        }
        
        return singleNumber;
    }
}