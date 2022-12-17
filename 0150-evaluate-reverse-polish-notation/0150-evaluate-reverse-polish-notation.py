class Solution:
    def evalRPN(self, tokens: List[str]) -> int:    
        
        operators = ["+", "-", "*", "/"]
        stack = []
        
        for i in tokens:
            if i in operators:
                num1 = stack.pop()
                num2 = stack.pop()
                
                match i:
                    case "+":
                        stack.append(num2 + num1)
                    case "-":
                        stack.append(num2 - num1)
                    case "*":
                        stack.append(num2 * num1)
                    case "/":
                        stack.append(int(num2 / num1))
                
            
            else:
                stack.append(int(i))
                
        return stack[0]
        