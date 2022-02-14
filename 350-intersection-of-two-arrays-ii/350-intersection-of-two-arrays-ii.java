class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        ArrayList<Integer> list = new ArrayList<>();
        ArrayList<Integer> list1 = new ArrayList<>();
        
        for(int i=0; i<nums1.length; i++) {
            list1.add(nums1[i]);
        }
            
        for(int i=0; i<nums2.length; i++) {
            if(list1.contains(nums2[i])) {
                list.add(nums2[i]);
                int index = list1.indexOf(nums2[i]);
                list1.remove(index);
            }
                
        }
        
        int[] array = new int[list.size()];
        for(int i=0; i<array.length; i++) {
            array[i] = list.get(i);
        }
        
        return array;
    }
}