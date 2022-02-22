class Solution {
    public int titleToNumber(String columnTitle) {
        char[] array = columnTitle.toCharArray();
        
        int total = 0;
        for(int i=0; i<array.length; i++) 
            total+=Math.pow(26, array.length-i-1) * (array[i]-64);
        
        return total;
        
    }
}