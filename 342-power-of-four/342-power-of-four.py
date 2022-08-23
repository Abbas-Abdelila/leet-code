class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        from math import log
        if n < 1:
            return False
        
        return (math.log(n, 4)) % 1 == 0