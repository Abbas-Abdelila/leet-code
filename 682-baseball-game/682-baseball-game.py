class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        
        for i in ops:
            if(i == "+"):
                x,y = stack[-1], stack[-2]
                stack.append(x+y)
                
            elif(i=="D"):
                stack.append(stack[-1]*2)
                
            elif(i=="C"):
                stack.pop()
            else:
                stack.append(int(i))
                
        return sum(stack)