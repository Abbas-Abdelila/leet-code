class Solution {
    public int titleToNumber(String columnTitle) {
        char[] array = columnTitle.toCharArray();
        int total =0;
        for(int i=0; i<array.length; i++) {
           int current = array[i]-'A'+ 1;    
           total = total*26 + current ;
        }
        
        
        return total;
        
        
    }
}