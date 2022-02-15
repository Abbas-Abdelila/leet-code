class Solution {
    public int singleNumber(int[] nums) {
        ArrayList<Integer> numbers = new ArrayList<>();
        
        for(int i=0; i<nums.length; i++) {
            if(numbers.contains(nums[i])) {
                numbers.remove(numbers.indexOf(nums[i]));
            }
            else {
                numbers.add(nums[i]);
            }
        }
        
        return numbers.get(0).intValue();
        
        
    }
}