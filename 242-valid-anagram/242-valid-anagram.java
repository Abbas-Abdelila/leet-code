class Solution {
    public boolean isAnagram(String s, String t) {
        char[] string1 = s.toCharArray();
        char[] string2 = t.toCharArray();
        
        HashMap<Character, Integer> hashmap1 = new HashMap<>();
        for(char ch : string1) {
            if(hashmap1.containsKey(ch)){
                hashmap1.put(ch, hashmap1.get(ch) + 1);
            }
            else {
                hashmap1.put(ch, 1);
            }
        }
        
        HashMap<Character, Integer> hashmap2 = new HashMap<>();
        for(char ch : string2) {
            if(hashmap2.containsKey(ch)){
                hashmap2.put(ch, hashmap2.get(ch) + 1);
            }
            else {
                hashmap2.put(ch, 1);
            }
        }
        
        
        return hashmap1.equals(hashmap2);
        
    }
}