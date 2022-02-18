class Solution {
    public String removeKdigits(String num, int k) {
        
        
        int size = num.length();
        
        Stack<Character> stack = new Stack<>();
        
        
        if(k==size) 
            return "0";
        
        int counter = 0;
        
        while(counter < size) {
            
            while(!stack.isEmpty() && k>0 && stack.peek() > num.charAt(counter)){
                stack.pop();
                k--;
            }
            
            stack.push(num.charAt(counter));
            counter++;
        }  
        
        while(k>0) {
            stack.pop();
            k--;
        }
        
        
        StringBuilder strbuilder = new StringBuilder();
        
        while(!stack.isEmpty()) {
            strbuilder.append(stack.pop());
        }
        
            
        strbuilder.reverse();
        
        while(strbuilder.length() > 1 && strbuilder.charAt(0)=='0'){
            strbuilder.deleteCharAt(0);
        }
        
        return strbuilder.toString();
        
    }
}