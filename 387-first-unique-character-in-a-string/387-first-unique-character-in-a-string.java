class Solution {
    public int firstUniqChar(String s) {
        int[] c = new int[26];
        for(char i: s.toCharArray()){
            c[i-'a']++;
        }
        
        
        for(char i: s.toCharArray()) {
            if(c[i-'a']==1){
                return s.indexOf(Character.toString(i));                
            }
        }
        
        
        return -1;
        
       
    }
}