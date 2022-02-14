class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashmap = new HashMap<>();
        int[] result = new int[2];
        
        for(int i=0; i<nums.length; i++) {
            if(hashmap.containsKey(target-nums[i])){
                result[0] = i;
                result[1] = hashmap.get(target-nums[i]);
            }
            hashmap.put(nums[i], i);
        }
        
        return result;
    }
}