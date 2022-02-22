class Solution {
    public int titleToNumber(String columnTitle) {
        
        int total = 0;
        for(int i=0; i<columnTitle.length(); i++) 
            total+=Math.pow(26, columnTitle.length()-i-1) * (columnTitle.charAt(i)-64);
        
        return total;
        
    }
}