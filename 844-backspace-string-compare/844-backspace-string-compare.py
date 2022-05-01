class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        stock = []
        for i in range(len(s)):
            
            try:
                if s[i] == "#":
                    stack.pop()
                else:
                    stack.append(s[i])
            except: 
                continue
                
        for i in range(len(t)):
            
            try:
                
                if t[i] == "#":
                    stock.pop()
                else:
                    stock.append(t[i])
            except: 
                continue
        
        return stack == stock