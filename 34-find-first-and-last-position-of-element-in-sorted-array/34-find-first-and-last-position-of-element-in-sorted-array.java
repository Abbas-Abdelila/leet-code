class Solution {
    public int[] searchRange(int[] nums, int target) {
        
        
        ArrayList<Integer> list = new ArrayList<Integer>();
        for(int num : nums) {
            list.add(num);
        }
        
        int[] array = {list.indexOf(target), list.lastIndexOf(target)};
        
        return array;
        
    }
}