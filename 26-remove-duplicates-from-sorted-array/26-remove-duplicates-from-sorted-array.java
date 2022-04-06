class Solution {
    public int removeDuplicates(int[] nums) {
        int begin = 0;
        int end = 0;
        
        int size = nums.length;
        
        while(end<size) {
            if(nums[begin] == nums[end]) {
                end++;
            }
            else {
                begin++;
                nums[begin] = nums[end];
            }
        }
        
        return begin+1;
        
    }
}