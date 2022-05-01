class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def parse(s):
            stack = []
            
            for c in s:
                if c == "#":
                    if len(stack) > 0:
                        stack.pop()
                else:
                    stack.append(c)
                
            return "".join(stack)
            
        return parse(s) == parse(t)    
           
        
        