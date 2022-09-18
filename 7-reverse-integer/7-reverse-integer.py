class Solution:
    def reverse(self, x: int) -> int:
        
        if x > 0:
            x = str(x)
            x = int(x[::-1])
        else:
            x *= -1
            x = int(str(x)[::-1])
            x *= -1
            
        if -2**(31) <= x <= 2**(31) - 1:
            return x
        else:
            return 0
        